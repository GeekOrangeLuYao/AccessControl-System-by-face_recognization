import urllib,urllib2
import json as js
class EyeKey:

    def __init__(self,url,app_id,app_key):
        self.url = url
        self.app_id = app_id
        self.app_key = app_key

    def transGet(self,Mode_str,pic):

        return Mode_str

    def transJson(self,jsontext):
        # may need encoding
        ans = js.loads(jsontext)
        return ans