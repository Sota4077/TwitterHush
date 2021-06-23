#Update the credentials_template.py file.  First, rename it to just credentials.py.  Then input your Twitter API keys for each variable.
#Also you will need to install the Tweepy package in the cmd/terminal with "pip install tweepy"

from __future__ import unicode_literals
import logging, tweepy

from credentials import * #imports the variabls consumer_key, consumer_secret, access_token & access_token_secret.
print("Assembling keywords for keyword variable...")

with open('keywords.txt') as f:
    keywords = [line.rstrip() for line in f]
print(keywords)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
    def on_status(self, status):
        if not status.truncated:
            text = status.text
            print('@'+status.user.screen_name+'\n')
            print(text+'\n')
            print('twitter.com/anyuser/status/'+status.id_str)
        else:
            text = status.extended_tweet['full_text']
            print('@'+status.user.screen_name+'\n')
            print(text+'\n')
            print('twitter.com/anyuser/status/'+status.id_str)
        print("--------------------------------------")

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)\

myStream.filter(track=keywords, is_async=True)
