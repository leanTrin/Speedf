
# Reddit imports
import praw
import json

#Reddit functions

subReddit = 'todayilearned'
reddit = praw.Reddit(client_id='3QBnDb_NxGrPBA',
                     client_secret='s531SAL5eUWGk4O_sXQ4WcOozFc',
                        user_agent='my user agent')

def getSubmissions(amount):
# get random submisions
    data = []
    count = 0
    while(len(data) < amount):
        submission = reddit.subreddit(subReddit).random()
        while(submission.title in data or len(submission.title) < 100):
            submission = reddit.subreddit(subReddit).random()
        data.append(submission.title)
        count += 1
        print(count)

    for i in range(len(data)):
        data[i] = str.replace(data[i],"TIL","Today I learned")
    return data

##End of Reddit Functions###################

with open('data.json', 'w') as outfile:
    json.dump(getSubmissions(100), outfile)
