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


query = twitter.search.tweets(q = "google")


print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])


for result in query["statuses"]:
    print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])
