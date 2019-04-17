from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True
form= """
<!DOCTYPE html>
<html>
<body>
    <h1> My Sign-Up Form </h1>
    <form action="/welcome" method="POST">
        <label for="username">Username:</label>
        <input id="username" type="text" name="username"/>

        <br>
        <br>

        <label for="password1">Write Password:</label>
        <input id= password1 type="password" name= "password1"/>

         <br>
         <br>

        <label> Rewirte Password:
        <input id="password2" type="password" name= "password2"/>
        </label>
        
        <input type="submit"/>


    </form>
</body>
</html>
"""
@app.route ("/welcome", methods=['POST'])
def welcome():
    username= request.form ["username"]
    return  '<h1>Welcome,' + username + '</h1>'
        
        

@app.route("/")
def index():
    return form

app.run()
