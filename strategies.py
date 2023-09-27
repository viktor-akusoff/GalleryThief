from abc import ABC, abstractmethod
from typing import List

StealingResult = List[str]


class StealingStrategy(ABC):

    @abstractmethod
    def get_images(self, prompt: str, count: int) -> StealingResult:
        pass


class StealingFromYandex(StealingStrategy):

    def get_imagess(self, prompt: str, count: int) -> StealingResult:
        return []


class StealingFromGoogle(StealingStrategy):

    def get_images(self, prompt: str, count: int) -> StealingResult:
        return []
