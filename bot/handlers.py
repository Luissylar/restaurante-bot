import json
from telegram import Update
from telegram.ext import CallbackContext

# Función para leer y formatear el archivo JSON con el menú
def get_menu() -> str:
    menu_file_path = 'data/menu.json'
    
    try:
        with open(menu_file_path, 'r', encoding='utf-8') as file:
            menu_data = json.load(file)
    except FileNotFoundError:
        return "El archivo del menú no se encuentra."
    except json.JSONDecodeError:
        return "Error al leer el archivo del menú."
    
    # Verificar que el menú tiene la estructura correcta
    if not isinstance(menu_data, dict):
        return "El formato del menú es incorrecto."
    
    # Formatear el contenido del menú de manera más legible
    menu_text = "📝 *Menú del Restaurante*\n\n"
    for category, items in menu_data.items():
        menu_text += f"📂 *{category}*\n"
        if not isinstance(items, list):
            menu_text += "Error: La categoría no contiene una lista de elementos.\n"
            continue
        for item in items:
            if not isinstance(item, dict):
                menu_text += "Error: Un elemento del menú no está en el formato correcto.\n"
                continue
            name = item.get("name", "Nombre no disponible")
            description = item.get("description", "Descripción no disponible")
            price = item.get("price", "Precio no disponible")
            menu_text += f"🔹 {name}: {description} - {price}\n"
        menu_text += "\n"
    
    return menu_text

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("¡Hola! Soy tu bot. ¿Cómo puedo ayudarte hoy? Puedes ver el menú con el comando /menu o contactarnos con el comando /contact.")

async def menu(update: Update, context: CallbackContext) -> None:
    menu_text = get_menu()
    await update.message.reply_text(menu_text, parse_mode='Markdown')

async def contact(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("📧 Contáctanos en Luigis@restaurante.pe. ¡Estamos aquí para ayudarte!")
