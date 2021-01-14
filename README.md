# Ionic Café, Ionic/Angular Auth0 Cafe App

![Showcase.gif](/Showcase.gif)

## Table of Contents

* [Summary](#Summary)

* [Technologies](#Technologies)

* [Features](#Features)

* [Structure](#Structure)

* [RBAC](#RBAC)

* [Documentation and Unit Testing](#Documentation-and-Unit-Testing)

* [Usage and Installation](#usage-and-installation)

## Summary

Ionic Café is an app to manage drinks for a café, it is built using Ionic, Python and Flask that I built to practice full stack programming as part of udacity nanodegree.

It demonstrates my understanding of full stack development, including creating and deploying a flask server as a backend to an Ionic front end and implementing Oauth (Auth0 in this case) with tiered access/permissions using RBAC (role-based access control)

## Technologies

Flask was used as a backend using python.  
SQLite as the database I used.  
SQLAlchemy as the ORM of choice.  
Ionic/Angular was used for the front end.  
Auth0 was used for Oauth and RBAC.  
JOSE is used for creating and signing JWTs.

## Features
1. Display graphics representing the ratios of ingredients in each drink.

1. Tiered access system for users and employees.

2. Authenticating employees using Auth0.

3. Allows public users to view drink names and graphics.

4. Allows the shop baristas to see the recipe information.

5. Allows the shop managers to create new drinks and edit existing drinks.


## Structure
```
+---backend
|   |   requirements.txt
|   |   The Ionic Cafe.postman_collection.json
|   |   
|   \---src
|       |   api.py
|       |   
|       +---auth
|       |       auth.py
|       |       __init__.py
|       |       
|       \---database
|               database.db
|               models.py
|               
\---frontend
    |   angular.json
    |   ionic.config.json
    |   package-lock.json
    |   package.json
    |   tsconfig.json
    |   tslint.json
    |   
    +---e2e
    |   |   protractor.conf.js
    |   |   tsconfig.e2e.json
    |   |   
    |   \---src
    |           app.e2e-spec.ts
    |           app.po.ts
    |           
    \---src
        |   global.scss
        |   index.html
        |   karma.conf.js
        |   main.ts
        |   polyfills.ts
        |   test.ts
        |   tsconfig.app.json
        |   tsconfig.spec.json
        |   tslint.json
        |   zone-flags.ts
        |   
        +---app
        |   |   app-routing.module.ts
        |   |   app.component.html
        |   |   app.component.spec.ts
        |   |   app.component.ts
        |   |   app.module.ts
        |   |   
        |   +---pages
        |   |   +---drink-menu
        |   |   |   |   drink-menu.module.ts
        |   |   |   |   drink-menu.page.html
        |   |   |   |   drink-menu.page.scss
        |   |   |   |   drink-menu.page.spec.ts
        |   |   |   |   drink-menu.page.ts
        |   |   |   |   
        |   |   |   +---drink-form
        |   |   |   |       drink-form.component.html
        |   |   |   |       drink-form.component.scss
        |   |   |   |       drink-form.component.spec.ts
        |   |   |   |       drink-form.component.ts
        |   |   |   |       
        |   |   |   \---drink-graphic
        |   |   |           drink-graphic.component.html
        |   |   |           drink-graphic.component.scss
        |   |   |           drink-graphic.component.spec.ts
        |   |   |           drink-graphic.component.ts
        |   |   |           
        |   |   +---tabs
        |   |   |       tabs.module.ts
        |   |   |       tabs.page.html
        |   |   |       tabs.page.scss
        |   |   |       tabs.page.spec.ts
        |   |   |       tabs.page.ts
        |   |   |       tabs.router.module.ts
        |   |   |       
        |   |   \---user-page
        |   |           user-page.module.ts
        |   |           user-page.page.html
        |   |           user-page.page.scss
        |   |           user-page.page.spec.ts
        |   |           user-page.page.ts
        |   |           
        |   \---services
        |           auth.service.ts
        |           drinks.service.ts
        |           
        +---assets
        |   |   shapes.svg
        |   |   
        |   \---icon
        |           favicon.png
        |           
        +---environments
        |       environment.prod.ts
        |       environment.ts
        |       
        \---theme
                variables.scss
```

## RBAC

**Baristas**  
``
get:drinks-detail
``  

**Managers**  
``
post:drinks
``  
``
patch:drinks
``  
``
delete:drinks
``

## Documentation and Unit Testing

A complete Postman collection json file **The Ionic Cafe.postman_collection.json** with examples and unit tests is provided

## Usage and Installation

a database.db file is already included and ready for use.
You can get the project up and running in a few simple steps.

**Back End**

1. Use the following command to install the required packages
```
pip install -r requirements.txt
```
2. Supply your own Auth0 information at auth/auth.py
```
AUTH0_DOMAIN = 'AUTH0_DOMAIN_HERE'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'AUDIENCE_HERE'
```
3. Use The following command to start the server.
```
set FLASK_APP=api.py
flask run
```
**Front End**
1. Use the following command to install Ionic CLI
```
npm install -g @ionic/cli
```
2. Use the following command to install the required packages
```
npm install
```
3. Supply your own Auth0 information at \src\environments\environment.ts
```
url: 'URL HERE',
audience: 'AUDIENCE HERE',
clientId: 'CLIENT ID HERE',
```
4. Use The following command to start ionic!
```
ionic serve
```
