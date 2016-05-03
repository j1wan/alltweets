import requests.auth
import base64
from .constants import *


class TwitterAppOnlyAuth(requests.auth.AuthBase):
    """ https://dev.twitter.com/oauth/application-only """
    def __init__(self, consumer_key, consumer_secret):
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_token = self._get_access_token()

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer %s' % self._access_token
        return r

    def _get_access_token(self):
        url = 'https://api.twitter.com/oauth2/token'
        credentials = '%s:%s' % (self._consumer_key, self._consumer_secret)
        base64_credentials = base64.b64encode(bytearray(credentials, 'utf-8'))

        headers = {
            'Authorization': 'Basic ' + base64_credentials.decode('utf-8'),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'User-Agent': USER_AGENT
        }

        params = {
            'grant_type': 'client_credentials'
        }

        try:
            response = requests.post(url, headers=headers, params=params)
            payload = response.json()
            return payload['access_token']
        except Exception as e:
            # TODO
            raise Exception(e)
