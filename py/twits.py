$ pip install tweepy
-
import tweepy

auth = tweepy.OAuthHandler("YOU_CONSUMER_KEY", "YOUR_CONSUMER_SECRET")
auth.set_access_token("YOUR_ACCESS_TOKEN", "YOUR_ACCESS_SECRET")
api = tweepy.API(auth)

# Tweet something
tweet = api.update_status("My first tweet!")

# Like the tweet you just made
api.create_favorite(tweet.id)
