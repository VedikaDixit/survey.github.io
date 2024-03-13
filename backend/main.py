from flask import Flask, render_template, jsonify as json, request as req
from controlleres import getquesfir,getnext

app = Flask(__name__)

@app.route("/",methods=['GET'])
def loadHome():
    return render_template("homepage.html")

from flask import request

@app.route("/getques1", methods=['GET'])
def getres():
        return getquesfir(),200
@app.route('/nextques',methods=["POST"])
def nextq():
    data=req.json
    return getnext(data)
    
if __name__=="__main__":
    app.run(debug=True)