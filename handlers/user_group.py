from string import punctuation
from aiogram import F, types, Router
from aiogram.filters import Command, CommandStart, or_f

user_group_router = Router()

restricted_words = {'fuck', 'bitch', 'dick'}

def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))

@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
     if restricted_words.intersection(message.text.lower().split()):
        await message.answer(f"{message.from_user.username}, follow rules in chat")
        await message.delete()
        # await message.chat.ban(message.from_user_id)