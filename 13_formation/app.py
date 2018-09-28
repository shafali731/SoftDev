#Shafali Gupta
#SoftDev pd7
#K13 -- Echo Echo Echo
#2018-09-28
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/auth', methods = ['POST'])
def auth():
    if request.method == "POST":
        return render_template("auth.html", name = "BRRRUHHHH", method = request.method)
   # print(app)
   # print(request)
   # print(request.args)
   # print(request.args['username'])
   # print(request.headers)
    else:
        return render_template('auth.html', name= request.args['username'], method = request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
