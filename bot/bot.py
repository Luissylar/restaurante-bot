from telegram.ext import Updater, CommandHandler
import config.settings as settings
import bot.handlers

def main():
    # Inicializar el Updater con el token del bot
    updater = Updater(token=settings.TOKEN, use_context=True)
    
    # Obtener el dispatcher para registrar los manejadores
    dp = updater.dispatcher

    # Agregar manejadores de comandos
    dp.add_handler(CommandHandler("start", bot.handlers.start))
    dp.add_handler(CommandHandler("menu", bot.handlers.menu))
    dp.add_handler(CommandHandler("contact", bot.handlers.contact))
    
    # Iniciar el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
