import logging
import random
import markup as nav
import markup as gav
from db import Database
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types

TOKEN ="5829323052:AAHLWcWyxWlxijYjxZJkoFSYUlnx-ENw4rA"


#Подключение к базе данных
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = Database('Gattsu.db')
#bot
#!Сделать нормальный вход в Профиль!
datanow = {datetime.now().strftime('%d')}

# удаление всех сообщений
async def Delete_Mes(message, var1, var2):
    try:
        for i in range(var1, var1 + var2):
            await bot.delete_message(message.chat.id, message.message_id - i)
    except:
        print()
#запуск всей программы
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.chat.id, f"Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>\nЯ бот Beitman", parse_mode='html')
    await Delete_Mes(message, 1, 100)
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваш ник")
    else:
        if db.get_sign_up(message.from_user.id):
             await bot.send_message(message.from_user.id,"Вы успешно вошли в Профиль", reply_markup=gav.mainMenu)
        else:
             await bot.send_message(message.from_user.id, "Неправильный никнейм")
#проверка сообщений
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == '🏬🏬Меню':
             await bot.send_message(message.from_user.id,"Меню", reply_markup=nav.mainMenu)
             await Delete_Mes(message, 1, 100)
        elif message.text == '🎃Вход⚔️':
             await bot.send_message(message.from_user.id,"Вы вошли в свой аккаунт", reply_markup=gav.mainProfile)
             await Delete_Mes(message, 1, 100)
        elif message.text == '💼ПРОФИЛЬ':
             await bot.send_message(message.from_user.id,"Ваш Профиль", reply_markup=gav.mainProfile)
             await Delete_Mes(message, 1, 100)
        elif message.text == '☠️Выход':
             await bot.send_message(message.chat.id, "Вы вышли из аккаунта", reply_markup=gav.Bixod)
             await Delete_Mes(message, 1, 100)
        elif message.text == '🧱Мой Id':
             await bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}", reply_markup=nav.mainMenu)
             await Delete_Mes(message, 1, 100)
        elif message.text == '💎Мой Ник':
            user_nickname = "Ваш ник: " + db.get_nickname(message.from_user.id)
            await bot.send_message(message.chat.id,user_nickname, reply_markup=gav.mainProfile)   
            await Delete_Mes(message, 1, 100)
        elif message.text == '🍸Дата':
            await bot.send_message(message.from_user.id, f'Текущая дата {datetime.now().strftime("%D")}\nТекущее время {datetime.now().strftime("%H:%M:%S")}', reply_markup=nav.mainMenu)
            await Delete_Mes(message, 1, 100)
        elif message.text == '🍻Сайт':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Наш сайт", url="https://t.me/+zF7JCsov69lhODUy"))
            await bot.send_message(message.from_user.id, 'Перейти на сайт',reply_markup=markup)
            await Delete_Mes(message, 1, 100)
            await bot.send_message(message.from_user.id, '🏬🏬Меню', reply_markup=nav.mainMenu)
        elif message.text == 'Все команды':
            await bot.send_message(message.from_user.id, '🧱Мой Id - показыват ваш Id\n💎Мой Ник - показывает ваш ник\n🍸Дата - показывает сегодняшнюю дату и точное время\n🍻Сайт - присылает ссылку на сайт\nВсе команды - показывает все добавленные и реализованные команды\n🛩Мем - присылает рандомно актуальный мем', reply_markup=nav.mainMenu)
            await Delete_Mes(message, 1, 100)
        elif message.text == 'Обо мне':
            await bot.send_message(message.from_user.id, 'Я бот Beitman. В мой функионал входит, возможность присылать мемы, подробнее смотрите в <b>Все команды</b>', parse_mode='html' ,reply_markup=nav.mainMenu)
            await Delete_Mes(message, 1, 100)
        elif message.text == '🛩Мем🏢🏢':
            await bot.send_message(message.from_user.id, 'Обработка информации', reply_markup=gav.mainProfile)
            #Адрессация к картинкам которые я использую
            img_list = ['https://sun9-4.userapi.com/impg/HC-qajseTuUcaS6mdvNUEW3hANv3oNHoepGKfg/W7q3IVl5LNk.jpg?size=1372x1306&quality=96&sign=32cc488fb26227f2c8560a3f0540d213&type=album','https://sun9-3.userapi.com/impg/M5RcVoNJRsavzyUMz9o6PjC8nfmqhmCsEz-VXQ/JMZyaG8OWD4.jpg?size=1080x1017&quality=95&sign=fbf5a7d7cc89addad4157db768a8f59e&type=album','https://sun9-80.userapi.com/impg/34LHJBhpP7BXdQHHJ9gfdR00fsG8ETcrBqmEug/UouhKcFMMqI.jpg?size=640x640&quality=95&sign=835c4d0d19e5d9471436caff38116ee1&type=album','https://sun9-73.userapi.com/impg/ZQ1T2vrOo2O7WIBP4OqcZ410N_G6ladK8ZNVsA/aRRoBw_GMoI.jpg?size=736x672&quality=96&sign=7803ca99450697ca0cf13a99804a6d94&type=album','https://sun9-66.userapi.com/impg/CJ7wqijDSt11upQ3uonMOXrnRPSmsHwznTb9pA/Jnq06UHABGc.jpg?size=1021x834&quality=95&sign=b869f52827114fbe7d29974a6bfa503f&type=album','https://sun9-29.userapi.com/impg/ttsRJ3NkyGWxEngWM0pzPQY1_om3jtW1Gq7ACQ/bYydcmsGBcA.jpg?size=746x1080&quality=96&sign=a989d8efeca96b89b0ca78c3138b54c7&type=album','https://sun9-9.userapi.com/impg/qDbv7ANcUphfDtUiEUMH3JqIWcsCSiGz3qiYqA/VxS-Vvg_1-U.jpg?size=1162x1294&quality=96&sign=faac80a40541dc3e6a01d53247781048&type=album','https://sun9-26.userapi.com/impg/HxG9_S4m0dSplGZgyCrtXwevRMXt0UzXLwAWsQ/ZjDA2AbWqAc.jpg?size=1280x720&quality=95&sign=8a5edb49ecb8218881ea8704eae52952&type=album','https://sun9-84.userapi.com/impg/RPbNVNANaXmV3xu2PxWZBa8heT9PQdLExekqQA/O9zN8yStrhA.jpg?size=1600x1600&quality=95&sign=ad10455ebfecea01c2dcb862d592a629&type=album','https://sun9-82.userapi.com/impg/QiVwvu_czHb4sScJWCeEtJQqfD3z0AS2qGsHdg/kCpwTsBM77M.jpg?size=530x711&quality=96&sign=123236459bc2fb95f2b41df8ff79d0be&type=album','https://sun9-67.userapi.com/impg/We9yVPzQ8s0p-D1ZzhrEgC-4iJbHFAFvHm58_w/2Dqxg52i7TA.jpg?size=499x502&quality=95&sign=208270b13a51180ffb08e36a323654ea&type=album','https://sun9-51.userapi.com/impg/uiot6Sa-sucIN3CHF1eXJcFDmB4jVwI1gLI2hQ/SbtlgMp-ggw.jpg?size=506x675&quality=96&sign=1d0bc5ba26c615f40f7dd946eb242a61&type=album','https://sun9-79.userapi.com/impg/9shnq5LO_LLK2VhjC1sfOxM457KamFUZ8MmU4g/2Q_A9kppGdI.jpg?size=1080x845&quality=96&sign=3ab21d27ff5146c5e948409ffa18051e&type=album', 'https://sun9-86.userapi.com/impg/VrcG4gbEgWy9jdY3H9KuVpdO7-nzDdmnqBXPRA/8y7Q9HD-sVM.jpg?size=1142x1042&quality=96&sign=a991e417b7f7531a83e23c990b18a6a2&type=album.jpg,https://sun9-1.userapi.com/impg/P3H3Ee1Sd8eP4Kyq9AxgXorjZvetH1OLP5yxcQ/FH3UAel18JA.jpg?size=960x818&quality=96&sign=c14deef28d68c61889313f3359f22890&type=album', 'https://sun9-9.userapi.com/impg/EriFYl-76ZW3C92irGwiOuIJD7I6lyHS7nOX8w/nIfHOteDzIQ.jpg?size=894x864&quality=96&sign=7d0337fa21917c269f5edfa30914b386&type=album', 'https://sun9-46.userapi.com/impg/EnAxnxSlKQ9EjEvYS_KDKMhXWGzN9ahmOKUAjg/mEUpsp9peyA.jpg?size=800x589&quality=95&sign=5ca3029a056f0521d00fc306cc33d747&type=album', 'https://sun9-31.userapi.com/impg/FFCrq5ALX7E7DUASgRYaI2CCbLH3e0FYOgWsJQ/EgxDYwNo5y8.jpg?size=758x590&quality=96&sign=c5b0193bd879e298798ed4d8285c74b8&type=album']
            img_path = random.choice(img_list)
            await bot.send_photo(message.from_user.id, img_path)
            await Delete_Mes(message, 1, 100)
        else:
            if db.get_sign_up(message.from_user.id) == "setnickname":
                if(len(message.text) > 15):
                     await bot.send_message(message.from_user.id, "Никнейм не должен превышать 15-ти символов")
                elif '@' in message.text or '/' in message.text:
                     await bot.send_message(message.from_user.id, "Вы использовали запрещённый символ")
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    db.set_sign_up(message.from_user.id, "done")
                    await bot.send_message(message.from_user.id, "Регестрация прошла успешно !", reply_markup=nav.mainMenu)
            else:
                 await bot.send_message(message.from_user.id, "Я вас не понимаю")
                 await Delete_Mes(message, 1, 100)
#polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)