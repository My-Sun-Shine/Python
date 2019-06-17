# web框架 flash 模板 需要安装jinja2模板
# 在该模板时，{{name}}表示一个可以替换的变量，{% %}表示指令
from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    'http://localhost:5000'
    return render_template("Home.html")


@app.route("/signin", methods=["GET"])
def signin_form():
    'http://localhost:5000/signin'
    return render_template("form.html")


@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    if username == "admin" and request.form["password"] == "password":
        return render_template("signin-ok.html", username=username)
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == "__main__":
    app.run()
