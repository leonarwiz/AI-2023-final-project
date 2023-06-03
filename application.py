from flask import Flask, render_template, request
# import your stargan_model.py or similar file here

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get the form data
    expression = request.form.get('expression')
    hair_style = request.form.get('hair_style')
    hair_color = request.form.get('hair_color')

    # Get the image file
    image = request.files.get('file')

    # You would call your StarGAN functions here to process the image
    # result = stargan_model.change_hair_color_and_style(image, expression, hair_style, hair_color)

    # For now, just return the form data as a string
    return render_template('index.html', img_file=image)

if __name__ == '__main__':
    app.run(debug=True)