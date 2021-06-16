#This is to be the main framework for the TwitterHush script/bot.

#You will need to install the following packages if they are not already installed.
import Tweepy

#The following are the Twitter API credentials you would need to get from your Twitter account.  They are keps in a separate folder that is not updated to this repository for obvious security reasons.
from credentials import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Testing.  Just want to make sure I understand how github works. 
