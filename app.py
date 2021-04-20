import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import netifaces
from flask_qrcode import QRcode
import click


app=Flask(__name__)
port_number = 5000
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
    return render_template('upload.html', address = 'http://{}:{}'.format(ipAddr, port_number))


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

@click.command()
@click.option('--host', '-h', default='0.0.0.0', help='The interface to bind to.')
@click.option('--port', '-p', default=5000, help='The port to bind to.')
@click.option('--debug', '-d', default=False, is_flag=True, help='show a debugger in case an exception happened')
@click.option('--dev', default=False, is_flag=True, help='show a debugger in case an exception happened')
def cli(host, port, debug, dev):
    global port_number
    port_number = port
    if(dev):
        app.run(host=host,port=port,debug=debug)
    else:
        app.run(host=host,port=port,debug=debug)
