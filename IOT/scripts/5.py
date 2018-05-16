import feedparser
def parseRSS( rss_url ):
    return feedparser.parse( rss_url )

def getHeadlines( rss_url ):
    headlines = []

    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])

    return headlines


allheadlines = []

newsurls = {
    'apnews':           'http://hosted2.ap.org/atom/APDEFAULT/3d281c11a76b4ad082fe88aa0db04909',
    'googlenews':       'http://news.google.com/?output=rss',
    'yahoonews':        'http://news.yahoo.com/rss/'
}

for key,url in newsurls.items():
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend( getHeadlines( url ) )


for hl in allheadlines:
    print("\n")
    print(hl)
