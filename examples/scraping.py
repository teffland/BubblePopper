from __future__ import print_function
import scrape
import httplib
import urllib2

for i, event in enumerate(scrape.scrapeGoogleTopNews(), 1):
    print("{} {}".format(i, event["title"]))
    links = scrape.scrapeGoogleNewsCluster(event["url"])
    for l, link in enumerate(links, 1):
        try:
            article = scrape.scrapeLink(link)
            if article != None:
                print("  {} {} {}".format(
                    l, article["domain"], article["title"]))
        except urllib2.HTTPError, e:
            print("   {} {} {}".format(l, type(e), str(e)))
        except httplib.BadStatusLine, e:
            print("   {} {} {}".format(l, type(e), str(e)))
        except urllib2.URLError, e:
            print("   {} {} {}".format(l, type(e), str(e)))

