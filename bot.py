import telebot

TOKEN = "7519260088:AAFnR0Dx2PpTiE27c-TmWIw4tFWQXI81gJY"
bot = telebot.TeleBot(TOKEN)

COMMANDS = {
    'about': 'https://t.me/finansmost/26',
    'begin': 'https://t.me/finansmost/31',
    '2fa': 'https://t.me/finansmost/44',
    'verifikaciya': 'https://t.me/finansmost/41',
    'birga': 'https://t.me/finansmost/41',
    'p2p': 'https://t.me/finansmost/49',
    'portfel': 'https://t.me/finansmost/23',
    'moneti': 'https://t.me/finansmost/52',
    'strportfel': 'https://t.me/finansmost/55',
    'tools': 'https://t.me/finansmost/63'
}

@bot.message_handler(commands=list(COMMANDS.keys()))
def send_answer(message):
    command = message.text[1:]
    bot.send_message(message.chat.id, COMMANDS[command])

bot.polling()
