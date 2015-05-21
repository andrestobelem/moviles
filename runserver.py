import os
from flask import Flask, request, Response
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/andrestobelem/Workspace/moviles/in/'
ALLOWED_EXTENSIONS = set(['gpx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
    return "Para ejecutar el servicio de moviles..."

@app.route('/snap', methods=['GET', 'POST'])
def snap():
    if request.method == 'POST':
        aFile = request.files['file']
        if aFile and allowed_file(aFile.filename):
            filename = secure_filename(file.filename)
            aFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


        os.system("cd /home/andrestobelem/Workspace/map-matching/ ; ./map-matching.sh action=match gpx=../moviles/in/moviles.gpx maxSearchMultiplier=150")
        os.system("mv /home/andrestobelem/Workspace/moviles/in/moviles.gpx.res.gpx /home/andrestobelem/Workspace/moviles/out/")
        os.system("rm /home/andrestobelem/Workspace/moviles/in/moviles.gpx.res.gpx")

        with open('/home/andrestobelem/Workspace/moviles/out/moviles.gpx.res.gpx') as f:
            content = f.readlines()

        return Response(content, mimetype='application/xml')

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)