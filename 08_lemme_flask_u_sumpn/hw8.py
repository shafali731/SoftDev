#Shafali Gupta
#SoftDev1 pd07
#K08 -- Fil  Yer Flask
#2018-09-18
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
     print(__name__)
     return "ayooo!"


@app.route("/csTeachers")
def teachers():
    return "Get rid of windows and download <b>ubuntu</b>. Ubuntu is <b>GOD</b>"

@app.route("/stuyKids")
def kids():
    return " <b>\"Everybody </b>\" just buy a mac. Apple is the best"

@app.route("/everyb")
def everybodyElse():
    return "We like to suffer with <b>windows</b> (aka the love of my life) and love that it is so complicated to code in! (I hope you got the sarcasm)"
app.debug = True
app.run()
