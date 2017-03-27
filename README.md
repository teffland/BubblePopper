# BubblePopper
Poppin' dat filter bubble

## References
### Related Projects

* [PolitEcho](http://politecho.org/) - Shows you the political leanings of your facebook friends compared to you, as measured by the polarity of content in feeds
* [Read Across the Aisle](http://www.readacrosstheaisle.com/) - App that rates sources on spectrum and encourages reading across this spectrum
* [Electome](http://socialmachines.media.mit.edu/projects/)
* [Read Outside Your Bubble - BuzzFeed](https://www.buzzfeed.com/bensmith/helping-you-see-outside-your-bubble?utm_term=.hqZbMxL4E#.sy65N8wKe) - Pilot extension for buzz feed that shows you social media comments that have opposing views
* [Escape Your Bubble](https://www.escapeyourbubble.com/) - Extension that inserts manually procurred content from opposite political party to help expand your views

### Visualization of Text
* [ConVis](https://www.cs.ubc.ca/~enamul/papers/ConVis_EuroVis2014.pdf) - System to visualize and explore opinions and topics in blog comments. Good visualization principle and list of user requirements.
### Articles (among other things) of Interest

* [How Facebook Feed Algo Works(ish)](http://www.slate.com/articles/technology/cover_story/2016/01/how_facebook_s_news_feed_algorithm_works.html)
* [NYTimes "How to Escape Your Filter Bubble"](http://www.slate.com/articles/technology/cover_story/2016/01/how_facebook_s_news_feed_algorithm_works.html)
* [Twitter](http://www.slate.com/articles/technology/cover_story/2017/03/twitter_s_timeline_algorithm_and_its_effect_on_us_explained.html) now has a feed-filtering algorithm to improve user retention (aka up click-through via drama and baiting.)
* [OG TED talk](https://www.ted.com/talks/eli_pariser_beware_online_filter_bubbles)
* [This guy](https://users.ics.aalto.fi/kiran/) has done a lot of applicable/related research

### Goals

* Look at article `<meta>` tags as proxy for the "aspects" of a document
  * Not all have these, but could you heuristically use NER on title to get for others
* Classify or Quantify if article is "opinion-based" or "opinionated"
* Organize articles by their constituent aspects/topics (right now these are Named Entities)

### Components
* Flask server backend to do heavy scraping, storage
* Chrome extension frontend to visualize analysis results with one click

### Gameplan of Minimal Product
* Use google news rss feeds to get large streams of articles, indexed by events
* Pick a set of related google news docs to work with
* [X] - Give me an RSS list of article links, and scrape all of the linked articles
* [ ] - For each article: Extract article text, aspects, and political leaning
* [X] - Implement chrome extension that scrapes a page for it's article content, aspects, leaning as with RSS aggregator
* [ ] - Simple Comparator: Use meta tags like "keywords" and "article:tag" to serve as proxy aspects. Return nearest neighbors based on Jaccard sim of tags.

### Examples
* See examples/scraping.py to see an example of how to retrieve articles from google news.

### Installation
* Dependencies: pip install goose-extractor beautifulsoup4 pyyaml
* Set `PYTHONPATH=$PYTHONPATH:path-to-src-directory`

#### Mac OSX
**System Dependencies:**
* OpenSSL
* python 2.7.6

* To install python packages, it is suggested you use [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), then use command
```bash
    pip install -r requirements.txt
```


