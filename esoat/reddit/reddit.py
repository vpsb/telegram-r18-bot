import requests

from .. import constants


class Reddit:
    def __init__(self):
        self._http = requests.Session()
        self._http.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
    
    def _listing(self, type, sub, **params):
        url = f"{constants.REDDIT_API_URL}/r/{sub}/{type}"
        resp = self._http.get(url, params=params)
        return resp.json()

    def top(self, sub: str, t: str = "day", limit: int = 5):
        return self._listing("top", sub, t = t, limit = limit)
    
    def controversial(self, sub: str, limit: int = 5):
        return self._listing("controversial", sub, limit = limit)
    
    def best(self, sub: str, limit: int = 5):
        return self._listing("best", sub, limit = limit)
    
    def hot(self, sub: str, limit: int = 5):
        return self._listing("top", sub, limit = limit)
    
    def new(self, sub: str, limit: int = 5):
        return self._listing("top", sub, limit = limit)
    
    def rising(self, sub: str, limit: int = 5):
        return self._listing("rising", sub, limit = limit)
    
    def random(self, sub):
        return self._listing("random", sub)