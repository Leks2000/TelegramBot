from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnProfile = KeyboardButton('💼ПРОФИЛЬ')
btnId = KeyboardButton('🧱Мой Id')
btnSite = KeyboardButton('🍻Сайт')
btnDate = KeyboardButton('🍸Дата')
btnHelp = KeyboardButton('Обо мне')
btnCommands = KeyboardButton('Все команды')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnProfile, btnId, btnSite, btnDate, btnHelp, btnCommands)

btnYourName = KeyboardButton('💎Мой Ник')
btnMem = KeyboardButton('🛩Мем🏢🏢')
btuMenu = KeyboardButton('🏬🏬Меню')
btnExit = KeyboardButton('☠️Выход')

mainProfile = ReplyKeyboardMarkup(resize_keyboard = True)
mainProfile.add(btnYourName, btuMenu, btnExit, btnMem)

btnBxod = KeyboardButton('🎃Вход⚔️')
Bixod = ReplyKeyboardMarkup(resize_keyboard=True)
Bixod.add(btnBxod)