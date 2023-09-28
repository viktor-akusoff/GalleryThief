# Gallery Thief


![Gallery Thief Logo](https://i.imgur.com/j3TgyZc.png)

Simple python package scraping images by propmt from different search engines.

## Quick Start

```
from GalleryThief.performer import Thief
from GalleryThief.strategies import StealingFromYandex

strategy = StealingFromYandex() # Creating strategy for getting images
thief = Thief(strategy) # Creating thief using this strategy

# Ordering thief to get one image of Pluto from yandex images
result = Thief.get_images_list(['Photo of Pluto', 1]) 

print(result)
```

## Guide

Work in progress...