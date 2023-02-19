
import openai
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6099519998:AAGAwIe41-Vuk4XnKLkMt64iEuyiOyB7gj4'
openai.api_key = "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"


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Привет! Я бот с искусственным интеллектом. Чем я могу вам помочь?")

@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Я здесь, чтобы помочь вам с вашими вопросами. Просто напишите свои вопросы, и я сделаю все возможное, чтобы дать вам ответ.")

@dp.message_handler(content_types=['text'])
async def handle_text(message: types.Message):
    prompt = message.text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    reply = response["choices"][0]["text"]
    await bot.send_message(chat_id=message.chat.id, text=reply)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)