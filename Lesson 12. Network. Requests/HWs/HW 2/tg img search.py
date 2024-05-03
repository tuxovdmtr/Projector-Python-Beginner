import requests
from  telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

token = "6898908138:AAGbcRDSmoqd-mKQf-0lWAIAy-3vwF4VchQ"
api_key = "FINmM5yMk9PykNRq7zr8sWZB7npAxagO"
chat_id = "395283227"
bot_username = "@GiphyImageSearchBot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Enter a word to search an image")

# Responses

def handle_responce(q: str) -> str:
    response = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={q}")
    dict = response.json()
    data = dict["data"]
    url_list = list()
    print(f"Here are {len(data)} {q} GIFs")
    for i in range(len(data)):
        #return "asd"
        url_list.append(data[i]["embed_url"])
    
    return(" ".join(url_list))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f"User {update.message.chat.id} in {message_type}: '{text}'")

    if message_type == "group":
        if bot_username in text:
            new_text = text.replace(bot_username, "").strip()
            response = handle_responce(new_text)
        else:
            return
    else:
        response = handle_responce(text)
    print("Bot:", response)
    await update.message.reply_text(response)

if __name__ == "__main__":
    print("Starting")
    app = Application.builder().token(token).build()
    #commands
    app.add_handler(CommandHandler("start", start_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("Polling...")
    app.run_polling(poll_interval=3)


#message = "Please enter a word to search a GIF for it."
#url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
#url = f"https://api.telegram.org/bot{token}/getUpdates"
#print(requests.get(url).json())
