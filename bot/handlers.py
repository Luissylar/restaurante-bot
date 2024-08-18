from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("¡Hola! Soy el bot del restaurante. Usa /menu para ver el menú.")

def menu(update: Update, context: CallbackContext):
    # Aquí puedes cargar el menú desde un archivo JSON o base de datos
    update.message.reply_text("Aquí está el menú del restaurante...")

def contact(update: Update, context: CallbackContext):
    update.message.reply_text("Puedes contactarnos al correo: contacto@restaurante.com")
