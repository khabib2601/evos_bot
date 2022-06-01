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
    await message.answer("<b> Ajoyib! Buyurtma berish uchun menyudan kerakli mahsulotni tanlang...👇</b>",parse_mode="HTML",reply_markup=menyu)


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
    await call.message.answer("Turini Tanlang....",reply_markup=menu1)
@dp.callback_query_handler(text="tovuq")
async def bosh_menu(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu2)
@dp.callback_query_handler(text="tovuq1")
async def bosh_menu(call: CallbackQuery):
    await call.message.answer_photo(
        photo=open("images/photo.jfif", "rb"),
        caption="""Narxi 18000 so'm \nTarkibi: Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez\n Iltimos kerakli bo'lgan miqdorni tanlang...""",reply_markup=menuson)
    await call.message.delete()

@dp.callback_query_handler(text="tovuq2")
async def bosh_menu(call: CallbackQuery):
    await call.message.answer("Narxi 22000 so'm \nTarkibi: Tarkibi: Xamir, tovuq go`sht, chips, pomidor, bodring, sous, mayonez\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson)

### gusht
@dp.callback_query_handler(text="gusht")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu3)
@dp.callback_query_handler(text="gusht1")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Narxi 22000 so'm \nTarkibi: Tarkibi: Xamir, Mol go`sht, chips, pomidor, bodring, sous, mayonez\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson1)
@dp.callback_query_handler(text="gusht2")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Narxi 25000 so'm \nTarkibi: Tarkibi: Xamir, Mol go`sht, chips, pomidor, bodring, sous, mayonez\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson1)

### sir
@dp.callback_query_handler(text="sir")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu4)
@dp.callback_query_handler(text="sir1")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Narxi 19000 so'm \nTarkibi: Tarkibi: Xamir, Pishloq, Mol go`sht, chips, pomidor, bodring, sous, mayonez\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson2)
@dp.callback_query_handler(text="sir2")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Narxi 23000 so'm \nTarkibi: Tarkibi: Xamir,Pishloq, Mol go`sht, chips, pomidor, bodring, sous, mayonez\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson2)


## tandir
@dp.callback_query_handler(text="tandir")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Hajmini tanlang....",reply_markup=menu5)
@dp.callback_query_handler(text="tandir1")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Narxi 25000 so'm \nTarkibi: Tarkibi: Xamir, Qo'y go'shti, Mol go`sht, chips, pomidor, bodring, sous, mayonez\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson3)
@dp.callback_query_handler(text="tandir2")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Narxi 28000 so'm \nTarkibi: Tarkibi: Xamir, Qo'y go'shti, Mol go`sht, chips, pomidor, bodring, sous, mayonez\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson3)



####################

#hot_dog_uchun

@dp.callback_query_handler(text="hot")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Turini Tanlang...",reply_markup=menuhot)


