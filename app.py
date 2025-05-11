from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': '파일이 업로드되지 않았습니다.'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '선택된 파일이 없습니다.'}), 400
    
    # 임시로 성공 메시지만 반환
    return jsonify({
        'message': '파일이 성공적으로 업로드되었습니다.',
        'filename': file.filename
    })

if __name__ == '__main__':
    app.run(debug=True)