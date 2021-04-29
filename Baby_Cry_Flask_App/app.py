from flask import Flask, render_template, request
import os
#from baby_cry_detection.prediction_simulation import prediction_simulation
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods = ['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'files/')

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        destination = "/".join([target, "temp.mp3"])
        file.save(destination)
        myfile=open('./output/prediction/prediction.txt')
        mytxt=myfile.read()
    return mytxt


if __name__ == "__main__":
    app.run(debug=True)