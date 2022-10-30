from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
startkey = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Buyurtma berish")],
        [KeyboardButton(text="📦 Buyurtmalarim"),KeyboardButton(text="Manzil")]
    ],
    resize_keyboard=True
    
)
buyurtma_berishkey = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🥣Полезные сэты"),KeyboardButton(text="🍰Домашние десерты")],
        [KeyboardButton(text="🥦 Свежие салаты"),KeyboardButton(text="🥤 Напитки")],
        [KeyboardButton(text="📥 Savatcha"),KeyboardButton(text="◀️ Orqaga")],
    ],
    resize_keyboard = True
)

salatkey1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ПРЕМИУМ")],
        [KeyboardButton(text="📥 Savatcha"),KeyboardButton(text="◀️ Orqaga")],
    ],
    resize_keyboard=True
)
saonlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"),KeyboardButton(text="2"),KeyboardButton(text="3")],
        [KeyboardButton(text="4"),KeyboardButton(text="5"),KeyboardButton(text="6")],
        [KeyboardButton(text="7"),KeyboardButton(text="8"),KeyboardButton(text="9")],
        [KeyboardButton(text="📥 Savatcha"),KeyboardButton(text="◀️ Orqaga")],
    ],
    resize_keyboard = True
)
pirog = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ПИРОГ")],
        [KeyboardButton(text="📥 Savatcha"),KeyboardButton(text="◀️ Orqaga")],
    ],
    resize_keyboard=True
)
pirog1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ТВОРОЖНЫЙ ПИРОГ")],
        [KeyboardButton(text="📥 Savatcha"),KeyboardButton(text="◀️ Orqaga")],
    ],
    resize_keyboard=True
)
solatlars = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="СВЕЖИЙ САЛАТ"),KeyboardButton(text="Капустный")],
        [KeyboardButton(text="📥 Savatcha"),KeyboardButton(text="◀️ Orqaga")]
    ],
    resize_keyboard=True
)
salomt_ikki = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Achchiq-Chuchuk")],
        [KeyboardButton(text="📥 Savatcha"),KeyboardButton(text="◀️ Orqaga")],
    ],
    resize_keyboard=True
)
suvlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Gazlangan"),KeyboardButton(text="Gazlanmagan")],
        [KeyboardButton(text="📥 Savatcha"),KeyboardButton(text="◀️ Orqaga")]
    ],
    resize_keyboard=True
)
suvlar1 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Pepsi 0.5 L"),KeyboardButton(text="Coca-Cola 0.5 L")],
        [KeyboardButton(text="📥 Savatcha"),KeyboardButton(text="◀️ Orqaga")]
    ],
    resize_keyboard=True
)