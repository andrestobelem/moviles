# -*- coding: utf-8 -*-
import os

from flask import Flask, request, Response
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'in')
SERVER_FOLDER = os.path.join(os.path.dirname(__file__), 'out')

MAP_MATCHING_FOLDER = '../map-matching'

ALLOWED_EXTENSIONS = set(['gpx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)


@app.route("/")
def index():
    return "Para ejecutar el servicio para móviles it a /snap-to-road"


@app.route("/snap-to-road", methods=['GET', 'POST'])
def snap_to_road():
    if request.method == 'POST':
        a_file = request.files['file']
        if a_file and allowed_file(a_file.filename):
            filename = secure_filename(a_file.filename)
            a_file.save(os.path.join(UPLOAD_FOLDER, filename))
            os.system("cd " + MAP_MATCHING_FOLDER + " ;" + "./map-matching.sh action=match gpx=../moviles/in/moviles.gpx maxSearchMultiplier=150")
            os.system("mv in/" + filename + ".res.gpx " + SERVER_FOLDER + "/.")
            os.system("rm " + filename)

            with open(SERVER_FOLDER + '/' + filename + '.res.gpx') as f:
                content = f.readlines()

            return Response(content, mimetype='application/xml')

        pass

    return '''
    <!doctype html>
    <title>Subir un archivo gpx</title>
    <h1>Subir un archivo gpx</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Subir>
    </form>
    '''


if __name__ == "__main__":
    app.run(debug=True, port=5050)
