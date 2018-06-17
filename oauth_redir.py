from functools import wraps
import json
import os

from flask import Flask, jsonify, request, abort, redirect
import requests

app = Flask(__name__)

@app.route('/')
def root():
    return redirect("http://auth.%s/auth/pebble/complete?%s" % (os.environ['DOMAIN_ROOT'], request.query_string.decode('ascii'), ))

app.run("0.0.0.0", 60000, debug=True)