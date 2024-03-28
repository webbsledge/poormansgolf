import feedparser as fp

rss_url = "https://chasingscratch.libsyn.com/rss"
feed = fp.parse(rss_url)

for entry in feed.entries:
    print("Entry Title:", entry.title)
    print("Entry Link:", entry.link)
    print("Entry Published Date:", entry.published)
    print("Entry Summary:", entry.summary)
    print("\n")
