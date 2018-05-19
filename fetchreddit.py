#!/usr/bin/python3
#Chronos, 2018
import praw, sys
from subprocess import Popen,PIPE

if len(sys.argv) == 2:
    link = sys.argv[1]
else:
    link = input('enter reddit id: ')

r = praw.Reddit('bot1', user_agent='bot1 user agent')
submission = r.submission(id=link)
p1 = Popen(["echo",submission.url], stdout=PIPE) #print submission url
p2 = Popen(["pbcopy"],stdin=p1.stdout,stdout=PIPE) #copy submission url to clipboard
p2.wait()
if p2.returncode == 0:
    print("copied url to clipboard.")
else:
    print(p2.returncode)
