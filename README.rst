AllTweets
_________

To crawl entire timeline of a user, simply do::

.. code-block:: python
.. from alltweets.crawler import TwitterCrawler :: python
    >>> crawler = TwitterCrawler(your_key, your_secret) :: python
    >>> tweets = crawler.crawl_user_timeline(screen_name='TwitterAPI')

