#!/usr/local/bin/python3
#Chronos, 2018
#TODO: let the user see a preview of each video, automatically detect when a url is passed as argument and skip to downloading it, maybe make a GUI?
import urllib.request, urllib.parse, sys, inquirer
from bs4 import BeautifulSoup
from subprocess import call

if len(sys.argv) == 2:
    textToSearch = sys.argv[1]
elif len(sys.argv) > 2:
    print('must enclose in quote symbols')
    exit()
else:
    textToSearch = input('look up what?\n')

results = {}
query = urllib.parse.quote(textToSearch) #percent-enconding, in case of trying to look up something with special characters in its name
url = "https://www.youtube.com/results?search_query=" + query 
response = urllib.request.urlopen(url) #get search results
html = response.read()           
soup = BeautifulSoup(html, 'html.parser')       #parse search results
for vid, x in zip(soup.findAll(attrs={'class':'yt-uix-tile-link'}), range(1,9)): #for each video found in the search query
    results[vid['title']]=vid['href']                                     #add to dictionary, formatted as <NAME>:<URL>

choice = [
        inquirer.List('videoToDownload',message='Choose a video',choices=results,
            ),
]
answer = inquirer.prompt(choice) #let the user choose a video
selectedVideo = answer['videoToDownload'] #find out which video they chose
for key, value in results.items():
    if selectedVideo == key:
        download = 'https://www.youtube.com'+value

print('[LOG] url: '+download)
call(["youtube-dl", "--extract-audio", "--audio-format","mp3",download])
