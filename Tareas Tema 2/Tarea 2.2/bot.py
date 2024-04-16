import logging
import re
import datetime
import random

from telegram import ForceReply, Update # type: ignore
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters # type: ignore

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Expresiones regulares
saludo_expresion_regular = re.compile(r"hello|hi|hey|hola", re.IGNORECASE)
hora_expresion_regular = re.compile(r"hora|time", re.IGNORECASE)
chiste_expresion_regular = re.compile(r"chiste|broma|joke", re.IGNORECASE)
gratitud_expresion_regular = re.compile(r"gracias|thank you", re.IGNORECASE)
bien_expresion_regular = re.compile(r"bien|good", re.IGNORECASE)
mal_expresion_regular = re.compile(r"mal|bad", re.IGNORECASE)
conversion_expresion_regular = re.compile(r"(\d+(?:\.\d+)?)\s*pulgadas", re.IGNORECASE)

# Factores de conversión de pulgadas a centímetros
factor_pulgadas_a_cm = 2.54

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches any regular expression."""
    message_text = update.message.text

    if saludo_expresion_regular.search(message_text):
        await update.message.reply_text("¿Cómo estás?")

    elif hora_expresion_regular.search(message_text):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        await update.message.reply_text(f"La hora actual es {current_time}.")

    elif chiste_expresion_regular.search(message_text):
        joke = random.choice(["¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
                              "¿Qué le dice un jardinero a otro jardinero? ¡Estamos sembrados!",
                              "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
                              "¿Cómo se dice 'pez' en inglés? ¡Fish!",
                              "¿Qué le dice una iguana a su hermana gemela? ¡Iguanita!"])
        await update.message.reply_text(joke)

    elif gratitud_expresion_regular.search(message_text):
        await update.message.reply_text("¡De nada! Si necesitas ayuda con algo más, no dudes en preguntar.")

    elif bien_expresion_regular.search(message_text):
        await update.message.reply_text("¡Qué bien!")

    elif mal_expresion_regular.search(message_text):
        await update.message.reply_text("¡Qué mal!")

    elif conversion_expresion_regular.search(message_text):
        match = conversion_expresion_regular.search(message_text)
        pulgadas = float(match.group(1))
        centimetros = pulgadas * factor_pulgadas_a_cm
        await update.message.reply_text(f"{pulgadas} pulgadas equivalen a {centimetros} centímetros.")

    else:
        await update.message.reply_text("No entendí tu mensaje.")

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("7193544779:AAH7WXRC1G8L4ohxZxtmcghJh8USHEzdfkM").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
