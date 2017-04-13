import praw

reddit = praw.Reddit("bot1")

subreddit = reddit.subreddit("learnpython")

print(reddit.read_only)

for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)
    print(submission.display_name)
    print(submission.title)
    print(submission.descrpition)