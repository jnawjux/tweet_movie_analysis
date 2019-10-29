# Based on the work of Adil Moujahid (adilmoujahid/Twitter_Analytics)

# Import packages and config
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from config import consumer_key, consumer_secret, access_token, access_token_secret
import datetime
import csv
import sys

# Takes tweets and a designated csv file and writes them to it.


class StdOutListener(StreamListener):

    def on_status(self, status):
        if (status.lang == "en") & (status.user.followers_count >= 1000):
            text_for_output = "'" + status.full_text.replace('\n', ' ') + "'"
            csvw.writerow([status.id,
                           status.user.screen_name,
                           status.created_at.strftime(
                               '%d/%m/%y %I:%M %S %p'),
                           status.user.followers_count,
                           text_for_output])
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
    csvw = csv.writer(open(sys.argv[-1], "a"))
    csvw.writerow(['twitter_id', 'name', 'created_at',
                   'followers_count', 'text'])
    stream.filter(track=['jason voorhees', 'freddie krueger', 'michael myers'])
