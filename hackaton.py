
import telebot
from telebot import types  # кнопки

TOKEN = "1218113804:AAHu7enaQnCTz4Ad5bWruHsKTpIL9gB8mc0"
bot = telebot.TeleBot(token=TOKEN)

user_dict = {}
orders = []


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/about')
    itembtn2 = types.KeyboardButton('/reg')
    markup.add(itembtn1, itembtn2)

    bot.send_message(message.chat.id, "Здравствуйте "
                     + message.from_user.first_name
                     + ", я бот, чтобы вы хотели узнать?", reply_markup=markup)


@bot.message_handler(commands=['about'])
def send_about(message):
    bot.send_message(message.chat.id, "Здравствуйте, Вас приветствует MakersFood, "
                                    + "введите /reg для заказа \nЕсли у Вас " +
                                    "есть вопросы относительно заказа, звоните нам"
                                    + " по номеру +996222222222")


@bot.message_handler(commands=["reg"])
def user_reg(message):
    user_dict.clear()
    orders.clear()
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Sushi Room')
    itembtn2 = types.KeyboardButton('Ocak Kebap')
    itembtn3 = types.KeyboardButton("Nathan's")

    markup.add(itembtn1, itembtn2, itembtn3)

    msg = bot.send_message(chat_id, "Откуда закажем?", reply_markup=markup)
    bot.register_next_step_handler(msg, check_cafe)


def check_cafe(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id, "Отлично! Ваше имя пожалуйста")

    place = {"restaurant": text}
    user_dict.update(place)
    print(user_dict)
    if text == "Sushi Room":
        bot.register_next_step_handler(msg, sushi_room)
    elif text == "Ocak Kebap":
        bot.register_next_step_handler(msg, ocak_kebap)
    elif text == "Nathan's":
        bot.register_next_step_handler(msg, nathan)


def sushi_room(message):
    chat_id = message.chat.id
    name = {"name": message.text}
    user_dict.update(name)
    print(user_dict)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("Унаги ролл")
    btn2 = types.KeyboardButton("Осака ролл")
    btn3 = types.KeyboardButton("Хот ролл")
    btn4 = types.KeyboardButton("Калифорния")
    btn5 = types.KeyboardButton("Филадельфия")
    btn6 = types.KeyboardButton("Удон с курицей")
    btn7 = types.KeyboardButton("Сок")
    btn8 = types.KeyboardButton("Айс ти")
    btn9 = types.KeyboardButton("Готово")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)

    msg = bot.send_message(message.chat.id, "Какие роллы будем заказывать?", reply_markup = markup)

    bot.register_next_step_handler(msg, check_food_sushi)


def ocak_kebap(message):
    chat_id = message.chat.id
    name = {"name": message.text}
    user_dict.update(name)
    print(user_dict)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("Шаурма с курицей")
    btn2 = types.KeyboardButton("Шаурма с говядиной")
    btn3 = types.KeyboardButton("Тавук донер")
    btn4 = types.KeyboardButton("Адана с йогуртом")
    btn5 = types.KeyboardButton("Ожак кофте")
    btn6 = types.KeyboardButton("Бейти кебаб")
    btn7 = types.KeyboardButton("Шашлык из курицы")
    btn8 = types.KeyboardButton("Шашлык на мангале")
    btn9 = types.KeyboardButton("Айс ти")
    btn10 = types.KeyboardButton("Айран")
    btn11 = types.KeyboardButton("Сок")
    btn12 = types.KeyboardButton("Кола")
    btn13 = types.KeyboardButton("Компот")
    btn14 = types.KeyboardButton("Фанта")
    btn15 = types.KeyboardButton("Готово")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)

    msg = bot.send_message(message.chat.id, "Что закажем?", reply_markup = markup)

    bot.register_next_step_handler(msg, check_food_kebap)


def nathan(message):
    chat_id = message.chat.id
    name = {"name": message.text}
    user_dict.update(name)
    print(user_dict)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("Супер чизбургер")
    btn2 = types.KeyboardButton("Чизбургер фреш")
    btn3 = types.KeyboardButton("Криспи чикен")
    btn4 = types.KeyboardButton("Чикен ролл")
    btn5 = types.KeyboardButton("Фиш ролл")
    btn6 = types.KeyboardButton("Манхэттен хот-дог")
    btn7 = types.KeyboardButton("Кола")
    btn8 = types.KeyboardButton("Айс ти")
    btn9 = types.KeyboardButton("Готово")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)

    msg = bot.send_message(message.chat.id, "Выберите блюдо", reply_markup = markup)

    bot.register_next_step_handler(msg, check_food_nathan)


