from flask import Flask, request
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-5" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Validation Example</title>
    <link rel="stylesheet" href="/static/app.css" />
  </head>
  <body>
  """

page_footer = """
<body>
<html>"""

signup_form= """
<form action="/welcome" id="form" method="POST">
        <h1> Signup Form </h1>
        <label for="username">Username:</label>
        <input id="username" type="text" name="username" value= "{0}"/>
        <p class="error"> {1} </p>    
        <label for="password1">Write Password:</label>
        <input id= password1 type="password" name= "password1" value= "{2}"/>
         <p class="error"> {3} </p> 
        <label> Rewirte Password:
        <input id="password2" type="password" name= "password2" value= "{4}"/>
        <p class="error"> {5} </p> 
        </label>
        <button type="submit">Submit</button>
    </form>
"""


@app.route("/")
def index():
    content= page_header + signup_form.format("", "", "", "", "","") + page_footer
    return content 

@app.route("/welcome", methods=['POST'])
def welcome():
    username = cgi.escape(request.form ['username'])
    
    welcome_message = '<h1>Welcome, ' + username + '</h1>'
    content = page_header + welcome_message + page_footer
    return content
        
app.run()
