from config import TOKEN 
import logging 
from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from aiogram.types import Message, CallbackQuery

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("<b>🇺🇿 Tilni Tanlang! \n🇷🇺 Выберите Язык!</b>",parse_mode="HTML",reply_markup=til)

# Til uchun
@dp.message_handler(text="🇺🇿 O'zbekcha")
async def uzbek(message: types.Message):
    await message.answer("<b> Iltimos telefon raqamingizni yuboring!...👇</b>",parse_mode="HTML",reply_markup=con)

# raqam lokatsiya 
@dp.message_handler(content_types=["contact"])
async def uzbek(message):
    print(message.from_user.first_name)
    print(message.contact.phone_number)
    await message.answer("<b> Manzilingizni yuboring !?👇👇👇</b>",parse_mode="HTML",reply_markup=loc) #reply_markup=ism

# lokatsiya 
@dp.message_handler(content_types=["location"])
async def uzbek(message):
    print(message.location)
    await message.answer("<b> Ajoyib! Birgalikda buyurtma beramizmi?👇👇👇</b>",parse_mode="HTML",reply_markup=menyu) #reply_markup=ism


# Buyurtma uchun
@dp.message_handler(text="🍽Menu")
async def menu_uchun(message: types.Message):
    
    await message.answer("<b> Iltimos mahsulotlardan birini tanglang 😊 </b>",parse_mode='HTML',reply_markup=menu)

@dp.message_handler(text="⬅️ Orqaga")
async def menu_uchun(message: types.Message):
    
    await message.answer("<b>🇺🇿 Tilni Tanlang! \n🇷🇺 Выберите Язык!</b>",parse_mode='HTML',reply_markup=til)

#Lavash_menu_uchun
## tovuq
@dp.callback_query_handler(text="lavash")
async def bosh_menu(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu1)
@dp.callback_query_handler(text="tovuq")
async def bosh_menu(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang...",reply_markup=menu2)
@dp.callback_query_handler(text="tovuq1")
async def bosh_menu(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuq1.jpg", "rb"),
        caption="""Narxi 18000 so'm \nTarkibi:  Xamir, tovuq go`sht, chips, pomidor, bodring, sous, ko'katlar mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson)
    await call.message.delete()

@dp.callback_query_handler(text="tovuq2")
async def bosh_menu(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/tovuq1.jpg", "rb"),
        caption="""Narxi 20000 so'm \nTarkibi:  Xamir, tovuq go`sht, chips, pomidor, bodring, sous, ko'katlar, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson)
    await call.message.delete()

### gusht
@dp.callback_query_handler(text="gusht")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu3)
@dp.callback_query_handler(text="gusht1")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/mol1.jpg", "rb"),
        caption="""Narxi 21000 so'm \nTarkibi:  Xamir, Mol go`sht, chips, pomidor, bodring, sous, ko'katlar, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson1)
    await call.message.delete()

@dp.callback_query_handler(text="gusht2")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/mol1.jpg", "rb"),
        caption="""Narxi 23000 so'm \nTarkibi:  Xamir, Mol go`sht, chips, pomidor, bodring, sous, ko'katlar, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson1)
    await call.message.delete()

### sir
@dp.callback_query_handler(text="sir")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu4)
@dp.callback_query_handler(text="sir1")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/.jpg", "rb"),
        caption="""Narxi 19000 so'm \nTarkibi:  Xamir, Pishloq, Mol go`sht, chips, pomidor, bodring, sous, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson2)
    await call.message.delete()

@dp.callback_query_handler(text="sir2")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/.jpg", "rb"),
        caption="""Narxi 23000 so'm \nTarkibi:  Xamir, Pishloq, Mol go`sht, chips, pomidor, bodring, sous, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson2)
    await call.message.delete()

## tandir
@dp.callback_query_handler(text="tandir")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu5)
@dp.callback_query_handler(text="tandir1")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/.jpg", "rb"),
        caption="""Narxi 25000 so'm \nTarkibi:  Xamir, Qo'y go'shti, Mol go`sht, chips, pomidor, bodring, sous, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson3)
    await call.message.delete()    

@dp.callback_query_handler(text="tandir2")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/.jpg", "rb"),
        caption="""Narxi 28000 so'm \nTarkibi:  Xamir, Qo'y go'shti, Mol go`sht, chips, pomidor, bodring, sous, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson3)
    await call.message.delete()


####################

#hot_dog_uchun

@dp.callback_query_handler(text="hot")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Turini Tanlang...",reply_markup=menuhot)

@dp.callback_query_handler(text="hot1")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/korolevskiy.jpg", "rb"),
        caption="""Narxi 10000 so'm \nTarkibi:  Bulochka, Ketchup, Sosiska, chips, pomidor, bodring, sous, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson4)
    await call.message.delete()

@dp.callback_query_handler(text="hot2")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/classic.jpg", "rb"),
        caption="""Narxi 15000 so'm \nTarkibi:  Bulochka, Ketchup, Double Sosiska, chips, pomidor, bodring, sous, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson4)
    await call.message.delete()

