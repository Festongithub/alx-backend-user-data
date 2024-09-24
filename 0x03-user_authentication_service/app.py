#!/usr/bin/env python3
"""Basic flask App"""

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def index() -> str:
    """
    Return json
    """
    text = {"message": "Bienvenue"}
    return jsonify(text)


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """"
    Register a new user
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    msg = {"email": email, "message": "user created"}
    return jsonify(msg)


@app.route('/sessions', methods=['POST'])
def log_in() -> str:
    """
    implement login
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    text = {"email": email, "message": "logged in"}
    resp = jsonify(text)

    resp.set_cookie("session_id", session_id)

    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
