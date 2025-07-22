class Transcriber:
    def __init__(self, recognizer, audio_file_path):
        self.recognizer = recognizer
        self.audio_file_path = audio_file_path

    def transcribe_audio(self):
        with open(self.audio_file_path, 'rb') as audio_file:
            audio_data = self.recognizer.record(audio_file)
            try:
                transcription = self.recognizer.recognize_google(audio_data)
                return transcription
            except Exception as e:
                print(f"Error during transcription: {e}")
                return None

    def save_transcription(self, transcription, output_file_path):
        with open(output_file_path, 'w') as output_file:
            output_file.write(transcription)