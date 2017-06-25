# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '3184260913-uydgdf878yfb'
ACCESS_SECRET = '1Epl9RJO3e9zkhSfyhud9d8hs7fggbs8gxPxg4JJpfxpSMAe'
CONSUMER_KEY = 'fJiUTHwN98342uedbhje5vJKiADc2'
CONSUMER_SECRET = 'Wj6Gu293udbjhv90udn97x13WUc872i84ybwu6vdZ15zWmx5ByGts0oP6kTW'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth=oauth)


user = "jacob2588m"

#-----------------------------------------------------------------------
# query the user timeline.
# twitter API docs:
# https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
results = twitter.statuses.user_timeline(screen_name = user)

#-----------------------------------------------------------------------
# loop through each status item, and print its content.
#-----------------------------------------------------------------------
for status in results:
    print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))
