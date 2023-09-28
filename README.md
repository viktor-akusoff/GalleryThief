# Gallery Thief


![Gallery Thief Logo](https://i.imgur.com/j3TgyZc.png)

> Gallery Thief, an artful liar\
> Cunningly steals your heart's desire.\
> Python library, so refined,\
> Your digital treasures are its' prize.

*YandexGPT2, 2023*

## Introduction

Gallery Thief is a simple web-scraping tool designed for parsing images in different search engines.

It isn't fast because it tries to keep all the captcha stuff away by changing User-Agent, proxy and
refer every its request. It also has some kind of a cooldown between two requests to make them
less repetitive and suspicious.

First run takes a while because it loads proxy list from [freeproxyupdate.com](https://freeproxyupdate.com).
After that you can send several requests and they will be processed much faster than an inital run.

## Quick Start

If you installed this package correctly you can just copy and paste this example code to test
how does it work:

```
from GalleryThief.performer import Thief
from GalleryThief.strategies import StealingFromYandex

strategy = StealingFromYandex()  # Creating strategy for getting images
thief = Thief(strategy)  # Creating thief using this strategy

# Ordering thief to get one image of Pluto from yandex images
result = thief.get_images_list(['Photo of Pluto', 1])

print(result)
```

## Guide

Work in progress...