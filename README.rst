AllTweets
_________


To crawl entire timeline of a user, simply do::


.. highlight:: python

.. code-block:: python

   from alltweets.crawler import TwitterCrawler
   crawler = TwitterCrawler(your_key, your_secret)
   tweets = crawler.crawl_user_timeline(screen_name='TwitterAPI')

