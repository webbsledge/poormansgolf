import assemblyai as assembly_ai
from functions import *

API_KEY = 'b1ffed0961df4723b22e1652f782b077'
SPEAKER_LABELS = True

def main():
    audio_path = input("Enter the podcast audio path: ")  # audio URL or local path
    assembly_ai.settings.api_key = API_KEY
    config = assembly_ai.TranscriptionConfig(speaker_labels=SPEAKER_LABELS)
    try:
        transcript = transcribe_audio(audio_path, config)
        transcript_formatted = format_transcript(transcript)
        save_transcript(transcript_formatted)
    except Exception as e:
        print(f"An error occurred while transcribing the audio: {e}")


if __name__ == "__main__":
    main()
