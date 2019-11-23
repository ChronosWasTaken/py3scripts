
import re, requests, sys, os

cd = os.getcwd()
logmark = "[LOG]"
filt = re.compile(r'<img src="(http:\/\/static\.spore\.com\/static\/thumb\/\d+\/\d+\/\d+\/\d+.png)"\/>')
def regsearch1(string):
    # URL that generated this code:
    # http://txt2re.com/index-python.php3?s=http://www.spore.com/sporepedia%23qry=ssc-500646063538&-11&6
    re1='(http)'	# Word 1
    re2='.*?'	# Non-greedy match on filler
    re3='(\\d+)'	# Integer Number 1
    rg = re.compile(re1+re2+re3,re.IGNORECASE|re.DOTALL)
    m = rg.search(string)
    if m:
        word1=m.group(1)
        int1=m.group(2)
        return int1

def regsearch2(string):
    # URL that generated this code:
    # http://txt2re.com/index-python.php3?s=http://static.spore.com/static/thumb/500/442/472/500442472736.png&5
    re1='.*?'	# Non-greedy match on filler
    re2='\\d+'	# Uninteresting: int
    re3='.*?'	# Non-greedy match on filler
    re4='\\d+'	# Uninteresting: int
    re5='.*?'	# Non-greedy match on filler
    re6='\\d+'	# Uninteresting: int
    re7='.*?'	# Non-greedy match on filler
    re8='(\\d+)'	# Integer Number 1
    rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8,re.IGNORECASE|re.DOTALL)
    m = rg.search(string)
    if m:
        int1=m.group(1)
        return int1

def begin():
    if len(sys.argv) < 2:
        url = input('Paste your URL here.\n>> ')
        return url
    else:
        return sys.argv[2]

#main
sporeid = regsearch1(begin())
print(logmark+" Processing Sporecast #"+sporeid)
atomurl = requests.get("http://www.spore.com/atom/sporecast/"+sporeid)
print(logmark+" Filtering...")
searchd = filt.findall(atomurl.text)

for i, y in enumerate(searchd):
    if os.path.exists(regsearch2(y)+".png"):
        print(logmark+"["+str(i)+"/"+str(len(searchd))+"]"" Ignoring already downloaded file... ["+str(regsearch2(y))+"]")
        continue
    else:
        print(logmark+"["+str(i)+"/"+str(len(searchd))+"]"" Currently downloading... ["+str(regsearch2(y))+"]")
        thefile = requests.get(y)
        open(cd+'/'+str(regsearch2(y))+".png",'wb').write(thefile.content)

print("\nDone!")
input("Press any key to continue...")