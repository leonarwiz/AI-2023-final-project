from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
# import torch
# from torchvision import transforms
# from your_model_package import StarGAN  # Substitute with actual package

app = Flask(__name__)

# Set where you want the images to be uploaded
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# model = StarGAN()
# model.load_state_dict(torch.load('/path/to/model', map_location=device))
# model.to(device).eval()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        filename = secure_filename(f.filename)
        file_path = os.path.join('static/uploads', filename)  # save to static directory
        f.save(file_path)

        # Return the relative path
        rel_path = os.path.join('uploads', filename)
        return render_template('result.html', image_path=rel_path)
    return render_template('index.html')


# def process_file(file_path):
#     image = Image.open(file_path)
#     transform = transforms.Compose([
#         transforms.ToTensor(),
#         transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))])
#     image = transform(image).unsqueeze(0).to(device)
#     output = model(image)  # Substitute with actual function call
#     # Post-process the image and return the path
#     return post_process(output)
if __name__ == "__main__":
    app.run(port=5000, debug=True)
