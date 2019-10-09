
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>你好, 帅哥<h1>"


@app.route("/login", methods=["POST"])
def login():
    print(request.form.items())
    print(request.form)
    for k, v in request.form.items():
        print(k, "----", v)
    username = request.form.get("username", "")
    return "<h1>你好, %s!!<h1>" % username


@app.route("/loginget", methods=["GET"])
def loginget():
    for k, v in request.args.items():
        print(k, "----", v)
    username = request.args.get("username", "")
    return "<h1>你好, %s!<h1>" % username


if __name__ == "__main__":
    app.run(host="0.0.0.0")
