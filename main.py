from flask import Flask, jsonify, Response
import requests
import hashlib

app = Flask(__name__)

@app.route('/md5/<str:talk>')
           def info(talk):
            result = hashlib.md5(talk.encode())
            final = result.hexdigest()
           return f"The hexadecimal equivalent of hash is: {final}"

@app.route('/fibonacci/<int:val>')
           def term(val):
           Out = 0
           Sequence = [0,1]

