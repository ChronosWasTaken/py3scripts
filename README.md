# python3snippets
collection of kind of useful python3 scripts 

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

- youtube-dl (install with your preferred package manager, examples below)
- inquirer (install with pip, `pip3 install inquirer`)

Usage: `./youtube-dl.py <something to look up>`

### Arch Linux, Antergos:
```
pacman -S youtube-dl
```

### Debian, Ubuntu, Linux Mint, Elementary OS, etc:
```
sudo apt-get install youtube-dl
```

### Mac OS X, OSX
```
brew install youtube-dl
```

etc.
