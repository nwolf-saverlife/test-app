#!/usr/bin/env python
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    all_env_vars = ""
    for var in os.environ:
        all_env_vars += f"\n{var}={os.environ[var]}<br>\n"
    return "<p>Hello, World!</p>\n" + all_env_vars

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
