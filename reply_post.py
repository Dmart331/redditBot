import praw
import pdb
import re
import os
import json
from urllib.request import quote 

r = praw.Reddit('bot1')
r.read_only = False 
subreddit = r.subreddit("all") 
f = open("./posts_replied_to.txt")
 
   
 
defOfDef = "definitely"




def do_the_thing():
    for submission in subreddit.hot(limit=2):
        comments = subreddit.stream.comments() # get the comment stream
        for comment in comments: #for each comment in the comments stream. the current comment being processed is called "comment"
            print("found new comment! processing... (" ")") #the str(x) thing is printing the number of the comment being proccesed
            text = str(comment.body) # Fetch body
            try:
                author = str(comment.author) # Fetch author
            except AttributeError: #check if the author has been deleted
                print("Author has been deleted")
                #author was deleted
                continue
            print(text) #DEBUGGING, REMOVE WHEN WORKING
            if author.lower() == "YOURUSERNAMEHERE".lower(): #Don't reply to yourself
            #myself
                print("Comment is by myself")
                continue

        # if defOfDef in text:

        #     if comment.id not in f.read(): #^
        #         # Generate a message
        #         print("Attempting Answer")
        #         parid = comment.parent_id #by /u/bboe
        #         parbody = r.comment(comment.parent_id.rsplit('_', 1)[0])#by /u/bboe
        #         parentbody = parbody.body #by /u/bboe, fetches the body of the parent comment
        #         message = "*BLeeP BloOp* I think you meant Pasifically!"

        #         try:
        #             comment.reply(message) #reply to comment
     
        #         except praw.errors.Forbidden:
        #             print('403 error - is the bot banned from sub %s?' % "not impl")
        #         print("Replied to comment by " + author)
        #         f.write(comment.id + "\n")#write comment id to file so it doesn't reply to it again
        #         if comment.id in f.read():

            if defOfDef in text:

                f = open('./posts_replied_to.txt', 'w') 
                r = open('./posts_replied_to.txt', 'r')
                if comment.id in r.read(): #if the comment is already in the file, bot has replied to it
                    print("ALREADY IN FILE")
                else: 
                    comment.reply("*BLeeP BloOp* I think you meant definitly!" + "\n")
                    print("Bot replying to ", str(comment.author) + str(comment.id))
                    f.write(comment.id)
                    print("Written Successfully!")
              

if __name__ == '__main__':

    while True:
        do_the_thing()
        time.sleep(500)
                    