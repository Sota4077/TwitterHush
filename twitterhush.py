from __future__ import unicode_literals

import sys, logging, tweepy

from credentials import * #imports the variabls consumer_key, consumer_secret, access_token & access_token_secret.
logging.warning("Assembling keywords for keyword variable...")

with open('keywords.txt') as f:
    keywords = [line.rstrip() for line in f]
logging.warning(keywords)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



class MyStreamListener(tweepy.StreamListener):
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
    def on_status(self, status):
        print(status.user.screen_name)
        print(status.text)
        print("--------------------------------------")

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)\

myStream.filter(track=keywords, is_async=True)
