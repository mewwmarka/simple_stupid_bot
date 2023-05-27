from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from custom_types import ActionType, CuEFaType


def get_base_markup() -> ReplyKeyboardMarkup:
    return (
        ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Выберите действие")
        .row(KeyboardButton(text=ActionType.GAME.value), KeyboardButton(text=ActionType.STAT.value))
        .add(KeyboardButton(text=ActionType.HELP.value))
    )


def get_game_markup() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        resize_keyboard=True, input_field_placeholder="Камень,Ножницы, Бумага", row_width=3
    ).add(
        KeyboardButton(CuEFaType.SCISSORS.value),
        KeyboardButton(CuEFaType.STONE.value),
        KeyboardButton(CuEFaType.PAPER.value),
        KeyboardButton(ActionType.BACK.value),
    )


def get_finish_game_markup() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
        KeyboardButton(ActionType.GAME.value),
        KeyboardButton(ActionType.STAT.value),
        KeyboardButton(ActionType.BACK.value),
    )
