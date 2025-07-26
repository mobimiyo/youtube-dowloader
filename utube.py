import telebot
import yt_dlp
import os
import glob
TOKEN = "8490159393:AAHaCa8OToCqyBjZ81CqW4gchzg-Y6QJ340"
bot = telebot.TeleBot(TOKEN)

# 🎯 تابع دانلود ویدیو از یوتیوب
def download_video(url, save_path='downloads'):
	if not os.path.exists(save_path):
		os.makedirs(save_path)

	ydl_opts = {
		'outtmpl': f'{save_path}/%(title)s.%(ext)s',
		'format': 'mp4',
	}
	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=True)
		filename = ydl.prepare_filename(info)

		return filename


# 📩 پاسخ به دستور /start
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    meow_button = KeyboardButton("meow")
    markup.add(meow_button)
    bot.send_message(message.chat.id, "سلام! لینک ویدیو رو بفرست تا برات دانلودش کنم", reply_markup=markup)

# هندلر برای پیام meow (ریست بات)
@bot.message_handler(func=lambda message: message.text and message.text.lower() == "meow")
def handle_meow(message):
    bot.send_message(message.chat.id, "برای دانلود های بیشتر  start  را بزنید⏳")
    # اینجا می‌تونی کد ریست بات یا راه‌اندازی مجدد بذاری
    # مثلاً اگر برنامه‌ات ساختار خاصی داره، تابع ریست رو صدا بزن
    # برای نمونه، این فقط پیام می‌فرسته




# 📥 وقتی کاربر لینک فرستاد
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text.strip()

    bot.reply_to(message, "در حال دانلود ویدیو... بصبر ⏳")

    try:
        file_path = download_video(url)
        bot.send_video(message.chat.id, video=open(file_path, 'rb'))

        # ← اینجا پیام اضافه کن:
        bot.send_message(message.chat.id, "✅ دانلود انجام شد!\nبرای restart روی meow کلیک کنید.")

        os.remove(file_path)

    except Exception as e:
        bot.reply_to(message, f"❌ خطا در دانلود یا ارسال:\n{e}")




bot.infinity_polling()


