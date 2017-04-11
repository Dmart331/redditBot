import praw

reddit = praw.Reddit("bot1" , user_agent='bot1 user agent')

words_to_match = ['definately', 'definatly', 'definetly']
cache = []

def run_bot():
    subreddit = [reddit.subreddit('space') ]  
    comments = []
    for submission in subreddit:
        print(submission.title)  # Output: the submission's title
        print(submission.score)  # Output: the submission's score
        print(submission.id)     # Output: the submission's ID
        print(submission.url) 
    
        comments = submission.comments.list()

    for comment in comments: 
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)

        if isMatch:
            comment.reply('I think you meant to say "definitely"')
            cache.append(comment.id)

while True:
    run_bot()
    time.sleep(10)