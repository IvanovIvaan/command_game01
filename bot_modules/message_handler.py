
# from .create_bot import bot

from aiogram.filters import CommandStart
from .create_dispatcher import dispatcher
from aiogram.types import Message

@dispatcher.message(CommandStart())
async def bot_start(message: Message):
    await message.answer(text = "Привіт користувач")