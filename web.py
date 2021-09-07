import os
from flask import Flask, render_template, send_from_directory

facedir = os.path.abspath('FaceDetect')
app = Flask(__name__, template_folder=facedir)


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/<path:path>")
def server_static(path):
    return send_from_directory("FaceDetect", path)

def startapp():
    app.run(debug=False)
