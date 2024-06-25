import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from transliterate import to_latin

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7240944660:AAE1M_eDe0yuNld7GoHbTzMst-Xx3lqvLF8"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"assolumu alaykum, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Matndagi so'zlarni tahlil qilib chiqib,matnni o'chirish kerak bo'lsa o'chiradi
    """
    try:
        #compare
        msgs = message.text.split()
        for msg in msgs:
            if msg.isascii():
                msg = msg.lower()
                if msg.startswith("https") or msg.startswith("@") or msg.startswith("toshkent") or msg.startswith("tashkent") or msg.startswith("xorazm"):
                    await message.delete()
                    break
            else:
                msg = to_latin(msg).lower()
                if msg.startswith("https") or msg.startswith("@") or msg.startswith("toshkent") or msg.startswith("tashkent")  or msg.startswith("xorazm"):
                    await message.delete()
                    break

    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Qayta urinib ko'ring!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())