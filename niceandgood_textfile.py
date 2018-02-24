import tweepy
import random
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

adjectives_file = open('adjectives.txt', 'r')
nouns_file = open('nouns.txt', 'r')
adverbs_file = open('adverbs.txt', 'r')
verbs_file = open('verbs.txt', 'r')


adjectives_lines = adjectives_file.readlines()
nouns_lines = nouns_file.readlines()
adverbs_lines = adverbs_file.readlines()
verbs_lines = verbs_file.readlines()



def niceandgood():
	for i in range(5):
		rand = random.randint(1, 2)
		if (rand == 1):
	 		a = random.choice(adjectives_lines).rstrip()
			b = random.choice(nouns_lines).rstrip()
		if (rand == 2):
			a = random.choice(adverbs_lines).rstrip()
			b = random.choice(verbs_lines).rstrip()
		else:
			pass
		tweet = a + ' ' + b
		#print(tweet)
		api.update_status(tweet)
		sleep(86400)

niceandgood()

adjectives_file.close()
nouns_file.close()
adverbs_file.close()
verbs_file.close()
