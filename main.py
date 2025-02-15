import telebot
import random

bot = telebot.TeleBot('5991967053:AAFk-AuVEhYO4qUB7tn-9o_JPCQwU0HaimU')

# Список карт Таро
tarot_cards = ["Шут", "Маг", "Жрица", "Императрица", "Император", "Иерофант", "Влюбленные", "Колесница", "Сила", "Отшельник", "Колесо Фортуны", "Правосудие", "Повешенный", "Смерть", "Умеренность", "Дьявол", "Башня", "Звезда", "Луна", "Солнце", "Суд", "Мир", "Туз Кубков", "Двойка Кубков", "Тройка Кубков", "Четвёрка Кубков", "Пятёрка Кубков", "Шестёрка Кубков", "Семёрка Кубков", "Восьмёрка Кубков", "Девятка Кубков", "Десятка Кубков", "Паж Кубков", "Рыцарь Кубков", "Королева Кубков", "Король Кубков", "Туз Пентаклей", "Двойка Пентаклей", "Тройка Пентаклей", "Четвёрка Пентаклей", "Пятёрка Пентаклей", "Шестёрка Пентаклей", "Семёрка Пентаклей", "Восьмёрка Пентаклей", "Девятка Пентаклей", "Десятка Пентаклей", "Паж Пентаклей", "Рыцарь Пентаклей", "Королева Пентаклей", "Король Пентаклей", "Туз Мечей", "Двойка Мечей", "Тройка Мечей", "Четвёрка Мечей", "Пятёрка Мечей", "Шестёрка Мечей", "Семёрка Мечей", "Восьмёрка Мечей", "Девятка Мечей", "Десятка Мечей", "Паж Мечей", "Рыцарь Мечей", "Королева Мечей", "Король Мечей", "Туз Жезлов", "Двойка Жезлов", "Тройка Жезлов", "Четвёрка Жезлов", "Пятёрка Жезлов", "Шестёрка Жезлов", "Семёрка Жезлов", "Восьмёрка Жезлов", "Девятка Жезлов", "Десятка Жезлов", "Паж Жезлов", "Рыцарь Жезлов", "Королева Жезлов", "Король Жезлов"]

# Список советов
advice_list = ["Слушай своё сердце.", "Не торопись с решениями.", "Сегодня хороший день для новых начинаний.", "Отдохни — это тоже важно.", "Подумай о своих целях и стремлениях.", "Будь открыт к новым возможностям."]

# Список предсказаний
today_predictions = ["Сегодня вас ждёт успех в работе.", "День будет спокойным и приятным.", "Вы встретите человека, который вас вдохновит.", "Возможны небольшие трудности, но вы с ними справитесь.", "Сегодня хороший день для творчества.", "Ожидайте приятный сюрприз!"]

# Команда /start
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
        "Добро пожаловать! Вот список доступных команд:\n"
        "/help - список команд\n"
        "/tarot - вытащить карту Таро\n"
        "/advice - получить совет\n"
        "/today - предсказание на день")

# Команда /help
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id,
        "Список доступных команд:\n"
        "/start - начать работу с ботом\n"
        "/help - список команд\n"
        "/tarot - вытащить карту Таро\n"
        "/advice - получить случайный совет\n"
        "/today - предсказание на день")

# Команда /tarot
@bot.message_handler(commands=['tarot'])
def tarot_command(message):
    chosen_card = random.choice(tarot_cards)
    bot.send_message(message.chat.id, f"Ваша карта: *{chosen_card}*", parse_mode='Markdown')

# Команда /advice
@bot.message_handler(commands=['advice'])
def advice_command(message):
    bot.send_message(message.chat.id, random.choice(advice_list))

# Команда /today
@bot.message_handler(commands=['today'])
def today_command(message):
    bot.send_message(message.chat.id, random.choice(today_predictions))

bot.infinity_polling()