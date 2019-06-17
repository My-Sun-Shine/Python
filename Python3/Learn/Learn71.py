# web框架 flash
from flask import Flask,request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    'http://localhost:5000'
    return '<h1>Home</h1>'


@app.route("/signin", methods=["GET"])
def signin_form():
    'http://localhost:5000/signin'
    return '''<form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>'''


@app.route("/signin", methods=["POST"])
def signin():
    #
    if request.form["username"] == "admin" and request.form["password"] == "password":
        return "<h3>Hello, admin</h3>"
    return "<h3>error</h3>"


if __name__ == "__main__":
    app.run()
