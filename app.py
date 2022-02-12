import requests as requests
from flask import Flask, render_template, request
app = Flask(__name__)


# GETメソッド、POSTメソッドの追記
@app.route("/set", methods=["GET", "POST"])
def set():
    # if requests.method == "GET":
    return render_template("index.html")

    # if requests.method == "POST":
    # content = "アラームをセットしました。"
    # return render_template("index.html", content=content)


if __name__ == '__main__':
    hostname = "127.0.0.1"
    port = 5000
    app.run(host=hostname, port=port, debug=True)
