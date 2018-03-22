import praw
from twilio.rest import Client
import time
with open("secret.txt") as f:
	secret = f.readlines()
	account_sid = secret[0].rstrip()
	auth_token = secret[1].rstrip()
client = Client(account_sid, auth_token)
reddit = praw.Reddit(client_id = 'ID', client_secret = 'SECRET', user_agent= 'Crypto Checker Bot v1 by github.com/schembora')
while True:
	for submission in reddit.subreddit('cryptocurrency').new(limit=20):
		if int(time.time()) - int(submission.created_utc) <= 1800:
			if submission.score >= 50:
				message = client.messages.create(
		    		to="TO_NUMBER", 
		    		from_="FROM_NUMBER",
		   			body="Title: " + submission.title + "\nScore: " + str(submission.score) + " \n" + submission.url)
	print("Going to Sleep for 15 minutes")
	time.sleep(60*15)