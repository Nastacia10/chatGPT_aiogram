import openai
from aiogram import Bot, Dispatcher, executor, types
from config import OPENAI_API_KEY, TOKEN


openai.api_key = (OPENAI_API_KEY)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

async def on_startup(_):
    print('bot is running...')

HELP_COMMAND = """
/start - get started with the bot
"""

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.chat.id, f"Welcome to the smart search engine for a programmer. Ask any question in a message. The bot understands any language well, but we recommend making requests in English.")

@dp.message_handler(content_types=['text'])
async def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    await bot.send_message(message.chat.id, text=response['choices'][0]['text'])


if __name__ == '__main__':
   print('bot is running...!')
executor.start_polling(dp)