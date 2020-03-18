import requests
import random
import datetime

from bot_config import TOKEN as bot_token
from bot_config import ID as bot_chatID

dayOfWeekUA = ("Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя")
todayWeekDay = datetime.datetime.today().weekday()
tranformWeekDayFromNumberToString = dayOfWeekUA[todayWeekDay]

def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

VerbsForWeekDay = ["Сьогодні в нас", "Отакої", "Неочікувано але", "І що то робити, якщо", "Невстиг простунись як вже", "Невже настав"]
VerbsForCall = ["Привіт! Ти ж пам'ятаєш, що в нас мітинг за 5хв?", "Як сі маєш? Але то таке - гайда на мітинг!", "Чьо, как? - Будь готовий дати відповідь замовнику =)", "Прівітусіки! І слід шурусіки на міт...", "Хай! Заходь вгості по лінку", "Ти, той во - заходь якшо шо...", "Здоровенькі були, якщо є сили то гайда на мітинг!", "Володарі - прошу підіть на мітинг, бо можуть бути не переливки..."]

if todayWeekDay == 0 or todayWeekDay == 6:
    reminder_text = telegram_bot_sendtext("Вихідні, хоч це й не помітно... \nперевірка Бота на логіку")
else:
    reminder_text = telegram_bot_sendtext("{} {} \n{}".format(
                                                            random.choice(VerbsForWeekDay),
                                                            tranformWeekDayFromNumberToString,
                                                            random.choice(VerbsForCall)))

print(reminder_text)