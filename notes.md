## \_\_init__
```py

from flask import Flask
app = Flask(__name__)
app.secret_key = "skittles"

```

## Server
```py
from flask import Flask
app = Flask(__name__)
app.secret_key = "skittles"
```
## Config
```py
import pymysql.cursors
class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', # change the user and password as needed
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        self.connection = connection
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                executable = cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # if the query is an insert, return the id of the last row, since that is the row we just added
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # if the query is a select, return everything that is fetched from the database
                    # the result will be a list of dictionaries
                    result = cursor.fetchall()
                    return result
                else:
                    # if the query is not an insert or a select, such as an update or delete, commit the changes
                    # return nothing
                    self.connection.commit()
            except Exception as e:
                # in case the query fails
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# this connectToMySQL function creates an instance of MySQLConnection, which will be used by server.py
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)

```
## Models
```py
# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 


class (User)/no():
    def __init__(self,data):
        self.id = data['id']

# C ****************************************
# C ****************************************
# C ****************************************

    @classmethod
    def create(cls,data):
        query = "INSERT INTO (users/no()) (*something*, *something*) VALUES (%(*something*)s, %(*something*)s);"
        (user/no())_id = connectToMySQL('(userS/no())').query_db(query,data)
        return (user/no())_id

# R ****************************************
# R ****************************************
# R ****************************************

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM (users)/no());"
        (userS/no()) = connectToMySQL('*userS*').query_db(query)
        (userS/no()) = []
        for user in (userS/no()):
            (userS/no()).append(cls(user))
        return (userS/no()) 

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM burgers WHERE burgers.id = %(id)s;"
        burger_from_db = connectToMySQL('burgers').query_db(query,data)

        return cls(burger_from_db[0])

	# (joining two groups)  
    # add... from .model_(user/no()) import (User/no()) **to top of page 
	# add... self.(users/no()) = [] **to class(User/no()):
    @classmethod
    def get_one_with_ninjas(cls, data ):
        print(data)
        query = "SELECT * FROM (userS/no()) LEFT JOIN ninjas on (userS/no()).id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('***userS***').query_db(query,data)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            # users = [] in self dictionary
            dojo.(userS/no()).append( ***User***(n) )
        return dojo

# U ****************************************
# U ****************************************
# U ****************************************

# D ****************************************
# D ****************************************
# D ****************************************

```
## Controllers
```py
# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.(user/no()) import (User/no())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    data = {
        # 'id' : id
        "(something/no())" : requestform['(somethong/no())'],
        "(something/no())" : requestform['(somethong/no())'],
    }
    Sample.create(data)
    return redirect('/sample')

# Left Join --- Works with models 'get_one_with_....'
@app.route('/sample/<int:id>')
def sample(id):
    data = {
    "id": id
    }
    return render_template('dojo_info.html', dojo=Dojo.get_one_with_ninjas(data))   
```

## Bootstrap CSS
```py
# Name Input

<div class="input-group mb-3">
    <span class="input-group-text" id="inputGroup-sizing-default">First Name</span>
    <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" name="first_name">
</div>  

# SELECT/OPTION Dropdown

<select class="my-2 form-select" aria-label="Default select example">
    <option selected>Open this select menu</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
</select>

# Label with Text Box

<div class=" my-4 mb-3">
    <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
</div>

#Table (striped rows)

<table class="table table-striped table-hover">
  ...
</table>

# Button
 
	Blue-*** <button type="submit" class="btn btn-primary">Primary</button>
```
## Validation
```py
#models
@staticmethod
def vaildate_user(user):
    is_valid = True # we assume this is true

    # for ***Text Input*** unknown
    if len(user['first_name]) < 1: 
        flash("first_name must be included.")
        is_valid = False  #-- use different if statement for all inputs
    return is_valid

    # for ***Select/Options Input***
    if len(ninja['location']) < 2: 
        flash("Language must be included.")
        is_valid = False  #-- use different if statement for all inputs
    return is_valid

    # for ***EMAIL***
    import re	# the regex module  <--- add to /model top
    # create a regular expression object that we'll use later   
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #<--- Add to /model top

    if not EMAIL_REGEX.match(user['email']): 
        flash("Invalid email address!")
        is_valid = False
    return is_valid


#contoller

# For ***Registration***

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    return redirect('/dashboard')

# *** For Form Correctness***

@app.route('/create', methods=['POST'])
def create():
    if not Survey.vaildate_info(request.form):
        return redirect('/')

#HTML
{% with messages = get_flashed_messages() %}     <!-- declare a variable called messages -->
    {% if messages %}                            <!-- check if there are any messages -->
        {% for message in messages %}            <!-- loop through the messages -->
            <p>{{message}}</p>                   <!-- display each message in a paragraph tag -->
        {% endfor %}
    {% endif %}
{% endwith %}

```
## HTML
```py
##Validation Messages


