from flask import Flask, render_template, request
import json
import urllib.request as apirequest, json


app = Flask(__name__)

apikey = "aca389e0"
movie_url = "http://www.omdbapi.com/?t="

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        val = request.form.get("mname")

        conn = apirequest.urlopen(movie_url + val + "&apikey=" + apikey)
        json_data = json.loads(conn.read())

        return render_template("index.html", data=json_data)

    # conn = apirequest.urlopen(movie_url + "hero" + "&apikey=" + apikey)
    # json_data = json.loads(conn.read())
    # return render_template("index.html", data=json_data)
    return render_template("index.html",validation = True, data={"Message" : "boot"})



if __name__ == "__main__":
    app.run(debug = True)