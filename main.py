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

           if val > 0:
            while Out < val:
              Out = Sequence[-1] + Sequence[-2]
              if (Out < val):
                Sequence.append(Out)
            return f"The result is: {Sequence}."
           elif val <= 0:
            return f"That is not a valid number"
  
@app.route('/factorial/<int:x>')
           def bit(x):
                      output = 1
                      if x < 0:
                                 return('You must provide a positive number') 
                      else:
                                 while x > 0:
                                            output = output * x
                                            x = x - 1
                                 return(output)
