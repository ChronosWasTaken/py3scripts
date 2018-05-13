# python3snippets
collection of kind of useful python3 scripts 

## urban.py

Requirements: 

- None.

Usage: `./urban.py <word to look up, must enclose in quotes>`

## fetchreddit.py

Requirements:

- [PRAW.](http://praw.readthedocs.io/en/latest/getting_started/installation.html)

Must [set up PRAW.ini](https://praw.readthedocs.io/en/v3.6.2/pages/configuration_files.html) before use. 

Usage: `./fetchreddit.py <reddit id of the post>`

## youtube-dl.py

Requirements:

- youtube-dl (install with your preferred package manager, examples below)
- inquirer (install with pip, `pip3 install inquirer`)

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
