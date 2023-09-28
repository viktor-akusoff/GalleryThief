import requests
import json
from abc import ABC, abstractmethod
from typing import List
from enum import Enum
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


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


class StealingFromYandex(StealingStrategy):

    def __init__(self, size: YandexSizes = YandexSizes.ANY):
        self._size = size

    @property    
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def get_images(self, prompt: str, count: int = 1) -> StealingResult:
        ua = UserAgent()

        result: StealingResult = []

        params = {"text": prompt}

        if self._size != YandexSizes.ANY:
            params["isize"] = str(self._size)

        request = requests.get(
            "https://yandex.ru/images/search",
            params=params,
            headers={
                "User-Agent": ua.random,
            },
        )

        soup = BeautifulSoup(request.text, 'html.parser')
        items_place = soup.find('div', {"class": "serp-list"})

        if items_place is None:
            return result

        items = items_place.find_all("div", {"class": "serp-item"})
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
