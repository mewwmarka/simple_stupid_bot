import random
from enum import Enum, unique


class BaseCustomEnum(Enum):
    @classmethod
    def get_values(cls):
        return [en.value for en in cls]


@unique
class CuEFaResult(BaseCustomEnum):
    LOSE = "Поражение... с позором."
    WIN = "Победа!!!"
    DRAW = "Ничья."


@unique
class ActionType(BaseCustomEnum):
    GAME = "Начать игру"
    STAT = "Вывести статистику игрока"
    HELP = "Что делает бот?"
    BACK = "В главное меню"


class StatType(str, Enum):
    TOTAL = "TOTAL"
    WIN = "WIN"
    LOSE = "LOSE"
    DRAW = "DRAW"


@unique
class CuEFaType(BaseCustomEnum):
    SCISSORS = "Ножницы"
    STONE = "Камень"
    PAPER = "Бумага"

    @classmethod
    def get_random_enum(cls):
        return cls(
            random.choice(
                cls.get_values()
            )
        )

    def __eq__(self, other) -> CuEFaResult:
        if self.value == other.value:
            return CuEFaResult.DRAW
        if (
            (self.value == CuEFaType.SCISSORS.value and other.value == CuEFaType.PAPER.value)
            or (self.value == CuEFaType.STONE.value and other.value == CuEFaType.SCISSORS.value)
            or (self.value == CuEFaType.PAPER.value and other.value == CuEFaType.STONE.value)
        ):
            return CuEFaResult.WIN
        return CuEFaResult.LOSE
