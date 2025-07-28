# 🎥 YouTube Downloader Telegram Bot

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://core.telegram.org/bots)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

بات تلگرام ساده و کارآمد برای دانلود ویدیوهای یوتیوب به صورت MP4

## ✨ ویژگی‌ها

- 📥 دانلود مستقیم ویدیوهای یوتیوب در فرمت MP4
- 🚀 سرعت دانلود بالا با yt-dlp
- 🤖 رابط کاربری ساده در تلگرام
- 🔄 دکمه ریستارت آسان (meow)
- 🗑️ حذف خودکار فایل‌ها بعد از ارسال (صرفه‌جویی در فضا)
- ⚡ پردازش ناهمزمان و پاسخ‌گویی سریع
- 🛡️ مدیریت خطاها با پیام‌های کاربرپسند

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها

- Python 3.7 یا بالاتر
- اتصال به اینترنت

### نصب

1. **کلون کردن پروژه:**
```bash
git clone https://github.com/mobimiyo/youtube-dowloader.git
cd youtube-dowloader
```

2. **نصب کتابخانه‌های مورد نیاز:**
```bash
pip install pyTelegramBotAPI yt-dlp
```

3. **دریافت Bot Token:**
   - به [@BotFather](https://t.me/BotFather) در تلگرام مراجعه کنید
   - یک بات جدید بسازید: `/newbot`
   - نام و username برای بات انتخاب کنید
   - Token دریافتی را در فایل `ubot.py` جایگزین کنید:
   ```python
   TOKEN = "YOUR_BOT_TOKEN_HERE"
   ```

4. **اجرای بات:**
```bash
python ubot.py
```

## 📖 نحوه استفاده

### شروع کار
1. بات را در تلگرام پیدا کنید (username که به BotFather دادید)
2. دستور `/start` را بزنید
3. لینک ویدیو یوتیوب را ارسال کنید
4. منتظر دانلود و دریافت ویدیو باشید

### دستورات و ویژگی‌ها
- **`/start`** - شروع کار با بات و نمایش کیبورد
- **لینک یوتیوب** - دانلود مستقیم ویدیو
- **دکمه `meow`** - ریستارت بات برای دانلود جدید

### مثال استفاده
```
کاربر: /start
بات: سلام! لینک ویدیو رو بفرست تا برات دانلودش کنم

کاربر: https://www.youtube.com/watch?v=example
بات: در حال دانلود ویدیو... بصبر ⏳
بات: [ارسال ویدیو]
بات: ✅ دانلود انجام شد!
     برای restart روی meow کلیک کنید.
```

## 🛠️ جزئیات فنی

### کتابخانه‌های استفاده شده
- **`pyTelegramBotAPI`** - کتابخانه بات تلگرام
- **`yt-dlp`** - ابزار قدرتمند دانلود از یوتیوب
- **`os`** - مدیریت فایل‌ها و پوشه‌ها
- **`glob`** - جستجو در فایل‌ها

### ساختار کد
```python
# تنظیمات اولیه بات
TOKEN = "YOUR_TOKEN"
bot = telebot.TeleBot(TOKEN)

# تابع دانلود ویدیو
def download_video(url, save_path='downloads')

# هندلر شروع کار
@bot.message_handler(commands=['start'])

# هندلر ریستارت
@bot.message_handler(func=lambda message: message.text.lower() == "meow")

# هندلر دانلود
@bot.message_handler(func=lambda message: True)
```

## ⚙️ تنظیمات

### مسیر دانلود
```python
save_path='downloads'  # پوشه ذخیره فایل‌ها
```

### فرمت خروجی
```python
'format': 'mp4'  # فرمت ویدیو خروجی
```

### الگوی نام‌گذاری فایل
```python
'outtmpl': f'{save_path}/%(title)s.%(ext)s'
```

## 📁 ساختار پروژه

```
youtube-dowloader/
├── ubot.py              # فایل اصلی بات
├── downloads/           # پوشه دانلود (ایجاد خودکار)
├── README.md
└── requirements.txt
```

## 📋 requirements.txt

```txt
pyTelegramBotAPI==4.14.0
yt-dlp>=2023.1.6
```

## 🔧 سفارشی‌سازی

### تغییر فرمت دانلود
```python
ydl_opts = {
    'format': 'best[height<=720]',  # حداکثر 720p
    # یا
    'format': 'bestaudio',          # فقط صوت
}
```

### اضافه کردن محدودیت حجم
```python
ydl_opts = {
    'format': 'best[filesize<50M]',  # حداکثر 50 مگابایت
}
```

## ⚠️ نکات مهم

- **امنیت**: Token خود را در کد قرار ندهید، از متغیر محیطی استفاده کنید
- **حریم خصوصی**: فقط از محتوای عمومی و قانونی استفاده کنید
- **حجم فایل**: ویدیوهای بزرگ ممکن است در ارسال با مشکل مواجه شوند
- **سرور**: برای استفاده دائمی، بات را روی سرور اجرا کنید

## 🔒 امنیت Token

برای امنیت بیشتر، Token را در فایل جداگانه یا متغیر محیطی قرار دهید:

```python
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
```

## 🐛 عیب‌یابی

### مشکلات رایج:
- **خطای Token**: Token صحیح را از BotFather دریافت کنید
- **خطای دانلود**: اتصال اینترنت و صحت لینک را بررسی کنید
- **خطای ارسال**: حجم فایل ممکن است زیاد باشد

## 🤝 مشارکت

1. Fork کنید
2. Branch جدید بسازید: `git checkout -b feature/new-feature`
3. تغییرات را Commit کنید: `git commit -m 'Add new feature'`
4. Push کنید: `git push origin feature/new-feature`
5. Pull Request بزنید

## 📄 مجوز

این پروژه تحت مجوز MIT منتشر شده است.

## 🙏 تشکر

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - برای کتابخانه دانلود قدرتمند
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - برای API تلگرام

---

⭐ اگر این پروژه برایتان مفید بود، یک star بدهید!

**نکته امنیتی**: لطفاً Token واقعی خود را در کد عمومی قرار ندهید! 🔐

