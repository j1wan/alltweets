import requests
from .oauth import TwitterAppOnlyAuth


class TwitterCrawler:
    def __init__(self, consumer_key, consumer_secret):
        """
        AllTweet crawler only uses application-only authentication.
        The crawler needs your CONSUMER KEY and SECRET.
        If you do not have them, you can get them from "https://apps.twitter.com/".
        """
        self.auth = TwitterAppOnlyAuth(consumer_key, consumer_secret)

    def get_user_timeline(self, **kwargs) -> list:
        """
        https://dev.twitter.com/rest/reference/get/statuses/user_timeline

        :param kwargs:
        :return:
        """
        session = requests.Session()
        session.auth = self.auth
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        try:
            r = session.request('GET', url, params=kwargs)
        except Exception as e:
            raise Exception('Error requesting GET statuses / user_timeline: %s' % e)
        return r.json()


    def all_user_timeline(self, **kwargs) -> list:
        if 'user_id' in kwargs == 'screen_name' in kwargs:
            raise Exception('EEE')

        kwargs['count'] = 200  # maximum tweets per distinct request

        tweets = []
        while True:
            batch = self.get_user_timeline(**kwargs)
            if not batch:
                break
            tweets.extend(batch)
            kwargs['max_id'] = batch[-1]['id'] - 1
        return tweets


    def friends_ids(self, **kwargs) -> list:
        session = requests.Session()
        session.auth = self.auth
        url = 'https://api.twitter.com/1.1/friends/ids.json'

        try:
            r = session.request('GET', url, params=kwargs)
        except Exception as e:
            raise Exception('friends/ids api' + e)
        return r.json()


    def follower_ids(self, **kwargs) -> list:
        session = requests.Session()
        session.auth = self.auth
        url = 'https://api.twitter.com/1.1/followers/ids.json'

        try:
            r = session.request('GET', url, params=kwargs)
        except Exception as e:
            raise Exception('friends/ids api' + e)
        return r.json()


    def crawl_friends_ids(self, **kwargs) -> list:
        kwargs['cursor'] = -1
        kwargs['count'] = 5000
        friends = []

        while True:
            batch = self.friends_ids(**kwargs)
            if not batch['ids']:
                break
            friends.extend(batch['ids'])
            kwargs['cursor'] = batch['next_cursor']

        return friends

    def crawl_follower_ids(self, **kwargs) -> list:
        """

        :param kwargs:
        :return:
        """
        kwargs['cursor'] = -1
        kwargs['count'] = 5000
        followers = []

        while True:
            batch = self.follower_ids(**kwargs)
            if not batch['ids']:
                break
            followers.extend(batch['ids'])
            kwargs['cursor'] = batch['next_cursor']

        return followers


