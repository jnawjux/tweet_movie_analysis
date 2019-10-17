# Based on the work of Adil Moujahid (adilmoujahid/Twitter_Analytics)

# Import packages and config
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from config import consumer_key, consumer_secret, access_token, access_token_secret
import ast


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_status(self, status):
        if (status.lang == "en") & (status.user.followers_count >= 1000):
            print({"twitter_id": status.id,
                   "name": status.user.screen_name,
                   "created_at": status.user.created_at,
                   "followers_count": status.user.followers_count,
                   "text": status.text})
            return True

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Filter based on movie titles
    stream.filter(track=['joker', 'gemini man', 'addams family',
                         'maleficent', 'zombieland 2', 'jojo rabbit'])
