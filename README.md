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
refer every its request. It also has some kind of a cool down between two requests to make them
less repetitive and suspicious.

First run takes a while because it loads proxy list from [freeproxyupdate.com](https://freeproxyupdate.com).
After that you can send several requests and they will be processed much faster than an initial run.

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

Gallery Thief uses several classes to retrieve images from search engines (Google, Yandex, Bing, etc.)

You should know them to achieve full potential of this little package.

### Thief class

Thief is your loyal performer for your mischievous deeds involving some
images web-scraping. You can find his class in ```GalleryThief.performer```.

To create new instance of Thief you must add ```StealingStrategy``` in
its constructor (we'll talk about strategies later). After that you can easily give orders to your helpful minion. Your put them in the simple python lists using special format: ```["Prompt text": str, number_of_images: int]```. To make Thief execute these orders you need call its only method ```get_images_list```. This method can accept as many orders as you wish. For example:

```
result = thief.get_images_list(
    ['Photo of Pluto', 1],
    ['Doctor Who', 2],
    ['Star Trek', 3],
    ['Solaris poster', 1]
)
```
It will return dictionary which keys are your prompts, every key in such dictionary stores list of urls to images it found using ```StealingStrategy```.

Your also can change strategy on fly using Thief's setter:
```
thief.strategy = StealingFromGoogle()
```

### Stealing Strategies Classes

This group of classes are describing different algorithms of getting images for different search engines. They all have their own params, options and etc. so it was logical to separate them into different classes with one abstract parent class called ```StealingStrategy```.
Let's look at them!

 1. #### StealingFromYandex

    Its purpose is obvious because of name of this class. It was designed for scraping "Yandex Images".

    ```
    StealingFromYandex(
        size: YandexSizes = YandexSizes.ANY,
        orientation: YandexOrientation = YandexOrientation.ANY,
        image_type: YandexImageType = YandexImageType.ANY,
        file_type: YandexFileType = YandexFileType.ANY,
        color: YandexColor = YandexColor.ANY,
        site: str = '',
        recent: bool = False,
    )
    ```
    Params description:

    | Parameter     | Description   |
    | ------------- | ------------- |
    | size | selects images of one of special size groups (SMALL, MIDDLE, LARGE, WALLPAPER, ANY) |
    | orientation | selects horizontal or vertical images (HORIZONTAL, VERTICAL, ANY) |
    | image_type | selects images by their type (PHOTO, CLIPART, LINEART, FACE, DEMOTIVATOR, ANY) |
    | file_type | selects images by file type (PNG, JPEG, GIF, ANY) |
    | color | selects images by dominant color in them (COLOR, GRAY, RED, ORANGE, YELLOW, CYAN, GREEN, BLUE, VIOLET, CYAN, WHITE, BLACK, ANY) |
    | site | specifies the site images should be from |
    | recent | if ```True``` looks among images published in last seven days  |

2. #### StealingFromGoogle

    Work in progress...