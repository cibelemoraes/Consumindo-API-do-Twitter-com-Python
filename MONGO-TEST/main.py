from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import tweepy

#client = MongoClient("")

#db=client.my_test

#tweets_collection = db.tweets

#tweets_collection.insert_one({"author": "teste", "text": "texto qualquer"})

#tweets = tweets_collection.find({})

#print(list(tweets))

#BRAZIL_WOE_ID =23424768

auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

#auth.set_acess_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

#api = tweepy.API(auth)

#trends = api.trends_place(BRAZIL_WOE_ID)

#for tweet in trends:
#    print(tweet)