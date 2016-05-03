AllTweets
_________

To use, simply do::

    >>> from alltweets.twitter_crawler import TwitterCrawler
    >>> crawler = TwitterCrawler(your_key, your_secret)
    >>> tweets = crawler.crawl_user_timeline(screen_name='TwitterAPI')