@dp.callback_query_handler(text="hot1")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Narxi 13000 so'm \nTarkibi: Tarkibi: Bulochka, Ketchup, Sosiska, chips, pomidor, bodring, sous, mayonez\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson4)
@dp.callback_query_handler(text="hot2")
async def bosh_menu2(call: CallbackQuery):
    await call.message.answer("Narxi 17000 so'm \nTarkibi: Tarkibi: Bulochka, Ketchup, Double Sosiska, chips, pomidor, bodring, sous, mayonez\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson4)


#PIZZA 

@dp.callback_query_handler(text="pizza")
async def bosh_menu3(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu6)

@dp.callback_query_handler(text="mar")
async def bosh_menu3(call: CallbackQuery):
    await call.message.answer("Narxi: 65000 so'm \nMargarita - Maxsus italyancha qizil sous, kolbasa, pomidor,\n mosarella va gauda pishloqlarining mayin mazasi bilan rayhon barglari uyg'unligi.\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson5)

@dp.callback_query_handler(text="pep")
async def bosh_menu3(call: CallbackQuery):
    await call.message.answer("Narxi: 70000 so'm \nPepperoni - Maxsus italyancha qizil sous, sosiska, pomidor,\n mosarella va gauda pishloqlarining mayin mazasi bilan rayhon barglari uyg'unligi.\n Iltimos kerakli bo'lgan miqdorni tanlang...",reply_markup=menuson5)

#KFC

@dp.callback_query_handler(text="kfc")
async def bosh_menu4(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu7)

@dp.callback_query_handler(text="bas")
async def bosh_menu4(call: CallbackQuery):
    await call.message.answer("Narxi: 25000 so'm \nTovuq oyoqchalari, qalampir, sous \nIltimos kerakli bo'lgan miqdorni tanlang...", reply_markup=menuson6)

@dp.callback_query_handler(text="san")
async def bosh_menu4(call: CallbackQuery):
    await call.message.answer("Narxi: 30000 so'm \nTovuq oyoqchalari, kartoshka, qalampir, sous \nIltimos kerakli bo'lgan miqdorni tanlang...", reply_markup=menuson6)


#CLUB SANDWICH

@dp.callback_query_handler(text="sendwich")
async def bosh_menu5(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu8)

@dp.callback_query_handler(text="set1")
async def bosh_menu5(call: CallbackQuery):
    await call.message.answer("Narxi: 15000 so'm \nBekon, non, pomidor, go'sht, pishloq, bodring, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...", reply_markup=menuson7)

@dp.callback_query_handler(text="set5")
async def bosh_menu5(call: CallbackQuery):
    await call.message.answer("Narxi: 50000 so'm \nBekon, non, pomidor, go'sht, pishloq, bodring, mayonez \nIltimos kerakli bo'lgan miqdorni tanlang...", reply_markup=menuson7)


#DONAR

@dp.callback_query_handler(text="donar")
async def bosh_menu6(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu9)

@dp.callback_query_handler(text="donar1")
async def bosh_menu6(call: CallbackQuery):
    await call.message.answer("Narxi: 25000 so'm \nGuruch, non, tovuq go'shti \nIltimos kerakli bo'lgan miqdorni tanlang...", reply_markup=menuson8)

@dp.callback_query_handler(text="donar2")
async def bosh_menu6(call: CallbackQuery):
    await call.message.answer("Narxi: 30000 so'm \nGuruch, non, mol go'shti \nIltimos kerakli bo'lgan miqdorni tanlang...", reply_markup=menuson8)


#DESERT

@dp.callback_query_handler(text="dessert")
async def bosh_menu7(call: CallbackQuery):
    await call.message.answer("Turini tanlang...",reply_markup=menu10)

@dp.callback_query_handler(text="fruitcake")
async def bosh_menu7(call: CallbackQuery):
    await call.message.answer("Narxi: 25000 so'm \nGuruch, non, tovuq go'shti \nIltimos kerakli bo'lgan miqdorni tanlang...", reply_markup=menuson9)

@dp.callback_query_handler(text="cheesecake")
async def bosh_menu7(call: CallbackQuery):
    await call.message.answer("Narxi: 30000 so'm \nGuruch, non, mol go'shti \nIltimos kerakli bo'lgan miqdorni tanlang...", reply_markup=menuson9)

@dp.callback_query_handler(text="choco")
async def bosh_menu7(call: CallbackQuery):
    await call.message.answer("Narxi: 30000 so'm \nGuruch, non, mol go'shti \nIltimos kerakli bo'lgan miqdorni tanlang...", reply_markup=menuson9)

@dp.callback_query_handler(text="med")
async def bosh_menu7(call: CallbackQuery):
    await call.message.answer("Narxi: 30000 so'm \nGuruch, non, mol go'shti \nIltimos kerakli bo'lgan miqdorni tanlang...", reply_markup=menuson9)




# ICHIMLIKLAR ?????????????????????????????????????????

@dp.callback_query_handler(text="ichimliklar")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Iltimos ichimlik turini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="choy")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="kofe")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu3)


@dp.callback_query_handler(text="americano")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik americano\nNarxi:5000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)


@dp.callback_query_handler(text="capuchino")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik capuchino\nNarxi:7000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)


@dp.callback_query_handler(text="3v1")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik 3v1 cofe\nNarxi:4000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)


@dp.callback_query_handler(text="latte")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik latte\nNarxi:8000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu5)

@dp.callback_query_handler(text="sok")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)

@dp.callback_query_handler(text="choylar")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu10)

@dp.callback_query_handler(text="yaxna")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryadan tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)

@dp.callback_query_handler(text="kuk")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik kuk choy\nNarxi:5000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu6)

@dp.callback_query_handler(text="qora")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik qora choy\nNarxi:5000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu6)

@dp.callback_query_handler(text="limon")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik limon choy\nNarxi:7000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu6)

@dp.callback_query_handler(text="fanta")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik Fanta\nNarxi:12000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu11)

@dp.callback_query_handler(text="pepsi")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik Pepsi\nNarxi:13000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu12)

@dp.callback_query_handler(text="cola")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik Coca Cola\nNarxi:13000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu13)

@dp.callback_query_handler(text="sprite")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik Sprite \nNarxi:13000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu14)

@dp.callback_query_handler(text="mojito")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik Mojito fresh \nNarxi:15000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu15)

@dp.callback_query_handler(text="meva")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Hurmatli mijoz\nsiz tanlagan ichimlik Mevali sok \nNarxi:13000 \nltimos sonini tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu16)


#Ichimlik Backlar

@dp.callback_query_handler(text="orqaga5")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = menu)

@dp.callback_query_handler(text="orqaga6")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="orqaga7")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="orqaga10")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu3)

@dp.callback_query_handler(text="orqaga13")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu2)

@dp.callback_query_handler(text="orqaga11")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu10)



@dp.callback_query_handler(text="orqaga8")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)


@dp.callback_query_handler(text="orqaga12")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)


@dp.callback_query_handler(text="orqaga9")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu1)

@dp.callback_query_handler(text="orqaga14")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)

@dp.callback_query_handler(text="orqaga15")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)

@dp.callback_query_handler(text="orqaga16")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)


@dp.callback_query_handler(text="orqaga17")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)

@dp.callback_query_handler(text="orqaga18")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu4)

@dp.callback_query_handler(text="orqaga19")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)

@dp.callback_query_handler(text="orqaga20")
async def suv(call:CallbackQuery):
    await call.message.answer("<b>Kategoryani tanlang</b>",parse_mode = 'HTML',reply_markup = ichimlik_menyu9)







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