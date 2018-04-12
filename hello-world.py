"""
Forked from https://github.com/katiebinley/hello-world

A simple fork which added Tweepy functionality
to Tweet the contents of README.md when run.

Don't forget to modify keys.py and add the API keys or
the program won't run!

To use do:

python hello-world.py  

12/04/2018 
by
R4inBird
"""

# Import The Tweepy Twitter API wrapper
from tweepy import OAuthHandler, API
# Best practice is to keep credentials in a seperarte file
from keys import keys

# Load API credentials into variables
screen_name = keys['screen_name']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']
consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']

# Setup the OAuth handler
auth_handler = OAuthHandler(consumer_key, consumer_secret)
auth_handler.set_access_token(access_token, access_token_secret)

# Create an API instance called api
api = API(auth_handler)

# Read the text in README.md and Tweet it using the Tweepy API
with open('README.md','r') as f:
   api.update_status(f.read())

# Now go and check your timeline and your Hello World Tweet will appear!
print "Done! Check your timeline to see your hello-world tweet!"