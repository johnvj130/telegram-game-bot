import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

numbers = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id
    numbers[user] = random.randint(1,10)

    await update.message.reply_text(
        "Guess a number between 1 and 10"
    )

async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.id

    if user not in numbers:
        await update.message.reply_text("Type /start first")
        return

    try:
        g = int(update.message.text)
    except:
        await update.message.reply_text("Send a number")
        return

    n = numbers[user]

    if g == n:
        await update.message.reply_text("Correct!")
        del numbers[user]

    elif g < n:
        await update.message.reply_text("Too low")

    else:
        await update.message.reply_text("Too high")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, guess))

app.run_polling()