def check_food_sushi(message):
    chat_id = message.chat.id
    if message.text != "Готово":
        orders.append(message.text)
        order = {"order": orders}
        user_dict.update(order)
        print(user_dict)

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Унаги ролл")
        btn2 = types.KeyboardButton("Осака ролл")
        btn3 = types.KeyboardButton("Хот ролл")
        btn4 = types.KeyboardButton("Калифорния")
        btn5 = types.KeyboardButton("Филадельфия")
        btn6 = types.KeyboardButton("Удон с курицей")
        btn7 = types.KeyboardButton("Сок")
        btn8 = types.KeyboardButton("Айс ти")
        btn9 = types.KeyboardButton("Готово")

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)

        msg = bot.send_message(chat_id, 'Что нибудь еще?', reply_markup = markup)
        bot.register_next_step_handler(msg, check_food_sushi)
    else:
        msg = bot.send_message(chat_id, "Ваш номер телефона, как в примере '996XXXXXX'")
        bot.register_next_step_handler(msg, process_phone_step)


def check_food_kebap(message):
    chat_id = message.chat.id
    if message.text != "Готово":
        orders.append(message.text)
        order = {"order": orders}
        user_dict.update(order)
        print(user_dict)

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Шаурма с курицей")
        btn2 = types.KeyboardButton("Шаурма с говядиной")
        btn3 = types.KeyboardButton("Тавук донер")
        btn4 = types.KeyboardButton("Адана с йогуртом")
        btn5 = types.KeyboardButton("Ожак кофте")
        btn6 = types.KeyboardButton("Бейти кебаб")
        btn7 = types.KeyboardButton("Шашлык из курицы")
        btn8 = types.KeyboardButton("Шашлык на мангале")
        btn9 = types.KeyboardButton("Айс ти")
        btn10 = types.KeyboardButton("Айран")
        btn11 = types.KeyboardButton("Сок")
        btn12 = types.KeyboardButton("Кола")
        btn13 = types.KeyboardButton("Компот")
        btn14 = types.KeyboardButton("Фанта")
        btn15 = types.KeyboardButton("Готово")

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)

        msg = bot.send_message(message.chat.id, "Еще что нибудь?", reply_markup = markup)

        bot.register_next_step_handler(msg, check_food_kebap)
    else:
        msg = bot.send_message(chat_id, "Ваш номер телефона, как в примере '996XXXXXX'")
        bot.register_next_step_handler(msg, process_phone_step)


def check_food_nathan(message):
    chat_id = message.chat.id
    if message.text != "Готово":
        orders.append(message.text)
        order = {"order": orders}
        user_dict.update(order)
        print(user_dict)

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Супер чизбургер")
        btn2 = types.KeyboardButton("Чизбургер фреш")
        btn3 = types.KeyboardButton("Криспи чикен")
        btn4 = types.KeyboardButton("Чикен ролл")
        btn5 = types.KeyboardButton("Фиш ролл")
        btn6 = types.KeyboardButton("Манхэттен хот-дог")
        btn7 = types.KeyboardButton("Кола")
        btn8 = types.KeyboardButton("Айс ти")
        btn9 = types.KeyboardButton("Готово")

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)

        msg = bot.send_message(message.chat.id, "Еще что нибудь?", reply_markup = markup)
        bot.register_next_step_handler(msg, check_food_nathan)
    else:
        msg = bot.send_message(chat_id, "Ваш номер телефона, как в примере '996XXXXXX'")
        bot.register_next_step_handler(msg, process_phone_step)


def process_phone_step(message):
    try:
        int(message.text)
        if message.text.startswith("996"):
            if len(message.text) == 12:
                chat_id = message.chat.id
                phone = {"phone": message.text}
                user_dict.update(phone)
                print(user_dict)
                msg = bot.send_message(chat_id, 'Ваш адрес')
                bot.register_next_step_handler(msg, process_address)
            else:
                raise Exception
        else:
            raise Exception
    except Exception:
        msg = bot.reply_to(message, 'Вы ввели что то другое. Пожалуйста введите номер телефона через 996. Длина номера должна быть равна 12 цифрам.')
        bot.register_next_step_handler(msg, process_phone_step)


def process_address(message):
    chat_id = message.chat.id
    address = {"address": message.text}
    user_dict.update(address)
    print(user_dict)
    i = user_dict.get("order")
    j = 0
    if len(i) == 1:
        n = i[j]
    else:
        for j in i:
            n = ", ".join(i)

    bot.send_message(chat_id, "Спасибо, Ваш заказ принят, для подтверждения заказа с Вами свяжется наш сотрудник\nВаш заказ:")
    bot.send_message(chat_id=chat_id, text=("Заведение: " + user_dict.get("restaurant") + "\nЗаказ: " + n
                                            + "\nИмя: " + user_dict.get("name") + "\nТелефон: " + user_dict.get("phone")
                                            + "\nАдрес: " + user_dict.get("address")))

    bot.send_message(chat_id="-477351712", text=("Заведение: " + user_dict.get("restaurant") + "\nЗаказ: " + n
                                            + "\nИмя: " + user_dict.get("name") + "\nТелефон: " + user_dict.get("phone")
                                            + "\nАдрес: " + user_dict.get("address")))


@bot.message_handler(content_types=["text"])
def send_help(message):
    bot.send_message(
        message.chat.id, 'О нас - /about\nРегистрация - /reg')


@bot.message_handler(content_types=["photo"])
def send_help_text(message):
    bot.send_message(message.chat.id, 'Напишите текст')


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)

# git add .
# git commit -m 'commit message'
# git push heroku master
