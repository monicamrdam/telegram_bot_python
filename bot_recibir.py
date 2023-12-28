from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler,  Filters, CallbackContext

TOKEN= "Aquí tu Token del bot"

def notificaciones(update:Update, context: CallbackContext):
    update.message.reply_text("Recibi tu mensaje")



def main():
    updater = Updater(TOKEN)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(filters =Filters.text & ~Filters.update.edited_message, callback = notificaciones))

    updater.start_polling()


    updater.idle()



if __name__ == "__main__":
    main()