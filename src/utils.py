def load_audio_file(file_path):
    # Function to load an audio file
    import librosa
    audio, sample_rate = librosa.load(file_path, sr=None)
    return audio, sample_rate

def format_transcription(transcription):
    # Function to format the transcribed text
    return transcription.strip()