#PIZZA 

@dp.callback_query_handler(text="pizza")
async def bosh_menu3(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu6)

@dp.callback_query_handler(text="mar")
async def bosh_menu3(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/margarita.jpg", "rb"),
        caption="""Narxi: 65000 so'm \nTarkibi:  Maxsus italyancha qizil sous, kolbasa, pomidor, mosarella va gauda pishloqlarining mayin mazasi bilan rayhon barglari uyg'unligi. \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson5)
    await call.message.delete()

@dp.callback_query_handler(text="pep")
async def bosh_menu3(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/pepperoni.jpg", "rb"),
        caption="""Narxi: 70000 so'm \nTarkibi:  Maxsus italyancha qizil sous, sosiska, pomidor, mosarella va gauda pishloqlarining mayin mazasi bilan rayhon barglari uyg'unligi. \nIltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson5)
    await call.message.delete()

#KFC

@dp.callback_query_handler(text="kfc")
async def bosh_menu4(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu7)

@dp.callback_query_handler(text="bas")
async def bosh_menu4(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/sanders.jpg", "rb"),
        caption="""Narxi: 25000 so'm \nTarkibi:  Tovuq oyoqchalari, qalampir, sous \nIltimos kerakli bo'lgan miqdorni tanlang...""", reply_markup=menuson6)
    await call.message.delete()

@dp.callback_query_handler(text="san")
async def bosh_menu4(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/basket.jpg", "rb"),
        caption="""Narxi: 30000 so'm \nTarkibi:  Tovuq oyoqchalari, kartoshka, qalampir, sous \nIltimos kerakli bo'lgan miqdorni tanlang...""", reply_markup=menuson6)
    await call.message.delete()

#CLUB SANDWICH

@dp.callback_query_handler(text="sendwich")
async def bosh_menu5(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu8)

@dp.callback_query_handler(text="set1")
async def bosh_menu5(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/club2.jpg", "rb"),
        caption="""Narxi: 15000 so'm \nTarkibi:  Bekon, non, pomidor, tovuq go'shti, pishloq, bodring, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""", reply_markup=menuson7)
    await call.message.delete()

@dp.callback_query_handler(text="set5")
async def bosh_menu5(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/club1.jpg", "rb"),
        caption="""Narxi: 18000 so'm \nTarkibi:  Bekon, non, pomidor, kurka go'shti, pishloq, bodring, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...""", reply_markup=menuson7)
    await call.message.delete()

#DONAR

@dp.callback_query_handler(text="donar")
async def bosh_menu6(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu9)

@dp.callback_query_handler(text="donar1")
async def bosh_menu6(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/donar1.jpg", "rb"),
        caption="""Narxi: 25000 so'm \nTarkibi:  Guruch, non, tovuq go'shti \nIltimos kerakli bo'lgan miqdorni tanlang...""", reply_markup=menuson8)
    await call.message.delete()

@dp.callback_query_handler(text="donar2")
async def bosh_menu6(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/donar2.jpg", "rb"),
        caption="""Narxi: 30000 so'm \nTarkibi:  Guruch, non, mol go'shti \nIltimos kerakli bo'lgan miqdorni tanlang...""", reply_markup=menuson8)
    await call.message.delete()

#DESERT

@dp.callback_query_handler(text="dessert")
async def bosh_menu7(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu10)

@dp.callback_query_handler(text="fruitcake")
async def bosh_menu7(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/fruitcake.jpg", "rb"),
        caption="""Narxi: 13000 so'm \nTarkibi:  Biskvit xamiri, mevalar, krem \nIltimos kerakli bo'lgan miqdorni tanlang...""", reply_markup=menuson9)
    await call.message.delete() 

@dp.callback_query_handler(text="cheesecake")
async def bosh_menu7(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/cheesecake.jpg", "rb"),
        caption="""Narxi: 15000 so'm \nTarkibi:  Biskvit xamiri, pishloq, o'rmon mevalari, krem \nIltimos kerakli bo'lgan miqdorni tanlang...""", reply_markup=menuson9)
    await call.message.delete()

@dp.callback_query_handler(text="choco")
async def bosh_menu7(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/choco.jpg", "rb"),
        caption="""Narxi: 12000 so'm \nTarkibi:  Biskvit xamiri, shokolad, krem, kakao \nIltimos kerakli bo'lgan miqdorni tanlang...""", reply_markup=menuson9)
    await call.message.delete()

@dp.callback_query_handler(text="med")
async def bosh_menu7(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/med.jpg", "rb"),
        caption="""Narxi: 14000 so'm \nTarkibi:  Xamir, asal, krem \nIltimos kerakli bo'lgan miqdorni tanlang...""", reply_markup=menuson9)
    await call.message.delete()



# ICHIMLIKLAR

@dp.callback_query_handler(text="ichimliklar")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Iltimos ichimlik turini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="choy")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="kofe")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu3)


