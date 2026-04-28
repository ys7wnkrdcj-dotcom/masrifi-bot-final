import telebot
from telebot import types
from flask import Flask, request

# التوكن من صورتك لـ BotFather
TOKEN = "8754037232:AAFMg0bDN6_9P_VMx0xhjV09TSSQzzhjPGs"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('🚀 سحب فرص مصرفي')
    btn2 = types.KeyboardButton('💳 شحن (بنكيلي/مصرفي)')
    btn3 = types.KeyboardButton('💰 سحب أرباح')
    btn4 = types.KeyboardButton('📞 تواصل مع الوكيل')
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(message.chat.id, "🇲🇷 مرحباً بك في بوت وكيل مصرفي المعتمد.\nتم تفعيل نظام سحب الفرص بنجاح.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == '🚀 سحب فرص مصرفي':
        bot.reply_to(message, "🔍 يتم الآن فحص الفرص المتاحة في موقع مصرفي المعتمد...\n🔗 الرابط الرسمي: https://www.masrfi.net")
    
    elif message.text == '💳 شحن (بنكيلي/مصرفي)':
        bot.reply_to(message, "لإتمام الشحن: أرسل الـ ID الخاص بك وصورة وصل التحويل (Bankily/Masrivi).")

@app.route('/', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "OK", 200

@app.route('/', methods=['GET'])
def index():
    return "Bot is active on GitHub!", 200
