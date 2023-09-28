import json
from abc import ABC, abstractmethod
from typing import List
from enum import Enum
from bs4 import BeautifulSoup

from mask import RobberMask

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
    ANY = 'ANY'


class YandexOrientation(Enum):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'
    ANY = 'ANY'


class YandexImageType(Enum):
    PHOTO = 'photo'
    CLIPART = 'clipart'
    LINEART = 'lineart'
    FACE = 'face'
    DEMOTIVATOR = 'demotivator'
    ANY = 'ANY'


class StealingFromYandex(StealingStrategy):

    def __init__(
        self,
        size: YandexSizes = YandexSizes.ANY,
        orientation: YandexOrientation = YandexOrientation.ANY,
        image_type: YandexImageType = YandexImageType.ANY
    ):

        self._size: YandexSizes = size
        self._orientation: YandexOrientation = orientation
        self._image_type: YandexImageType = image_type

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

    def get_images(self, prompt: str, count: int = 1) -> StealingResult:

        result: StealingResult = []

        params = {"text": prompt}

        if self._size != YandexSizes.ANY:
            params["isize"] = str(self._size)

        if self._size != YandexOrientation.ANY:
            params["iorient"] = str(self._orientation)

        if self._orientation != YandexImageType.ANY:
            params["type"] = str(self._image_type)

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
