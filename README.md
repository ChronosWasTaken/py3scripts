# python3snippets
collection of kind of useful python3 scripts 

## sporecast-downloader.py

download a sporecast from the sporepedia, has a nice logging system and all built in

reqs:

- Requests (`pip3 install requests`)

Usage: You can either pass the sporecast url to the program via arguments or execute it as-is and wait till asked

## urban.py

Short description:

Look something up on urbandictionary. Currently it only returns 2 definitions, I don't see why would you need more.

Requirements: 

- None.

Usage: `./urban.py <word to look up, must enclose in quotes>`

## fetchreddit.py

Short description:

Fetch original url from reddit post (redd.it links). 

Requirements:

- [PRAW.](http://praw.readthedocs.io/en/latest/getting_started/installation.html)

Must [set up PRAW.ini](https://praw.readthedocs.io/en/v3.6.2/pages/configuration_files.html) before use. 

Usage: `./fetchreddit.py <reddit id of the post>`

by reddit id I mean [this](https://puu.sh/AlEun/157c7ee5f1.png)

## youtube-dl.py

Short description:

You can use this script to look up something on youtube and automatically download it as an mp3 via youtube-dl.

Requirements:

- BeautifulSoup4 (install with pip, `pip3 install beautifulsoup4`)
- youtube-dl & ffmpeg (install with your preferred package manager, examples below)
- inquirer (install with pip, `pip3 install inquirer`)

Usage: `./youtube-dl.py <something to look up, must enclose in quotes>`

### Arch Linux, Antergos:
```
# pacman -S youtube-dl ffmpeg
```

### Debian, Ubuntu, Linux Mint, Elementary OS, etc:
```
# apt-get install youtube-dl ffmpeg
```

### Mac OS X, OSX
```
$ brew install youtube-dl ffmpeg
```

etc.
