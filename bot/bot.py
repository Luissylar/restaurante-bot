import sys
import os

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import config.settings as settings
import bot.handlers

async def start(update: Update, context: CallbackContext) -> None:
    await bot.handlers.start(update, context)

async def menu(update: Update, context: CallbackContext) -> None:
    await bot.handlers.menu(update, context)

async def contact(update: Update, context: CallbackContext) -> None:
    await bot.handlers.contact(update, context)

def main():
    # Crear la aplicación con el token del bot
    application = Application.builder().token(settings.TOKEN).build()
    
    # Agregar manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("contact", contact))
    
    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
