import telebot
import openai
from telebot import types

token = 'TOKEN'
openai_token = 'TOKEN'

bot = telebot.TeleBot(token)
openai.api_key = openai_token

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')

@bot.message_handler(commands=['ask'])
def ask(message):
    text = message.text[4:]

    prompt = [{'role': 'user', 'content': text}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt
    )

    bot.send_message(message.chat.id, f"{response['choices'][0]['message']['content']}")

bot.infinity_polling()
