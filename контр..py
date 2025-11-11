from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random
import datetime

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Привет 👋", "Помощь ❓"], ["Весёлое сообщение 😄", "Прощай 👋"], ["Случайное число 🎲", "Время ⏰"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привет! Я бот с кнопками. Выбери действие:", reply_markup=reply_markup
    )

# Команда /joke
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? Потому что Oct 31 == Dec 25!",
        "Какой язык программирования самый романтичный? Python — потому что у него есть сердца <3",
        "Почему Python стал таким популярным? Потому что он змеиный... нет, подожди...",
        "Что сказал один байт другому? Я тебя бит!",
        "Почему программист вышел из дома? Потому что ему надоели баги!"
    ]
    await update.message.reply_text(f"🤣 {random.choice(jokes)}")

# Команда /cat
async def cat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cat_faces = ["=^..^=", "(=🝦 ༝ 🝦=)", "/ᐠ｡ꞈ｡ᐟ\\\\", "ฅ/ᐠ.̫.ᐟ\\\\ฅ", "(=´∇｀=)"]
    await update.message.reply_text(f"Вот тебе котик: {random.choice(cat_faces)}")

# Ответ на текстовые сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "привет" in text:
        greetings = ["Привет! Рад тебя видеть 😎", "Здарова! 👋", "Приветствую тебя! ✨", "Хай! 😊"]
        await update.message.reply_text(random.choice(greetings))
    elif "помощь" in text:
        await update.message.reply_text("Вот что я умею:\n- Привет 👋\n- Весёлое сообщение 😄\n- Прощай 👋\n- Случайное число 🎲\n- Время ⏰\n\nТакже есть команды:\n/joke - случайная шутка\n/cat - показать котика")
    elif "весёлое" in text:
        await joke(update, context)
    elif "прощай" in text:
        farewells = ["Пока! 👋", "До скорой встречи! ✨", "Удачи! 🍀", "Бывай! 😊"]
        await update.message.reply_text(random.choice(farewells))
    elif "случайное" in text or "число" in text:
        number = random.randint(1, 100)
        await update.message.reply_text(f"🎲 Твое случайное число: {number}")
    elif "время" in text:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        await update.message.reply_text(f"⏰ Сейчас: {current_time}")
    elif "кот" in text or "котик" in text:
        await cat(update, context)
    elif "шутка" in text:
        await joke(update, context)
    else:
        responses = [
            "Я пока не понимаю это сообщение 🤔",
            "Попробуй выбрать что-то из меню! 📱",
            "Интересно... но я еще учусь! 📚",
            "Может, нажмешь одну из кнопок? 🔘"
        ]
        await update.message.reply_text(random.choice(responses))

# Основная функция запуска бота
def main():
    TOKEN = "8499759518:AAFRdF5dBgHoYaP_2Q3qx3E9r30x9gERY5I"  # Не забудь заменить на свой токен!

    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("joke", joke))
    app.add_handler(CommandHandler("cat", cat))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    print("🐱 Привет! Я бот с котиками и шутками!")
    app.run_polling()

if __name__ == "__main__":
    main()