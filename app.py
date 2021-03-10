import os
from flask import Flask, render_template, url_for, request, redirect, send_from_directory, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
# TODO change extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# @app.route('/', methods=['POST', 'GET'])
# def index():
#    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print(request.url, request.method, request.files)

    if request.method == 'POST':
        # check if the post request has the file part
        if 'filename' not in request.files:
            return render_template('index.html', description="Fail on tühi")
        file = request.files['filename']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return render_template('index.html', description="Unustasid faili valida")
        if file and allowed_file(file.filename):
            # print(file.read().decode("utf8"))
            # For saving file
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # TODO create description
            description = "Siia tuleb muusikafaili kirjeldus" + "\nÜles laetud fail: " + file.filename
            return render_template('index.html', description=description)

    return render_template('index.html', description="Lae üles fail kui kirjeldust soovid")


# If file is being save locally
# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
