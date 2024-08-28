import os
from flask import Flask, render_template, request, send_file
from compression import compress_pdf

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'

# Create directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    compression_level = request.form.get('compression_level', 'normal')
    output_filename = f"compressed_{file.filename}"
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(DOWNLOAD_FOLDER, output_filename)

    file.save(input_path)
    compress_pdf(input_path, output_path, compression_level)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
