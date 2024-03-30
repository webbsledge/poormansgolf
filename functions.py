import os
import assemblyai as assembly_ai

feed_path = "feed.csv"
transcript_path = "transcript.txt"


def transcribe_audio(audio_path, config):
    transcriber = assembly_ai.Transcriber()
    transcript = transcriber.transcribe(audio_path, config)
    return transcript


def format_transcript(transcript):
    transcript_formatted = ''
    for utterance in transcript.utterances:
        utterance = f"Speaker {utterance.speaker}: {utterance.text}\n"
        transcript_formatted += utterance
    return transcript_formatted


def read_feed(filepath=feed_path):
    with open(filepath, 'r') as file_read:
        # maybe should be readlines()?
        feed_local = file_read.read()
    return feed_local


def write_feed(df, filepath=feed_path):
    os.remove(feed_path)
    df.to_csv(filepath, index=True)


def save_transcript(transcript, filepath=transcript_path):
    os.remove(transcript_path)
    with open(filepath, 'w') as file_write:
        file_write.write(transcript)


def print_dict_structure(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            print_dict_structure(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(type(value)))


# if __name__ == "__main__":
