import praw

reddit = praw.Reddit(client_id="5NIELuR-oCvjtA",
                     client_secret="WqI5sOGwlVrnUw2bDHpOSU0_RaY",
                     user_agent="Def Bot 0.1")
    # client_id= "5NIELuR-oCvjtA",
# client_secret= "WqI5sOGwlVrnUw2bDHpOSU0_RaY",
# username= "_Def__Bot_" ,
# password= "shitghost2",
# user_agent= "Def Bot 0.1")

subreddit = reddit.subreddit("learnpython")

print(reddit.read_only)

for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)
# print(subreddit.display_name)
# print(subreddit.title)
# print(subreddit.descrpition)