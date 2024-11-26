from abc import ABC, abstractmethod


class FigureBase(ABC):
    def __init__(self, side_a: int):
        self.side_a = side_a
        return

    @abstractmethod
    def get_two_d_art(self) -> str:
        pass

    @abstractmethod
    def get_three_d_art(self) -> str:
        pass
