import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')
defOfDef = "definitely"
x = 1

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
        for comment in comments: #for each comment in the comments stream. the current comment being processed is called "comment"
            print("found new comment! processing... (" + str(x) + ")") #the str(x) thing is printing the number of the comment being proccesed
            x += 1 #add 1 to the number
            text = str(comment.body) # Fetch body
            try:
                author = str(comment.author) # Fetch author
            except AttributeError: #check if the author has been deleted
                print("Author has been deleted")
                #author was deleted
                continue
            print(text) #DEBUGGING, REMOVE WHEN WORKING

            if defOfDef in text:
                submission.reply("*BLeeP BloOp* I think you meant defanately!")
                print("Bot replying to : ", submission.comment.username)
                posts_replied_to.append(submission.id)
                with open('posts_replied_to.txt', 'w') as f:
                    for post_id in posts_replied_to:
                        f.write(post_id + "\n")

                