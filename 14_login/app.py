# Ray Onishi, Shafali Gupta - Devo Squad!
# SoftDev1 pd7
# K14 -- Do I Know You?
# 2018-10-01

from flask import Flask,render_template,session,request,url_for,redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

#hardcoded user
#user1 = "tester"
#pass1 = "test"
users = {"tester":"test"}

error = ""

#checks the credentials against the hard coded user
def check_credentials(username,password):
    #return username ==  and password == pass1
    if username in users.keys():
        if password == users[username]:
            return True;
        else:
            return False

@app.route("/")
def home():
    global error
    #if the user is in session, render the welcome page
    if "user" in session:
        return render_template('auth.html',username=session["user"])
    #resetting error after the message has been stored
    errorMessage = error
    error = ""
    #otherwise render the login page, shows an error if bad username/password was inputted
    return render_template('login.html',errorMessage=errorMessage)


# @app.route('/auth', methods = ["POST"])
# # userf = "test"
# # passwordf = "password1"
# def authenticate():
#     userf = "test"
#     passwordf = "password1"
#     user = request.form['username']
#     passw = request.form['password']
#     if (user != userf):
#         return "incorrect username"
#     if (passw != passwordf):
#         return "incorrect password"
#     else:
#         redu



@app.route("/logout")
def logout():
    #removes the user from the session
    session.pop("user")
    #redirects to the home page after logging user out
    return redirect(url_for('home'))

@app.route("/auth",methods=["POST"])
def authenticate():
    #needed to modify the global variable error (to be used in home)
    global error
    username = request.form['username']
    password = request.form['password']
    #if the credentials match, add the user to session
    if check_credentials(username,password):
        session["user"] = username
    #checks for bad username
    elif username not in users.keys():
        error = "bad username!"
    #otherwise it has to be a bad password
    else:
        error = "bad password!"
    #redirecting to home
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.run()
