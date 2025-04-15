import telebot
import google.generativeai as genai
from translate import Translator
translator=Translator(to_lang="es")

BOT_TOKEN ="your_token_bot"
bot=telebot.TeleBot(BOT_TOKEN)

Api="your_API_Gemeni" 
model_name="gemini-2.0-flash"
genai.configure(api_key=Api)
model=genai.GenerativeModel(model_name)

@bot.message_handler(func=lambda message:True)
def chat(message):
    user_input=message.text
    response=model.generate_content(user_input)
    translation=translator.translate(response.text)
    bot.reply_to(message,translation)


bot.infinity_polling()
