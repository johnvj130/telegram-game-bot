import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8712337321:AAES6a7S9oa4x9l_FgFm-7bX9Vpv0XEqKf4"

# store user game data
games = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Guess Game\n"
        "Type /game to start a new game."
    )

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    number = random.randint(1, 10)
    games[user_id] = number

    await update.message.reply_text(
        "I picked a number between 1 and 10.\n"
        "Send your guess."
    )

async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    if user_id not in games:
        await update.message.reply_text("Start a game first using /game")
        return

    try:
        user_guess = int(update.message.text)
    except:
        await update.message.reply_text("Send a number.")
        return

    number = games[user_id]

    if user_guess == number:
        await update.message.reply_text("Correct! You win.")
        del games[user_id]

    elif user_guess < number:
        await update.message.reply_text("Too low. Try again.")

    else:
        await update.message.reply_text("Too high. Try again.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("game", game))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, guess))

app.run_polling()
