import praw
import random
import time

reddit = praw.Reddit(
    #Get this information in https://www.reddit.com/prefs/apps
    client_id="k4Yos5koWU2ULw",
    client_secret="c9hSWfYGOlpjD1RMazB39SeZ5msuiw",

    user_agent="<console:WingMan>",
    username= "Affectionate_Mud_327",
    password = "09487311743b")

subreddit = reddit.subreddit("AskMen")

sad_quotes = ["“The Best Way To Get Started Is To Quit Talking And Begin Doing.” – Walt Disney",
              "“Don’t Let Yesterday Take Up Too Much Of Today.” – Will Rogers",
              "“The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.” – Winston Churchill",
              "“The way to love anything is to realize that it may be lost.”— Gilbert K. Chesterton"]

for submission in subreddit.hot(limit = 10):
    #print("+++++++++++++++++++")
    #print(submission.title)

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print("-------")
                print(comment.body)
                random_index = random.randint(0, len(sad_quotes)-1)
                comment.reply(sad_quotes[random_index])
                time.sleep(300)