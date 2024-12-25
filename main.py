import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load TOKEN from environment variable
TOKEN = '7705585839:AAEgf-F-OMeKE5Dw_LwMITgQSVT_7wNFYDc'

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to VNHAX iOS HACK! Type /help to get started.")

# Help Command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available Commands:\n"
        "/start - Start the bot\n"
        "/help - Get help and commands\n"
        "/info - Learn about our iOS hacks\n"
        "/contact - Contact us at @Thesqd\n"
        "/channel - Join our channel: https://t.me/vnhaxiosindia"
    )

# Info Command
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "VNHAX provides safe and reliable BGMI iOS hacks. Compatible with iPhones & iPads!"
    )

# Contact Command
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Contact us at @Thesqd for purchases!")

# Channel Command
async def channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Join our official channel: https://t.me/vnhaxiosindia")

# Build Application
app = ApplicationBuilder().token(TOKEN).build()

# Add Command Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("info", info))
app.add_handler(CommandHandler("contact", contact))
app.add_handler(CommandHandler("channel", channel))

# Run the bot
if __name__ == '__main__':
    app.run_polling()
