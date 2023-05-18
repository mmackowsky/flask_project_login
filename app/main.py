from flask import render_template, redirect, url_for, Blueprint, request


login_blueprint = Blueprint("login", __name__)
password_blueprint = Blueprint("password", __name__)
user_blueprint = Blueprint("user", __name__)


@login_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        nickname = request.form['nickname']
        password = request.form['password']
        return redirect(url_for("user.user", nick=nickname, password=password))
    else:
        return render_template("login.html")


@user_blueprint.route('/<nick>')
def user(nick):
    return f"<h1> Hello, {nick} </h1>"

