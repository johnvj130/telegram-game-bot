import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Get bot token from environment variable
TOKEN = os.getenv("BOT_TOKEN")

# Store numbers for users
user_numbers = {}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    number = random.randint(1, 10)
    user_numbers[user_id] = number

    await update.message.reply_text(
        "Welcome to the Guessing Game!\n"
        "I picked a number between 1 and 10.\n"
        "Send a number to guess."
    )

# Guess handler
async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in user_numbers:
        await update.message.reply_text("Type /start to begin the game.")
        return

    try:
        user_guess = int(update.message.text)
    except:
        await update.message.reply_text("Send a number between 1 and 10.")
        return

    secret = user_numbers[user_id]

    if user_guess == secret:
        await update.message.reply_text("Correct! You win! 🎉\nType /start to play again.")
        del user_numbers[user_id]

    elif user_guess < secret:
        await update.message.reply_text("Too low. Try again.")

    else:
        await update.message.reply_text("Too high. Try again.")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - start the game\n"
        "Guess a number from 1 to 10."
    )

# Main function
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, guess))

    print("Bot is running...")
    app.run_polling()

# Run bot
if __name__ == "__main__":
    main()
