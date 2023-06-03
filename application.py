from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import torch
from stargan_model import StarGAN  # assuming StarGAN model is defined in stargan_model.py

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'  # directory to save uploaded files
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Check if the file is one of the allowed types/extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# Load StarGAN model (replace with actual path to trained model)
model = StarGAN()
model.load_state_dict(torch.load('path_to_model/model.pth'))
model.eval()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        hair_color = request.form.get('hairColor')
        hair_style = request.form.get('hairStyle')
        # if user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Process the image with StarGAN
            processed_image = model.process(file_path, hair_color, hair_style)
            processed_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_' + filename)
            processed_image.save(processed_image_path)
            
            return render_template('result.html', filename='processed_' + filename)
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
