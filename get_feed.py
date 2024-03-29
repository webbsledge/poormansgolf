from functions import *
import feedparser as fp
import pandas as pd


rss_url = "https://chasingscratch.libsyn.com/rss"
feed = fp.parse(rss_url)

# print feed structure
# print_dict_structure(feed)

titles = []
dates = []
links = []
keys = ['index', 'title', 'date', 'link']

for entry in feed.entries:
      titles.append(entry.title)
      dates.append(entry.published)
      links.append(entry.link)

entry_index = list(range(len(titles)))
titles.reverse()
dates.reverse()
links.reverse()

podcasts = {k: [v1, v2, v3] for k, v1, v2, v3 in zip(entry_index, titles, dates, links)}

print(podcasts)

