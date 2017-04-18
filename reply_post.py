import praw
import pdb
import re
import os
from urllib.request import quote 

r = praw.Reddit('bot1')
r.read_only = False #no idea if this is required. Kept it to be safe.
subreddit = r.subreddit("futurology") #get the subreddit. "all" for all comments
f = open("./posts_replied_to.txt") #REPLACE THE PATH
 
   
 
comments = subreddit.stream.comments() # get the comment stream
x = 1 #for the counter
# for comment in comments: #for each comment in the comments stream. the current comment being processed is called "comment"
#     print("found new comment! processing... (" + str(x) + ")") #the str(x) thing is printing the number of the comment being proccesed
#     x += 1 #add 1 to the number
#     text = str(comment.body) # Fetch body
#     try:
#         author = str(comment.author) # Fetch author
#     except AttributeError: #check if the author has been deleted
#         print("Author has been deleted")
#         #author was deleted
#         continue
#     print(text) #DEBUGGING, REMOVE WHEN WORKING
#     print(author) #SAME
#     if author.lower() == "YOURUSERNAMEHERE".lower(): #Don't reply to yourself
#         #myself
#         print("Comment is by myself")
#         continue
 
#     if any("flat" in s for s in text): #check to see the comment is "!lmgtfy". use if text.lower() == "!lmgtfy".lower() to be non-case sensitive, use if "!lmgtfy" in text if you want the comment to be anywhere
#         if comment.id in f.read(): #if the comment is already in the file, bot has replied to it
#             print("ALREADY IN FILE")
#         if comment.id not in f.read(): #^
#             # Generate a message
#             print("Attempting Answer")
#             parid = comment.parent_id #by /u/bboe
#             parbody = r.comment(comment.parent_id.rsplit('_', 1)[1])#by /u/bboe
#             parentbody = parbody.body #by /u/bboe, fetches the body of the parent comment
#             message = "http://lmgtfy.com/?q=" + quote(str(parentbody)) + "\n\n_____\n\n^by ^/u/Shrellex. ^Please ^only ^use ^when ^the ^answer ^is ^blatantly ^obvious. ^Call ^the ^bot ^with ^!lmgtfy ^and ^it ^will ^lmgtfy-ify ^the ^parent ^comment. ^Please ^don't ^downvote ^me."
#             #quote() url-ifies the text, self explanatory i hope
#             try:
#                 comment.reply(message) #reply to comment
 
#             except praw.errors.Forbidden:
#                 print('403 error - is the bot banned from sub %s?' % "not impl")
#             print("Replied to comment by " + author)
#             f.write(comment.id + "\n")#write comment id to file so it doesn't reply to it again
#             if comment.id in f.read():
#                 print("Written Successfully!")
defOfDef = "definitely"
# x = 1


# f = open('./posts_replied_to.txt')
# subreddit = reddit.subreddit('futurology')
# comments = subreddit.stream.comments()

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
    if author.lower() == "YOURUSERNAMEHERE".lower(): #Don't reply to yourself
    #myself
        print("Comment is by myself")
        continue

    # if defOfDef in text:
    #     if comment.id in f.read(): #if the comment is already in the file, bot has replied to it
    #         print("ALREADY IN FILE")
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
    #             print("Written Successfully!")

    if defOfDef in text:
        comment.reply("*BLeeP BloOp* I think you meant definitly!")
        print("Bot replying to ", comment.author)
        f.write(comment.id)
      

                