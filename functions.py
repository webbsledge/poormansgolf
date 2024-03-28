import os
FILEPATH = "feed.txt"

def read_feed(filepath=FILEPATH):
    with open(filepath, 'r') as file_read:
        # maybe should be readlines()?
        feed_local = file_read.read()
    return feed_local

def write_feed(entry, filepath=FILEPATH):
    os.remove(FILEPATH)
    with open(filepath, 'w') as file_write:
        file_write.write(entry)
