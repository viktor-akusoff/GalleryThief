import json
from abc import ABC, abstractmethod
from typing import List
from enum import Enum
from bs4 import BeautifulSoup

from .mask import RobberMask

PROXY_SOURCE = "https://freeproxyupdate.com/files/txt/http.txt"

StealingResult = List[str]


class StealingStrategy(ABC):

    @abstractmethod
    def get_images(self, prompt: str, count: int) -> StealingResult:
        pass


class YandexSizes(Enum):
    LARGE = 'large'
    MEDIUM = 'medium'
    SMALL = 'small'
    WALLPAPER = 'wallpaper'
    ANY = 'any'


class YandexOrientation(Enum):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'
    ANY = 'any'


class YandexImageType(Enum):
    PHOTO = 'photo'
    CLIPART = 'clipart'
    LINEART = 'lineart'
    FACE = 'face'
    DEMOTIVATOR = 'demotivator'
    ANY = 'any'


class YandexFileType(Enum):
    PNG = 'png'
    JPEG = 'jpeg'
    GIF = 'gifan'
    ANY = 'any'


class YandexColor(Enum):
    COLOR = 'color'
    GRAY = 'gray'
    RED = 'red'
    ORANGE = 'orange'
    YELLOW = 'yellow'
    CYAN = 'cyan'
    GREEN = 'green'
    BLUE = 'blue'
    VIOLET = 'violet'
    WHITE = 'white'
    BLACK = 'black'
    ANY = 'any'


class StealingFromYandex(StealingStrategy):
    '''
    Implements parsing algorithm for Yandex Images.
    '''

    def __init__(
        self,
        size: YandexSizes = YandexSizes.ANY,
        orientation: YandexOrientation = YandexOrientation.ANY,
        image_type: YandexImageType = YandexImageType.ANY,
        file_type: YandexFileType = YandexFileType.ANY,
        color: YandexColor = YandexColor.ANY,
        site: str = '',
        recent: bool = False,
    ):
        '''
        Initializes strategy for getting images from Yandex with given params.

        size -> (SMALL, MIDDLE, LARGE, WALLPAPER, ANY)\n
        orientation -> (HORIZONTAL, VERTICAL, ANY)\n
        image_type -> (PHOTO, CLIPART, LINEART, FACE, DEMOTIVATOR, ANY)\n
        file_type -> (PNG, JPEG, GIF, ANY)\n
        color -> (COLOR, GRAY, RED, ORANGE, YELLOW, CYAN, GREEN, BLUE, VIOLET,\
                  CYAN, WHITE, BLACK, ANY)\n
        site -> specifies the site images are from.\n
        recent -> if True looks for images published in last seven days.
        '''

        self._size: YandexSizes = size
        self._orientation: YandexOrientation = orientation
        self._image_type: YandexImageType = image_type
        self._file_type: YandexFileType = file_type
        self._color: YandexColor = color
        self._site: str = site
        self._recent: bool = recent

        self._mask = RobberMask(
            source=PROXY_SOURCE,
            url="https://yandex.ru/images/search",
            proxies_limit=10
        )

    @property
    def size(self) -> YandexSizes:
        return self._size

    @size.setter
    def size(self, size) -> None:
        self._size = size

    @property
    def orientation(self) -> YandexOrientation:
        return self._orientation

    @orientation.setter
    def orientation(self, orientation) -> None:
        self._orientation = orientation

    @property
    def image_type(self) -> YandexImageType:
        return self._image_type

    @image_type.setter
    def image_type(self, image_type) -> None:
        self._image_type = image_type

    @property
    def file_type(self) -> YandexFileType:
        return self._file_type

    @file_type.setter
    def file_type(self, file_type) -> None:
        self._file_type = file_type

    @property
    def color(self) -> YandexColor:
        return self._color

    @color.setter
    def color(self, color) -> None:
        self._color = color

    @property
    def site(self) -> str:
        return self._site

    @site.setter
    def site(self, site) -> None:
        self._site = site

    @property
    def recent(self) -> bool:
        return self._recent

    @recent.setter
    def recent(self, recent) -> None:
        self._recent = recent

    def get_images(self, prompt: str, count: int = 1) -> StealingResult:

        result: StealingResult = []

        params = {"text": prompt}

        if self._size != YandexSizes.ANY:
            params["isize"] = self._size.value

        if self._orientation != YandexOrientation.ANY:
            params["iorient"] = self._orientation.value

        if self._image_type != YandexImageType.ANY:
            params["type"] = self._image_type.value

        if self._file_type != YandexFileType.ANY:
            params["itype"] = self._file_type.value

        if self._color != YandexColor.ANY:
            params["icolor"] = self._color.value

        if self._site:
            params["site"] = self._site

        if self._recent:
            params["recent"] = "7D"

        request = self._mask.reach_out(params)

        soup = BeautifulSoup(request, 'html.parser')
        items_place = soup.find('div', {"class": "serp-list"})

        if items_place is None:
            return result

        item_params = ("div", {"class": "serp-item"})
        items = items_place.find_all(*item_params)  # type: ignore
        counter = 0

        for item in items:
            data = json.loads(item.get("data-bem"))
            result.append(data['serp-item']['img_href'])
            counter += 1
            if counter == count:
                break

        return result


class StealingFromGoogle(StealingStrategy):

    def get_images(self, prompt: str, count: int) -> StealingResult:
        return []
