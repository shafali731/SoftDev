from flask import Flask, render_template
from urllib import request
import json
app = Flask(__name__)
# file = ""
# try:
#     file = open('nasa.json', 'x')
# except Exception as e:
#     file = open('nasa.json', 'w')


@app.route("/")
def test():
    thing= request.urlopen("http://api.open-notify.org/iss-now.json")
    readed = thing.read()
    dict = json.loads(readed)
    print(dict)
    longi = dict["iss_position"]["longitude"]
    lati = dict["iss_position"]["latitude"]
    return render_template("home.html", longit = longi, latit= lati)


if __name__ == "__main__":
    app.debug = True
    app.run()
