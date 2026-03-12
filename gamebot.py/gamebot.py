import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8712337321:AAES6a7S9oa4x9l_FgFm-7bX9Vpv0XEqKf4"

secret_number = random.randint(1,10)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Guess Game!\nGuess number between 1 and 10")

async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global secret_number
    try:
        user_number = int(update.message.text)

        if user_number == secret_number:
            await update.message.reply_text("Correct! You win!")
            secret_number = random.randint(1,10)

        elif user_number < secret_number:
            await update.message.reply_text("Too low")

        else:
            await update.message.reply_text("Too high")

    except:
        await update.message.reply_text("Send a number")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, guess))

app.run_polling()
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Guess numbers from 1-10")