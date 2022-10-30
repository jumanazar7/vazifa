
from aiogram import Bot, Dispatcher,executor,types
import logging
from keybords1 import startkey,buyurtma_berishkey,salatkey1,saonlar,pirog,pirog1,solatlars,salomt_ikki,suvlar,suvlar1
from TOKEN1 import TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def do_start(message: types.Message):
    msg = message.from_user.first_name
    await message.reply(f"Xush kelibsiz! {msg}", reply_markup=startkey)

@dp.message_handler(text= "📥 Savatcha")
async def do_buyirtma(message: types.Message):
    await message.reply("Baza qo'shilmagan!")

@dp.message_handler(text= "📦 Buyurtmalarim")
async def do_buyirtma(message: types.Message):
    await message.reply("Baza qo'shilmagan!")

@dp.message_handler(text="🛍 Buyurtma berish")
async def do_buyirtma(message: types.Message):
    await message.reply("Nimadan boshlaymiz?",reply_markup=buyurtma_berishkey)

@dp.message_handler(text="🥣Полезные сэты")
async def do_buyirtma1(message: types.Message):
    await message.reply("Kategoriyani tanlang",reply_markup=salatkey1)

@dp.message_handler(text="🍰Домашние десерты")
async def do_buyirtma1(message: types.Message):
    await message.reply("Kategoriyani tanlang",reply_markup=pirog)

@dp.message_handler(text="ПИРОГ")
async def do_buyirtma1(message: types.Message):
    await message.reply("Kategoriyani tanlang",reply_markup=pirog1)
sss1 = """ТВОРОЖНЫЙ ПИРОГ
Narx: 12000.0 so'm

ЦЕНА  УЧЕТОМ ПОСУДЫ"""
@dp.message_handler(text="ТВОРОЖНЫЙ ПИРОГ")
async def do_buyirtma1(message: types.Message):
    await message.answer_photo(photo="https://avatars.dzeninfra.ru/get-zen_doc/50840/pub_5bcb39fc3491a600a9656ce7_5bcb3c4c9989ff00ae41472c/scale_1200",caption = sss1, reply_markup=saonlar)

@dp.message_handler(text="БЫСТРЫЙ ЛАНЧ")
async def do_buyirtma1(message: types.Message):
    await message.reply("Kategoriyani tanlang",reply_markup=salatkey1)
s2 = """ПРЕМИУМ 
Narx: 75900.0 so'm

СТЕЙК  ИЗ СЕМГИ 130 ГР  СЫРОМ ВИДЕ, БРОККОЛИ ОТВАРНЫЕ 100Г, ЛИМОН 30Г, САЛАТ ДНЯ 120Г, ХЛЕБ ЧЕРНЫЙ 2Ш"""

s3 = """Pepsi 0.5 L
Narx: 6000.0 so'm

Характеристики Напиток безалкогольный сильногазированный Pepsi п/бут 0.5л."""

s4 = """Coca-Cola 0.5 L
Narx: 6500.0 so'm

Характеристики Напиток безалкогольный сильногазированный Cola Holiday п/бут 1.5л."""

@dp.message_handler(text="ПРЕМИУМ")
async def do_buyirtma1(message: types.Message):
    await message.answer_photo(photo="https://kedem.ru/photo/articles/2018/11/gorbusha-na-skovorode.jpg",caption = s2, reply_markup=saonlar)

@dp.message_handler(text ="◀️ Orqaga")
async def do_bsoh(message: types.Message):
    await message.reply("Kategoriyani tanlang",reply_markup=startkey)

@dp.message_handler(text = "🥦 Свежие салаты")
async def do_bsoh(message: types.Message):
    await message.reply("Kategoriyani tanlang",reply_markup=solatlars)

@dp.message_handler(text = "СВЕЖИЙ САЛАТ")
async def do_bsoh(message: types.Message):
    await message.reply("Kategoriyani tanlang",reply_markup=salomt_ikki)

sss2 = """Achchiq-Chuchuk
Narx: 10000.0 so'm

Lorem Ipsum"""

@dp.message_handler(text = "Achchiq-Chuchuk")
async def do_bsoh(message: types.Message):
    await message.answer_photo(photo="https://pigmine.ru/wp-content/uploads/3/4/b/34b7716d44a9c096ee95ea1ff82ee060.jpeg",caption = sss2, reply_markup=saonlar)

@dp.message_handler(text = "🥤 Напитки")
async def do_bsoh(message: types.Message):
    await message.reply("Kategoriyani tanlang",reply_markup=suvlar)

@dp.message_handler(text = "Gazlangan")
async def do_bsoh(message: types.Message):
    await message.reply("Kategoriyani tanlang",reply_markup=suvlar1)

@dp.message_handler(text="Pepsi 0.5 L")
async def do_buyirtma1(message: types.Message):
    await message.answer_photo(photo="https://shashli-chok.ru/wp-content/uploads/2022/07/23758330.jpg",caption = s3, reply_markup=saonlar)

@dp.message_handler(text="Coca-Cola 0.5 L")
async def do_buyirtma1(message: types.Message):
    await message.answer_photo(photo="https://шашлык-сити.рф/wp-content/uploads/2021/07/4a5c4aee105d40b9b8e3325ed3cdbbbc.jpg",caption = s4, reply_markup=saonlar)
s5 = """Семейное кафе.

Режим работы: Harkuni, 10:00 - 21:00 

Жалобы и предложения: @qodirberganov06 , +998 77 007 79 51

Доставка осуществляется по всему городу"""

@dp.message_handler(text="Manzil")
async def do_buyirtma1(message: types.Message):
    await message.answer_photo(photo="https://sgastronomy.ru/wp-content/uploads/2021/08/2-2.jpg",caption = s5, reply_markup=startkey)

@dp.message_handler()
async def nima(message: types.Message):
    await message.reply("Mahsulot topilmadi!")

if __name__ == "__main__": 
    executor.start_polling(dp,skip_updates=True) 

