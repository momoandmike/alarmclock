from flask import Flask, render_template, request

from main2 import sound, set_alarm

app = Flask(__name__)


# GETメソッド、POSTメソッドの追記
@app.route("/set", methods=["GET", "POST"])
def set():
    # if requests.method == "GET":
    return render_template("index.html")


@app.route("/alarm", methods=["GET"])
def alarm():
    # if requests.method == "GET":
    return render_template("alarm.html")


@app.route("/receive_post", methods=["post"])
def receive_post():
    t = request.form["time"]
    set_alarm(t)
    return t + 'にアラームをセットしました。'

    # if requests.method == "POST":
    # content = "アラームをセットしました。"
    # return render_template("index.html", content=content)


if __name__ == '__main__':
    hostname = "127.0.0.1"
    port = 5000
    app.run(host=hostname, port=port, debug=True)
