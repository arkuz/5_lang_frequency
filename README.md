# Frequency Analysis of Words

This script performs frequency analysis of words in the text file in any language.

The script takes 2 parameters:
+ ` - file` - input file with the text
+ ` - count` - сount of most frequent words to output to terminal, optional parameter, default value = 10

Sample text files:
+ Russian - [text_ru.txt](http://rgho.st/private/6Rt6yCrSm/e7bc678e2b5d03071c479cd7f6ebad5b)
+ English - [text_en.txt](http://rgho.st/private/67XLrChC5/a05850549b5a617ec6226b0ac3706119)
+ French - [text_fr.txt](http://rgho.st/private/6xjr98KPn/18baab36bacf761b3f3431b5d55f860e)

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash
$ python3 lang_frequency.py -file=text_en.txt -count=5
List of most frequent words:
('is', 6)
('and', 6)
('a', 5)
('the', 5)
('in', 4)
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
