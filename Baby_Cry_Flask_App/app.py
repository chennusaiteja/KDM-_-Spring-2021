#importing required libraries
from flask import Flask, render_template, request
import os
from subprocess import call
#python class for calling the python script
class CallPy(object):
    def  __init__(self, path='./baby-cry/baby_cry_detection/prediction_simulation/prediction_simulation.py'):
        self.path=path
    
    def call_prediction_method(self):
        call(["Python", "{}".format(self.path)])
#app naming and filing
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#default path to app
@app.route("/")
def index():
    return render_template("index.html")
#path that will be reloaded after a file upload
@app.route("/upload", methods = ['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'files/')

    if not os.path.isdir(target):
        os.mkdir(target)
#a loop to save the file to the target folder and load it to the predictor script and run it
    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, "temp.mp3"])
        file.save(destination)
        c= CallPy()
        c.call_prediction_method()
        myfile=open('./output/prediction/prediction.txt')
        mytxt=myfile.read()
    return mytxt

#running our flask app
if __name__ == "__main__":
    app.run(debug=True)