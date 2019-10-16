# Based on the work of Adil Moujahid (adilmoujahid/Twitter_Analytics)

# Import packages and config
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from config import consumer_key, consumer_secret, access_token, access_token_secret
import ast


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        data_dict = ast.literal_eval(data)
        if (data_dict["lang"] == "en"):
            print(data_dict["text"])
            # print({"twitter_id": data["id"],
            #        "created_at": data["created_at"],
            #        "user_id": data["user"]["screen_name"],
            #        "followers_count": data["user"]["followers_count"],
            #        "text": data["text"]})
            return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Filter based on movie titles
    stream.filter(track=['joker', 'gemini man', 'addams family',
                         'maleficent', 'zombieland 2', 'jojo rabbit'])
