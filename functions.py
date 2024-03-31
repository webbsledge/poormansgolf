import os
import assemblyai as assembly_ai
import feedparser as fp
import pandas as pd

feed_path = "feed.csv"
transcript_path = "transcript.txt"



def get_feed_data(rss_url):
    feed = fp.parse(rss_url)

    titles = []
    dates = []
    links = []

    for entry in feed.entries:
        titles.append(entry.title)
        dates.append(entry.published)
        links.append(entry.link)

    entry_index = list(range(len(titles)))
    titles.reverse()
    dates.reverse()
    links.reverse()

    podcasts = {k: [v1, v2, v3] for k, v1, v2, v3 in zip(entry_index, titles, dates, links)}
    podcasts = pd.DataFrame.from_dict(podcasts)

    return podcasts


def get_link(podcasts, podcast_num):
    return podcasts[podcast_num][2]


def transcribe_audio(audio_path, config):

    transcript_formatted = ''
    transcriber = assembly_ai.Transcriber()
    transcript = transcriber.transcribe(audio_path, config)
    for utterance in transcript.utterances:
        utterance = f"Speaker {utterance.speaker}: {utterance.text}\n"
        transcript_formatted += utterance

    return transcript_formatted


def save_transcript(transcript, filepath=transcript_path):
    os.remove(transcript_path)
    with open(filepath, 'w') as file_write:
        file_write.write(transcript)


def write_feed(df, filepath=feed_path):
    os.remove(feed_path)
    df.to_csv(filepath, index=True)


def print_dict_structure(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            print_dict_structure(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(type(value)))
