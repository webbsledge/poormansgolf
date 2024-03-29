import functions
import assemblyai as aai

aai.settings.api_key = 'b1ffed0961df4723b22e1652f782b077'

config = aai.TranscriptionConfig(speaker_labels=True)

# audio URL or local path
audio_path = ""

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_path, config)

# check if transcription error
if transcript.error:
    print(transcript.error)

# print transcription
print(transcript.text)
