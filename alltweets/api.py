from .oauth import TwitterAppOnlyAuth
from .constants import *
import requests


class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret):
        """
        AllTweet crawler only uses application-only authentication.
        The crawler needs your CONSUMER KEY and SECRET.
        If you do not have them, you can get them from "https://apps.twitter.com/".
        """
        self.auth = TwitterAppOnlyAuth(consumer_key, consumer_secret)

    def request(self, api, **kwargs):
        if api not in APP_ONLY_APIS:
            raise Exception

        method, endpoint = api.split()
        session = requests.Session()
        session.auth = self.auth
        url = 'https://api.twitter.com/1.1/%s.json' % endpoint

        try:
            if method == 'GET':
                r = session.request(method, url, params=kwargs)
                return r.json()
            elif method == 'POST':
                r = session.request(method, url, data=kwargs)
                return r.json()
        except Exception as e:
            raise Exception('Error requesting %s: %s' % (endpoint ,e))
