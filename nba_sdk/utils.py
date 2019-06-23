import random
from functools import wraps

from nba_sdk.headers import HEADERS


def namedtuple_to_dict(nt):
    return nt._asdict()


def namedtuple_name(nt):
    return type(nt).__name__


def build_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        request_entity = func(self, *args, **kwargs)
        r = {"url": "{base_url}/{path}".format(base_url=self._base_url, path=namedtuple_name(request_entity).lower()),
             "params": namedtuple_to_dict(request_entity), "headers": random.choice(HEADERS)}
        return r
    return wrapper
