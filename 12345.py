import telebot   # импорт.библиотеки

my_first_bot = telebot.TeleBot('')
# переменная = библиотека, класс(токен создаваемого бота)


@my_first_bot.message_handler(commands=['start'])    # M_h декоратор, который реагирует на сообщения
def start(message):  # def объявления функции
    answer = f'<b>Привет {message.from_user.first_name}</b>'   # вывод имени пользователя
    my_first_bot.send_message(message.chat.id, answer, parse_mode='html')
# три параметра /в какой чат отсылаем(сообщение>чат>айди)/текст/формат текста


@my_first_bot.message_handler()
def get_text(message):
    my_first_bot.send_message(message.chat.id, '<b>Приветик</b>', parse_mode='html')


my_first_bot.polling(none_stop=True)  # Запуск бота на выполнение
