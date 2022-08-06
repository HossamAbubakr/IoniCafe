import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from database.models import db_drop_and_create_all, setup_db, Drink
from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)
'''
@ uncomment the following line to initialize the datbase
'''
#db_drop_and_create_all()

## ROUTES


@app.route('/')
def index():
    return jsonify('Nothing to see here')


@app.route('/drinks')
def get_drinks():
    drinks_list = Drink.query.order_by(Drink.title).all(
    )  # Get all drinks and order them by the title alphabetically.
    if len(drinks_list) < 1:  # If there are no drinks
        abort(422)
    drinks = [drink.short() for drink in drinks_list
              ]  # Inline for loop for formatting the drinks
    return jsonify({'success': True, 'drinks': drinks})


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drinks_detail(payload):
    drinks_list = Drink.query.order_by(Drink.title).all()
    if len(drinks_list) < 1:
        abort(404)
    drinks = [drink.long() for drink in drinks_list]
    return jsonify({'success': True, 'drinks': drinks})


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_drink(payload):
    try:
        request_body = request.get_json()  # Get the request body
        drink_title = request_body.get(
            'title')  # Get the title from the request body
        drink_recipe = request_body.get(
            'recipe')  # Get the recipe from the request body
        if ('title' not in request_body) and ('recipe' not in request_body):
            abort(400, "Missing or empty request headers")
        new_drink = Drink(title=drink_title, recipe=json.dumps(drink_recipe))
        new_drink.insert()
    except Exception as err:
        abort(500, str(err))
    return jsonify({'success': True, 'drinks': new_drink.long()})


@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def patch_drink(payload, drink_id):
    try:
        drink = Drink.query.get(drink_id)
        if not drink:
            abort(422)
        request_body = request.get_json()
        if ('title' not in request_body) and ('recipe' not in request_body):
            abort(400, "Both title and recipe attributes are missing or empty")
        drink_title = request_body.get('title')
        drink_recipe = request_body.get('recipe')
        if drink_title:  # Partial update
            drink.title = drink_title
        if drink_recipe:
            drink.recipe = drink_recipe
        drink.update()
    except Exception as err:
        abort(500, str(err))
    return jsonify({'success': True, 'drinks': drink.long()})


@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('patch:drinks')
def delete_drink(payload, drink_id):
    try:
        drink = Drink.query.get(drink_id)
        if not drink:
            abort(422, "No such drink with that ID exists!")
        drink.delete()
    except:
        abort(500, "Server error, please try again later")
    return jsonify({'success': True, 'delete': drink_id})


## Error Handling


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message":
        "internal server error  " + str(error)  # Customized error message
    }), 500


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable " + str(error)
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found " + str(error)
    }), 404


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request " + str(error)
    }), 400


@app.errorhandler(
    AuthError
)  # Taken from auth0 official documentation https://auth0.com/docs/quickstart/backend/python/01-authorization
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "unauthorized " + str(error)
    }), 401
