import praw
import pprint
from PIL import Image, ImageDraw, ImageFont
import time
import sys
#TODO: get the image text converter to work
subReddit = 'todayilearned'
reddit = praw.Reddit(client_id='3QBnDb_NxGrPBA',
                     client_secret='s531SAL5eUWGk4O_sXQ4WcOozFc',
                        user_agent='my user agent')

def getSubmissions(amount):
# get random submisions
    data = []
    for i in range(amount):
        submission = reddit.subreddit(subReddit).random()
        while(submission.title in data):
            submission = reddit.subreddit(subReddit).random()
        data.append(submission.title)

    return data


