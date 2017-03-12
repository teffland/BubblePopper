import urllib2
import goose
from bs4 import BeautifulSoup
from urlparse import urlparse

def scrapeLink(url):
        
    ua = "Mozilla/5.0"
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    opener.addheaders = [('User-Agent', ua)]
    response = opener.open(url)
    raw_html = response.read()
    g = goose.Goose()
    try:
        a = g.extract(raw_html=raw_html)
        if a.cleaned_text == '': return None

        soup = BeautifulSoup(raw_html, "lxml")
        metadata = [{a: tag[a] for a in tag.attrs}
                    for tag in soup.find_all("meta")]

        parsed_uri = urlparse(url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)

        result = dict()
        result["content"] = a.cleaned_text
        result["title"] = a.title
        result["domain"] = domain
        cl = soup.find("link", rel="canonical")
        if cl != None:
            result["url"] = cl["href"]
        else:
            result["url"] = url
        result["metadata"] = metadata
        return result
    except RuntimeError, e:
        # soup sometimes hits recursion depth because recursion is bad.
        return None
    except IndexError, e:
        # goose sometimes returns index error when trying to get the title!?
        return None

def scrapeGoogleTopNews():
    try:
        # Python 2.6-2.7 
        from HTMLParser import HTMLParser
    except ImportError:
        # Python 3
        from html.parser import HTMLParser
    h = HTMLParser()
    ua = "Firefox/48.0"
    gnews_url = "https://news.google.com/?output=rss"

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    opener.addheaders = [('User-Agent', ua)]
    response = opener.open(gnews_url)

    raw_html = response.read()
    raw_html_u = h.unescape(raw_html.decode("utf8"))
    soup = BeautifulSoup(raw_html_u, "lxml")

    events = list()
    for item in soup.find_all("item"):
        title = item.find("title").getText()

        for a in item.find_all("a"):
            if a["href"].startswith("http://news.google.com/news/more"):
                  
                events.append({"title": title, "url": a["href"]})
    return events

def scrapeGoogleNewsCluster(url):

    ua = "Firefox/48.0"
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    opener.addheaders = [('User-Agent', ua)]

    found_urls = list()
    start = 0
    while start < 10000:

        response = opener.open(url + "&start={}".format(start))
        found_on_page = 0
        raw_html = response.read()
        
        soup = BeautifulSoup(raw_html, "lxml")
        for item in soup.find_all("div"):
            if "class" in item.attrs:
                if "story" in item.attrs["class"]:
                    for a in item.find_all("a"):
                        story_url = a.attrs["href"]
                        found_urls.append(story_url)
                        found_on_page += 1
                        break
        if found_on_page == 0: break
        start += 30
    return found_urls
