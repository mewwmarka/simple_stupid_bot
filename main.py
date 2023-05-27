from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from buttons import get_base_markup, get_finish_game_markup, get_game_markup
from custom_types import ActionType, CuEFaResult, CuEFaType
from messages import get_finish_game_message, get_game_message, get_help_message, get_stat_message
from statistic import StatManager

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from CuEFa import Ui_MainWindow


dp: Dispatcher = Dispatcher(
    Bot(
        token="5723291215:AAEKiVN_ws2T_t_wB0RGr6SJyohEo7zuBj0",
    )
)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        "Приветствую в игре 'Камень, ножницы, бумага'", reply_markup=get_base_markup()
    )


@dp.message_handler(Text([ActionType.HELP.value]))
async def bot_help(message: types.Message):
    await message.answer(get_help_message(), reply_markup=get_base_markup())


@dp.message_handler(Text([ActionType.BACK.value]))
async def bot_back(message: types.Message):
    await message.answer(text="Откатываюсь в главное меню", reply_markup=get_base_markup())


@dp.message_handler(Text([ActionType.GAME.value]))
async def bot_game(message: types.Message):
    await message.answer(get_game_message(), reply_markup=get_game_markup())


@dp.message_handler(lambda message: message.text in CuEFaType.get_values())
async def bot_check_result(message: types.Message):
    player_result: CuEFaType = CuEFaType(message.text)
    bot_result: CuEFaType = CuEFaType.get_random_enum()
    result: CuEFaResult = player_result == bot_result
    await StatManager.save_user_file(message.from_id, result)
    await message.answer(
        get_finish_game_message(opponent_choice=bot_result.value, result=result.value),
        reply_markup=get_finish_game_markup(),
    )


@dp.message_handler(Text([ActionType.STAT.value]))
async def bot_stat(message: types.Message):
    await message.answer(
        get_stat_message(await StatManager.repr_stat(message.from_id)),
        reply_markup=get_base_markup(),
    )


class CuEFa_UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(CuEFa_UI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.ui.pushButton.clicked.connect(self.launch())

    def init_UI(self):
        self.setWindowTitle('CuEFa_Bot')
        self.setWindowIcon(QIcon('CuEfa.png'))

    def launch(self):
        executor.start_polling(dp)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = CuEFa_UI()
    application.show()
    sys.exit(app.exec())
