from flask import Flask, request, jsonify
from utils import generate_summary, generate_headline, extract_skills, generate_linkedin_about
import werkzeug

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status': 'InstaResume API Running'})

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded (use multipart/form-data with key "file")'}), 400
    file = request.files.get('file')
    try:
        raw = file.read()
        # attempt to decode as text; for PDFs this will be binary garbage but still returned as text
        text = raw.decode('utf-8', errors='ignore')
    except Exception as e:
        text = ''
    return jsonify({'extracted_text': text})

@app.route('/summary', methods=['POST'])
def summary():
    data = request.get_json(force=True)
    text = data.get('text', '')
    return jsonify({'summary': generate_summary(text)})

@app.route('/headline', methods=['POST'])
def headline():
    data = request.get_json(force=True)
    text = data.get('text', '')
    return jsonify({'headline': generate_headline(text)})

@app.route('/skills', methods=['POST'])
def skills():
    data = request.get_json(force=True)
    text = data.get('text', '')
    return jsonify({'skills': extract_skills(text)})

@app.route('/linkedin', methods=['POST'])
def linkedin_about():
    data = request.get_json(force=True)
    text = data.get('text', '')
    return jsonify({'linkedin_about': generate_linkedin_about(text)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