@dp.callback_query_handler(text="americano")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/americano.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik americano \nNarxi: 6 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)
    await call.message.delete()

@dp.callback_query_handler(text="capuchino")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/cappuccino.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik cappuchino \nNarxi: 7 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)
    await call.message.delete()

@dp.callback_query_handler(text="3v1")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/3v1.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik 3v1 coffee \nNarxi: 5 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)
    await call.message.delete()   
 
@dp.callback_query_handler(text="latte")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/latte.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik latte \nNarxi:8 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)
    await call.message.delete()

@dp.callback_query_handler(text="sok")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)

@dp.callback_query_handler(text="choylar")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu10)

@dp.callback_query_handler(text="yaxna")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)

@dp.callback_query_handler(text="kuk")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/green.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik ko'k choy \nNarxi: 5 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu6)
    await call.message.delete()

@dp.callback_query_handler(text="qora")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/black.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik qora choy \nNarxi: 5 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu6)
    await call.message.delete()

@dp.callback_query_handler(text="limon")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/limon.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik limon choy \nNarxi: 7 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu6)
    await call.message.delete()

@dp.callback_query_handler(text="fanta")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/fanta.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik Fanta \nNarxi: 13 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu11)
    await call.message.delete()

@dp.callback_query_handler(text="pepsi")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/pepsi.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik Pepsi \nNarxi: 12 000 \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu12)
    await call.message.delete()

@dp.callback_query_handler(text="cola")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/cola.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik Coca Cola \nNarxi: 13 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu13)
    await call.message.delete()

@dp.callback_query_handler(text="sprite")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/sprite.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik Sprite \nNarxi: 13 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu14)
    await call.message.delete()

@dp.callback_query_handler(text="mojito")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/mojito.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik Mojito fresh \nNarxi: 15 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu15)
    await call.message.delete()

@dp.callback_query_handler(text="meva")
async def suv(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/bliss.jpg", "rb"),
        caption="""<b>Hurmatli mijoz siz tanlagan ichimlik Bliss mevali soki \nNarxi: 13 000 so'm \nIltimos sonini tanlang</b>""",parse_mode = 'HTML',reply_markup = ichimlik_menyu16)
    await call.message.delete()

#Ichimlik Backlar

@dp.callback_query_handler(text="orqaga5")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = menu)

@dp.callback_query_handler(text="orqaga6")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="orqaga7")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="orqaga10")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu3)

@dp.callback_query_handler(text="orqaga13")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="orqaga11")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu10)

@dp.callback_query_handler(text="orqaga8")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)


@dp.callback_query_handler(text="orqaga12")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)


@dp.callback_query_handler(text="orqaga9")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="orqaga14")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)

@dp.callback_query_handler(text="orqaga15")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)

@dp.callback_query_handler(text="orqaga16")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)

@dp.callback_query_handler(text="orqaga17")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)

@dp.callback_query_handler(text="orqaga18")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)

@dp.callback_query_handler(text="orqaga19")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)

@dp.callback_query_handler(text="orqaga20")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoriyani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)

################# BACKLAR ########################

@dp.callback_query_handler(text="back01")
async def ortga1(call: CallbackQuery):
    await call.message.answer(f"<b>Iltimos mahsulotlardan birini tanglang 😊</b>", parse_mode="HTML",reply_markup=menu)

@dp.callback_query_handler(text="back1")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu)

@dp.callback_query_handler(text="back2")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu1)

@dp.callback_query_handler(text="back2")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu2)

@dp.callback_query_handler(text="back3")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu2)

##
@dp.callback_query_handler(text="back4")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu1)

@dp.callback_query_handler(text="back4")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu3)

@dp.callback_query_handler(text="back5")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu3)

##
@dp.callback_query_handler(text="back6")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu1)

@dp.callback_query_handler(text="back6")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu4)

@dp.callback_query_handler(text="back7")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu4)
##
@dp.callback_query_handler(text="back8")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu1)


@dp.callback_query_handler(text="back8")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu5)

@dp.callback_query_handler(text="back9")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu5)

########### HOT DOG BACK ############## #####

@dp.callback_query_handler(text="back10")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu)

@dp.callback_query_handler(text="back11")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menuhot)

################ PIZZA BACK ##################

@dp.callback_query_handler(text="back12")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu)

@dp.callback_query_handler(text="back13")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu6)


################ KFC BACK ########################

@dp.callback_query_handler(text="back14")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu)

@dp.callback_query_handler(text="back15")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu7)


############## CLUBSANDWICH BACK ##############

@dp.callback_query_handler(text="back16")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu)

@dp.callback_query_handler(text="back17")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu8)


################ DONAR BACK #######################

@dp.callback_query_handler(text="back18")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu)

@dp.callback_query_handler(text="back19")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu9)


################ DESSERT BACK ####################

@dp.callback_query_handler(text="back20")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu)

@dp.callback_query_handler(text="back21")
async def ortga1(call: CallbackQuery):
    await call.message.answer("Turini Tanlang....",reply_markup=menu10)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)