#!/usr/local/bin/python3
#Chronos, 2018.
#TODO: use fancier colors, add as prefix the votes of each definition
import sys, urllib.request, json

if len(sys.argv) == 2:
    word = sys.argv[1]
else:
    word = input('word to look up? ')
 
j = urllib.request.urlopen('http://api.urbandictionary.com/v0/define?term=' + word) 

urbanparsed = json.load(j)['list']
urbandef0 = urbanparsed[0]['definition']
urbandesc0 = urbanparsed[0]['example']
urbandef1 = urbanparsed[1]['definition']
urbandesc1 = urbanparsed[1]['example']
print('\033[94m'+urbandef0+'\n'+urbandesc0+'\n')
print('\033[91m'+urbandef1+'\n'+urbandesc1)
