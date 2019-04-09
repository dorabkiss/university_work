# The mytwits app is a simple twitter clone
A web application built with the Flask microframework that has user authentication (flask-login), a MySQL database backend that implements CRUD operations, and a basic API that supports get, post, push, and delete.

### Tools: 
- jinja template engine
- wtforms
- flask-login: user authentication
- flask-restful: basic api
- sqlalchemy

### Features:
**there is more than one route and more than one view**

- routes: /login, /logout, /register, /edit twit, /add_twit, /<username>
- views: index, login, register, timeline


**the html is rendered using jinja templates**
- the jinja templates include some control structure(S) e.g. if/else, for/endfor

**it includes one or more forms**
- the forms have some validation
- there are feedback messages to the user
- use of wtforms 

**it has a database backend that implements CRUD operations**
- mysql database 
- the create & update operations take input data from a form or forms
- use of sqlalchemy 

**there is user authentication (i.e. logins)**
- the login process uses sessions
- passwords are stored as hashes
- use of a salt 
- there is a way to logout
- use of flask-login to authenticate users

**there is a basic api i.e. content can be accessed as json via http methods**
- basic api that implements/supports get, post, push, and delete
- use of flask-restful


*replace the text in <> with your twit and corresponding user_id or twit_id*

- to get twits using curl:
            curl -i localhost:8000/api

- to get a specific twit using curl:
            curl -i localhost:8000/api/<TWIT_ID_HERE>

- to post a twit using a form:
            curl -d "twit='<YOUR_MESSAGE_HERE>'&user_id=<YOUR_USER_ID>&submit=SUBMIT" localhost:8000/api

- to post a twit as json:
            curl -H "Content-Type: application/json" -X POST -d '{"twit":"<YOUR_MESSAGE_HERE>","user_id":<YOUR_USER_ID>}' http://localhost:8000/api

- to edit a twit:
            curl -d "twit=<YOUR_MESSAGE_HERE>" localhost:8000/api/<TWIT_ID_HERE> -X PUT -v

- to delete a twit:
            curl localhost:8000/api/<TWID_ID_HERE> -X DELETE -v