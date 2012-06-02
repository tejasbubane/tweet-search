import urllib2
import json

def get_tweets(name):
	s = urllib2.urlopen("http://search.twitter.com/search.json?q="+name).read()
	x = json.loads(s)
	for i in range(len(x['results'])):
		print "%s.%s--> %s\n" %(i, x['results'][i]['from_user_name'], x['results'][i]['text'])
		
name = raw_input("Enter the twitter-username get recent tweets: ")
get_tweets(name)
