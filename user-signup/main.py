from flask import Flask, request, render_template, redirect
import cgi
import os
import jinja2


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template ('index.html')

@app.route("/signup", methods=['POST'])
def register():
    username = request.form['username']
    password1 = request.form['password1']
    password2 = request.form['password2']
    email = request.form['email']

    usernameError =""
    password1Error = ""
    password2Error = ""
    emailError = ""
    count = 0

    if not username and len(username) >20 or len(username)<3:
        usernameError = "Username is required and must be 3 to 20 characters long"
        print("username error")
    
    for letter in username:
        if(letter.isspace()) == True:
            count +=1
            usernameError = "Username should not contain space"

        else:
            print ("no error")
  
    if not password1 and len(password1) >20 or len(password1) < 3:
        password1Error = "Password is required and must be 3 to 20 characters long"
    if password1 != password2:
        password2Error= "Passwords must match"
    if email:
        if "@" in email:
            emailError = ""
        else:
            emailError = "Must be a valid email"

    if usernameError or password1Error or password2Error or emailError:
        print("there was an error!")
        return render_template ("index.html", username= username, usernameError= usernameError,
        password1Error=password1Error,password2Error=password2Error,
        emailError=emailError)
    else:
        return render_template("welcome.html", username=username)



app.run()