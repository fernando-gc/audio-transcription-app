from flask import Flask, request, jsonify
from transcriber import Transcriber

app = Flask(__name__)
transcriber = Transcriber()

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio_file' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio_file']
    transcription = transcriber.transcribe_audio(audio_file)

    return jsonify({'transcription': transcription})

if __name__ == '__main__':
    app.run(debug=True)