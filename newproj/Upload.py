import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
uploads_dir = os.path.join(app.instance_path, 'uploads')
try:
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)
except OSError as error:
    print("Directory error: '%s' can not be created" % error)


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST', 'GET'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(uploads_dir, filename))
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)
