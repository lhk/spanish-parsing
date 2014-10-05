spanish-parsing
===============

I found a spanish dictionary in a parsing-friendly format here: https://github.com/evilgeniuschronicles/Kindle-Language-Dictionaries

With this dictionary I'm creating a sqlite db for our vocab-trainer:
Each line of the dict is parsed against a regex, if a new word is introduced in that line, another file is checked, if this word belongs to the 10000 most used words in spanish subtitles.

-> 4000 something words are found
