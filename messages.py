import textwrap
from typing import Any


def get_startup_message(name: str) -> str:
    return f"{name} bot in launching"


def get_game_message() -> str:
    return "Начало игры!\nВыберите действие:"


def get_help_message() -> str:
    message = """ 
    Вас приветствует бот игры "Камень, ножницы, бумага.

    Правила просты:
    Бумага бьет камень.
    Камень бьет ножницы.
    Ножницы бьют бумагу.

    В случае одинакового выбора - присуждается ничья.
    """
    return textwrap.dedent(message)


def get_finish_game_message(opponent_choice: str | Any, result: str | Any) -> str:
    message = f"""
    Ваш противник выбрал - {opponent_choice}

    {result}
    Хотите сыграть еще?
    """
    return textwrap.dedent(message)


def get_stat_message(stat: str):
    message = f"""
    Ваша статистика:
    {stat}
    """
    return textwrap.dedent(message)
