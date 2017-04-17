import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')
defOfDef = "definitely"
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []
else:
	with open("posts_replied_to.txt", "r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('futurology')

for submission in reddit.front.hot(limit=5):
	if submission.id not in posts_replied_to:
		comments = submission.comments.list()
		print(submission.id)
		for comment in comments:
			if defOfDef in comments:
				submission.reply("*BLeeP BloOp* I think you meant defanately!")
				print("Bot replying to : ", submission.comment.username)
				posts_replied_to.append(submission.id)
				with open('posts_replied_to.txt', 'w') as f:
					for post_id in posts_replied_to:
						f.write(post_id + "\n")