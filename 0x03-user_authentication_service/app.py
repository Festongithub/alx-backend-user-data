#!/usr/bin/env python3
"""Basic flask App"""
from flask import Flask, jsonify, request, abort, redirect

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """
    Return json
    """
    text = {"message": "Bienvenue"}
    return jsonify(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
