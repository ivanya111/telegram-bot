import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

TOKEN = "8757516911:AAFtUG6Zfl5o7TDPjVyhuCdrgn07CJ9JkbU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Проверить цену")]],
    resize_keyboard=True
)

ITEM_NAME = "Sticker | Natus Vincere (Holo) | Shanghai 2024"

def get_price():
    url = "https://steamcommunity.com/market/priceoverview/"
    params = {
        "appid": 730,
        "currency": 18,
        "market_hash_name": ITEM_NAME
    }

    r = requests.get(url, params=params)
    data = r.json()

    if data.get("success"):
        return data.get("lowest_price", "Нет данных")
    return "Ошибка"

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Жми кнопку 👇", reply_markup=kb)

@dp.message(lambda message: message.text == "Проверить цену")
async def check_price(message: types.Message):
    price = get_price()
    await message.answer(f"💰 Цена: {price}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())