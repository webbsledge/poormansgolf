from functions import *

rss_url = "https://chasingscratch.libsyn.com/rss"
API_KEY = 'b1ffed0961df4723b22e1652f782b077'
assembly_ai.settings.api_key = API_KEY
config = assembly_ai.TranscriptionConfig(speaker_labels=True)


def main():
    podcasts = get_feed_data(rss_url)

    print("There are", len(podcasts.T) - 1, "podcasts in this series.")
    podcast_num = int(input("Which podcast do you want to transcribe? Enter number: ")) - 1  # audio URL or local path

    audio_path = get_link(podcasts, podcast_num)

    try:
        transcript = transcribe_audio(audio_path, config)
        save_transcript(transcript)
    except Exception as e:
        print(f"An error occurred while transcribing the audio: {e}")


if __name__ == "__main__":
    main()
