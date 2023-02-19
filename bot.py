import openai
import logging
from aiogram import Bot, Dispatcher, executor, types
from fastapi import FastAPI
import os


API_TOKEN = os.environ.get('TG_TOKEN')
openai.api_key = os.environ.get('OPENAI_TOKEN')

app = FastAPI()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Привет! Я бот с искусственным интеллектом. Чем я могу вам помочь?")

@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Я здесь, чтобы помочь вам с вашими вопросами. Просто напишите свои вопросы, и я сделаю все возможное, чтобы дать вам ответ.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)