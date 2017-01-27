import requests
from urlparse import parse_qsl, urlparse
import json


class FacebookTokenRefresherException(Exception):
    pass


class FacebookTokenRefresher:
    base_url = 'https://graph.facebook.com/oauth/access_token'

    def __init__(self, app_id, app_secret, short_access_token):
        self.app_id = app_id
        self.app_secret = app_secret
        self.short_access_token = short_access_token

    def refresh(self, raise_exception=True):
        params = {
            'grant_type': 'fb_exchange_token',
            'client_id': self.app_id,
            'client_secret': self.app_secret,
            'fb_exchange_token': self.short_access_token
        }

        r = requests.get(self.base_url, params=params)

        if r.status_code == 200:
            return dict(parse_qsl(r.text))
        else:
            if raise_exception:
                raise FacebookTokenRefresherException(json.dumps(r.json(), indent=4))
            else:
                return r.json()