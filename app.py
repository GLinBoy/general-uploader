import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import netifaces
from flask_qrcode import QRcode


app=Flask(__name__)
port = 5000
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 * 1024
QRcode(app)

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    ipAddr = netifaces.ifaddresses(netifaces.gateways()['default'][netifaces.AF_INET][1])[netifaces.AF_INET][0]['addr']
    return render_template('upload.html', address = 'http://{}:{}'.format(ipAddr, port))


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file :
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=port,debug=False,threaded=True)
