import urllib2
import goose
from bs4 import BeautifulSoup

def scrapeLink(url):
        
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(url)
    raw_html = response.read()
    g = goose.Goose()
    a = g.extract(raw_html=raw_html)

    soup = BeautifulSoup(raw_html, "lxml")
    metadata = [{a: tag[a] for a in tag.attrs}
                for tag in soup.find_all("meta")]

    result = dict()
    result["content"] = a.cleaned_text
    result["title"] = a.title
    result["url"] = soup.find("link", rel="canonical")["href"]
    result["metadata"] = metadata
    return result
