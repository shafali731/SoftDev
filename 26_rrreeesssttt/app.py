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
    thing= request.urlopen("https://restcountries.eu/rest/v2/lang/es")
    readed = thing.read()
    dict = json.loads(readed)
    print(dict)
    lenn = len(dict)
    #while (lenn>50):
    nam = dict[0]["name"]
    curr = dict[0]["currencies"][0]["name"]
    #return render_template("index.html", n = nam, c= curr)
    k= request.urlopen("https://dog.ceo/api/breeds/image/random")
    kr = k.read()
    kdict = json.loads(kr)

    q = request.urlopen("https://www.boredapi.com/api/activity")
    qr = q.read()
    qrdict = json.loads(qr)

    
    return render_template("index.html", n = nam, c= curr, pic=kdict["message"], act=qrdict["activity"], p=qrdict["participants"])
    

if __name__ == "__main__":
    app.debug = True
    app.run()
