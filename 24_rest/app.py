from flask import Flask, render_template
import urllib, json
app = Flask(__name__)
# file = ""
# try:
#     file = open('nasa.json', 'x')
# except Exception as e:
#     file = open('nasa.json', 'w')


@app.route("/")
def test():
    thing= urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=tvuHZFwe2VP5f86ZBC8qvdYfWoXG7mx0WMII9t4B")
    readed = thing.read()
    dict = json.loads(readed)
    print(dict)
    img_url = dict["url"]
    expl = dict["explanation"]
    return render_template("home.html", url = img_url, explain= expl)


if __name__ == "__main__":
    app.debug = True
    app.run()
