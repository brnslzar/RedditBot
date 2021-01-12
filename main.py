import praw
import random
import time

reddit = praw.Reddit(
    #Get this information in https://www.reddit.com/prefs/apps
    client_id="k4Yos5koWU2ULw",
    client_secret="c9hSWfYGOlpjD1RMazB39SeZ5msuiw",
    
    #Put your account info here
    user_agent="",
    username= "",
    password = "")

subreddit = reddit.subreddit("AskMen")

sad_quotes = ["“The Best Way To Get Started Is To Quit Talking And Begin Doing.” – Walt Disney",
              "“Don’t Let Yesterday Take Up Too Much Of Today.” – Will Rogers",
              "“The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.” – Winston Churchill",
              "“The way to love anything is to realize that it may be lost.”— Gilbert K. Chesterton"]

for submission in subreddit.hot(limit = 10):
    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print("-------")
                print(comment.body)
                random_index = random.randint(0, len(sad_quotes)-1)
                comment.reply(sad_quotes[random_index])
                time.sleep(300)
