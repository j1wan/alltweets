from .oauth import TwitterAppOnlyAuth
import requests

app_only_api = {
    'GET statuses/user_timeline',
    # 'GET statuses/retweets/:id',
    # 'GET statuses/show/:id',
    'GET statuses/retweeters/ids',
    'GET statuses/lookup',

    'GET search/tweets',

    'GET friends/ids',
    'GET followers/ids',
    'GET friendships/show',
    'GET friends/list',
    'GET followers/list',

    'GET users/lookup',
    'GET users/show',
    # 'GET users/suggestions/:slug',
    'GET users/suggestions',
    # 'GET users/suggestions/:slug/members',

    'GET favorites/list',

    'GET lists/list',
    'GET lists/statuses', # !!!
    'GET lists/memberships',
    'GET lists/subscribers',
    'GET lists/subscribers/show',
    'GET lists/members/show',
    'GET lists/members',
    'GET lists/show',
    'GET lists/subscriptions',
    'GET lists/ownerships'

    'GET trends/place',
    'GET trends/available',
    'GET trends/closest',

    'GET application/rate_limit_status',

    'GET help/configuration',
    'GET help/languages',
    'GET help/privacy',
    'GET help/tos',
}



class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret):
        """
        AllTweet crawler only uses application-only authentication.
        The crawler needs your CONSUMER KEY and SECRET.
        If you do not have them, you can get them from "https://apps.twitter.com/".
        """
        self.auth = TwitterAppOnlyAuth(consumer_key, consumer_secret)

    def request(self, api, **kwargs):
        if api not in app_only_api:
            raise Exception

        method, endpoint = api.split()
        session = requests.Session()
        session.auth = self.auth
        url = 'https://api.twitter.com/1.1/%s.json' % endpoint

        try:
            r = session.request(method, url, params=kwargs)
            return r.json()
        except Exception as e:
            raise Exception('Error requesting %s: %s' % (endpoint ,e))
