import feedparser as fp

rss_url = "https://chasingscratch.libsyn.com/rss"
feed = fp.parse(rss_url)

for entry in feed.entries:
    # metadata
    print("Feed Title:", feed.feed.title)
    print("Feed Description:", feed.feed.description)
    print("Feed Link:", feed.feed.link)
    # entries
    print("Entry Title:", entry.title)
    print("Entry Link:", entry.link)
    print("Entry Published Date:", entry.published)
    print("Entry Summary:", entry.summary)
    print("\n")

# get date range
'''
from datetime import datetime, timedelta

# Define the time range (e.g., the last 24 hours)
now = datetime.now()
time_range = timedelta(days=1)
# Iterate through entries and filter by the time range
for entry in feed.entries:
    entry_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
    if now - entry_date <= time_range:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        print("Entry Published Date:", entry.published)
        print("Entry Summary:", entry.summary)
        print("\n")
'''

# do this with pandas instead
'''
import csv

# Prepare the CSV file
with open('rss_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'link', 'published', 'summary']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    # Iterate through entries and write to the CSV file
    for entry in feed.entries:
        writer.writerow({'title': entry.title, 'link': entry.link, 'published': entry.published, 'summary': entry.summary})
'''
