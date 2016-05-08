from .api import TwitterAPI


class TwitterCrawler(TwitterAPI):
    def crawl_user_timeline(self, **kwargs) -> list:
        if 'user_id' in kwargs == 'screen_name' in kwargs:
            raise Exception('EEE')
        kwargs['count'] = 200  # maximum tweets per distinct request
        tweets = []
        while True:
            batch = self.request('GET statuses/user_timeline', **kwargs)
            if not batch:
                break
            tweets.extend(batch)
            kwargs['max_id'] = batch[-1]['id'] - 1
        return tweets

    def crawl_friends_ids(self, **kwargs) -> list:
        kwargs['cursor'] = -1
        kwargs['count'] = 5000
        friends = []
        while True:
            batch = self.request('GET friends/ids', **kwargs)
            if not batch['ids']:
                break
            friends.extend(batch['ids'])
            kwargs['cursor'] = batch['next_cursor']
        return friends

    def crawl_followers_ids(self, **kwargs) -> list:
        kwargs['cursor'] = -1
        kwargs['count'] = 5000
        followers = []
        while True:
            batch = self.request('GET followers/ids', **kwargs)
            if not batch['ids']:
                break
            followers.extend(batch['ids'])
            kwargs['cursor'] = batch['next_cursor']
        return followers

