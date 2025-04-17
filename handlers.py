from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboards as kb
router=Router()
@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Как дела?",reply_markup=kb.main)


@router.message(F.text=='help')
async def help_handler(message: Message):
    await message.answer('Я могу помочь с чем угодно! Напиши мне, что тебя интересует.',reply_markup=kb.main)

@router.message(F.text=='У меня все хорошо')
async def reply_handler(message: Message):
    await message.answer("Я рад слышать это!")

@router.message()  
async def unknown_handler(message: Message):
    await message.answer("Я тебя не понял.")
