# BubblePopper
Poppin' dat filter bubble

### Competitors

* [PolitEcho](http://politecho.org/)
* [Read Across the Aisle](http://www.readacrosstheaisle.com/)
* [

### Goals
* Look at article `<meta>` tags as proxy for the "aspects" of a document
  * Not all have these, but could you heuristically use NER on title to get for others
* Classify or Quantify if article is "opinion-based" or "opinionated"
* Organize articles by their constituent aspects/topics (right now these are Named Entities)

### Components
* Flask server backend
* Chrome extension frontend

### Gameplan of Minimal Product
* Use google news rss feeds to get large streams of articles, indexed by events

* Pick a set of related google news docs
[ ] - Give me an RSS list of article links, and scrape all of the linked articles
[ ] - For each article: Extract article text, aspects, and political leaning
[ ] - Implement chrome extension that scrapes a page for it's article content, aspects, leaning as with RSS aggregator
[ ] - 
