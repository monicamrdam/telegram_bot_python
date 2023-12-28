from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler,  Filters, CallbackContext

TOKEN= "Aquí tu toquen del bot"
CHAT_ID ="Aquí el valor que te retorne print (update.message.chat.id)"

def echo (update: Updater, context: CallbackContext):
    print (update.message.chat.id)
    update.message.reply_text("<a href='https://oposicionestcae.es/'>Oposiciones TCAE </a>", parse_mode=ParseMode.HTML, reply_to_message_id=update.message.message_id)

    #Enviar imagenes desde nuestras carpetas
    update.message.reply_photo(open("C:\\Users\\monma\\Desktop\\Telegram_Bot\\tcaeEnAccion-remove.png","rb"))

    update.message.reply_audio(open("C:\\Users\\monma\\Desktop\\Telegram_Bot\\mario-bros_vida.mp3","rb"), title="Mario", reply_to_message_id=update.message.message_id, caption="Sonido de Mario.", thumb=open("C:\\Users\\monma\\Desktop\\Telegram_Bot\\mario_bros_14603.png","rb"))



def main():
    updater = Updater(TOKEN)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()


    updater.idle()



if __name__ == "__main__":
    main()