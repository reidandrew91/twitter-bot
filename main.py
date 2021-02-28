#TWITTER BOT
import tweepy
import time
from keep_alive import keep_alive

auth = tweepy.OAuthHandler('AUTH HANDLER!')
auth.set_access_token('API!','KEY!')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
search = 'Bitcoin'
nrTweets = 500

keep_alive()

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('RETWEETED')
        tweet.retweet()
        time.sleep(300)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
