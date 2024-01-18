import telebot
from extensions import APIExeption, CurrencyConverter
from config import keys, TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать работу введите комманду в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nЧтобы увидет доступные валюты введите /values')
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIExeption('Неверное количество параметров')

        quote, base, amount = values

        total_base = CurrencyConverter.get_price(quote,base,amount)
    except APIExeption as e:
        bot.reply_to(message, f'Ошибка пользователя.\n {e}')
    except Exception as e:
        bot.reply_to(message,f'Что-то пошло не так... {e}')
    else:
        bot.reply_to(message, f'{amount} {keys[quote]} будет стоить {total_base} {keys[base]}')


bot.polling()

