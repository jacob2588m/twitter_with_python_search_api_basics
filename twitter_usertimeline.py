# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '3184260913-HaT479oiz84a3fxyLRn8naPdIkr6jXPhmHZxYez'
ACCESS_SECRET = '1Epl9RJO3e9zkhSfyhu7hHkyHWGb8gxPxg4JJpfxpSMAe'
CONSUMER_KEY = 'fJiUTHwNnY94Ct3w5vJKiADc2'
CONSUMER_SECRET = 'Wj6GuAzmn023hc97x13WUc87cjsUk6Z15zWmx5ByGts0oP6kTW'

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
