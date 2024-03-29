import os
import pandas as pd

FILEPATH = "feed.csv"

def read_feed(filepath=FILEPATH):
    with open(filepath, 'r') as file_read:
        # maybe should be readlines()?
        feed_local = file_read.read()
    return feed_local

def write_feed(df, filepath=FILEPATH):
    os.remove(FILEPATH)
    df.to_csv(filepath, index=True)

def print_dict_structure(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            print_dict_structure(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(type(value)))

# if __name__ == "__main__":
