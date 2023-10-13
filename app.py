from flask import Flask, request, redirect, url_for, render_template
import os

UPLOAD_FOLDER = '/root/fileserv'  # Replace with your directory path
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webm', 'tar', 'gz'}  # Allowed file types

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return redirect(url_for('index'))
        else:
            return "File type not allowed. Upload failed."
    else:
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8881)  # Replace with your desired host and port
