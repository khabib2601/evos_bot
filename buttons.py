from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

til = ReplyKeyboardMarkup(
  keyboard = [
    [
        KeyboardButton(text="🇺🇿 O'zbekcha")
    ],
    [
        KeyboardButton(text="🇷🇺 Русский")
    ],
  ],
  resize_keyboard=True
)

con = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text="📞 Telefon raqamingzini yuboring", request_contact=True)
    ],
  ],
  resize_keyboard=True
)
loc = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text="📍 Lokatsiya Yuboring", request_location=True)
    ],
  ],
  resize_keyboard=True
)



menyu = ReplyKeyboardMarkup(
  keyboard = [
    [
      KeyboardButton(text="🍽Menu")
    ],
    [
      KeyboardButton(text="⬅️ Orqaga")
    ]
  ],
  resize_keyboard=True
)


menu = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="🫔 Lavash",callback_data="lavash"),
      InlineKeyboardButton(text="🌭 Hot-Dog",callback_data="hot")
    ],
    [
      InlineKeyboardButton(text="🍕 Pizza",callback_data="pizza"),
      InlineKeyboardButton(text="🍟 KFC",callback_data="kfc")
    ],
    [
      InlineKeyboardButton(text="🥪 ClubSendwich",callback_data="sendwich"),
      InlineKeyboardButton(text="🍱 Donar",callback_data="donar")
    ],
    [
      InlineKeyboardButton(text="🧁 Dessert",callback_data="dessert"),
      InlineKeyboardButton(text="🍹 Ichimliklar",callback_data="ichimliklar")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back01")
    ],
  ],
)

menu1 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="Tovuq go'shtli lavash 🍗",callback_data="tovuq"),
      InlineKeyboardButton(text="Mol go'shtli lavash 🥩",callback_data="gusht")
    ],
    [
      InlineKeyboardButton(text="Pishloqli Lavash 🧀",callback_data="sir"),
      InlineKeyboardButton(text="Tandir Lavash 🔥",callback_data="tandir")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back1")
    ],
  ],
)
menu2 = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Tovuqli Mini",callback_data="tovuq1"),
      InlineKeyboardButton(text="Tovuqli Classic",callback_data="tovuq2")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back2")
    ],
  ],
)
menuson = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="1",callback_data="son1"),
      InlineKeyboardButton(text="2",callback_data="son2"),
      InlineKeyboardButton(text="3",callback_data="son3")
    ],
    [
      InlineKeyboardButton(text="4",callback_data="son4"),
      InlineKeyboardButton(text="5",callback_data="son5"),
      InlineKeyboardButton(text="6",callback_data="son6")
    ],
    [
      InlineKeyboardButton(text="7",callback_data="son7"),
      InlineKeyboardButton(text="8",callback_data="son8"),
      InlineKeyboardButton(text="9",callback_data="son9")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back3")
    ],
  ],
)

#####


menu3 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="Go'shtli Mini",callback_data="gusht1"),
      InlineKeyboardButton(text="Go'shtli Classic",callback_data="gusht2")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back4")
    ],
  ],
)
menuson1 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="1",callback_data="son1"),
      InlineKeyboardButton(text="2",callback_data="son2"),
      InlineKeyboardButton(text="3",callback_data="son3")
    ],
    [
      InlineKeyboardButton(text="4",callback_data="son4"),
      InlineKeyboardButton(text="5",callback_data="son5"),
      InlineKeyboardButton(text="6",callback_data="son6")
    ],
    [
      InlineKeyboardButton(text="7",callback_data="son7"),
      InlineKeyboardButton(text="8",callback_data="son8"),
      InlineKeyboardButton(text="9",callback_data="son9")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back5")
    ],
  ],
)

###
menu4 = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Pishloqli Mini",callback_data="sir1"),
      InlineKeyboardButton(text="Pishloqli Classic",callback_data="sir2")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back6")
    ],
  ],
)
menuson2 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="1",callback_data="son1"),
      InlineKeyboardButton(text="2",callback_data="son2"),
      InlineKeyboardButton(text="3",callback_data="son3")
    ],
    [
      InlineKeyboardButton(text="4",callback_data="son4"),
      InlineKeyboardButton(text="5",callback_data="son5"),
      InlineKeyboardButton(text="6",callback_data="son6")
    ],
    [
      InlineKeyboardButton(text="7",callback_data="son7"),
      InlineKeyboardButton(text="8",callback_data="son8"),
      InlineKeyboardButton(text="9",callback_data="son9")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back7")
    ],
  ],
)

###
menu5 = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Tandir Mini",callback_data="tandir1"),
      InlineKeyboardButton(text="Tandir Classic",callback_data="tandir2")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back8")
    ],
  ],
)
menuson3 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="1",callback_data="son1"),
      InlineKeyboardButton(text="2",callback_data="son2"),
      InlineKeyboardButton(text="3",callback_data="son3")
    ],
    [
      InlineKeyboardButton(text="4",callback_data="son4"),
      InlineKeyboardButton(text="5",callback_data="son5"),
      InlineKeyboardButton(text="6",callback_data="son6")
    ],
    [
      InlineKeyboardButton(text="7",callback_data="son7"),
      InlineKeyboardButton(text="8",callback_data="son8"),
      InlineKeyboardButton(text="9",callback_data="son9")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back9")
    ],
  ],
)


menuhot = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="🌭 Classic Dog",callback_data="hot1"),
      InlineKeyboardButton(text="🌭 Korolevski",callback_data="hot2")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back10")
    ],
  ],
)


menuson4 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="1",callback_data="son1"),
      InlineKeyboardButton(text="2",callback_data="son2"),
      InlineKeyboardButton(text="3",callback_data="son3")
    ],
    [
      InlineKeyboardButton(text="4",callback_data="son4"),
      InlineKeyboardButton(text="5",callback_data="son5"),
      InlineKeyboardButton(text="6",callback_data="son6")
    ],
    [
      InlineKeyboardButton(text="7",callback_data="son7"),
      InlineKeyboardButton(text="8",callback_data="son8"),
      InlineKeyboardButton(text="9",callback_data="son9")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back11")
    ],
  ],
)


menu6 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="🍕 Margarita",callback_data="mar"),
      InlineKeyboardButton(text="🍕 Pepperoni",callback_data="pep")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back12")
    ],
  ],
)


menuson5 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="1",callback_data="son1"),
      InlineKeyboardButton(text="2",callback_data="son2"),
      InlineKeyboardButton(text="3",callback_data="son3")
    ],
    [
      InlineKeyboardButton(text="4",callback_data="son4"),
      InlineKeyboardButton(text="5",callback_data="son5"),
      InlineKeyboardButton(text="6",callback_data="son6")
    ],
    [
      InlineKeyboardButton(text="7",callback_data="son7"),
      InlineKeyboardButton(text="8",callback_data="son8"),
      InlineKeyboardButton(text="9",callback_data="son9")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back13")
    ],
  ],
)

menu7 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="🍟 Basket",callback_data="bas"),
      InlineKeyboardButton(text="🍟 Sanders basket",callback_data="san")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back14")
    ],
  ],
)


menuson6 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="1",callback_data="son1"),
      InlineKeyboardButton(text="2",callback_data="son2"),
      InlineKeyboardButton(text="3",callback_data="son3")
    ],
    [
      InlineKeyboardButton(text="4",callback_data="son4"),
      InlineKeyboardButton(text="5",callback_data="son5"),
      InlineKeyboardButton(text="6",callback_data="son6")
    ],
    [
      InlineKeyboardButton(text="7",callback_data="son7"),
      InlineKeyboardButton(text="8",callback_data="son8"),
      InlineKeyboardButton(text="9",callback_data="son9")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back15")
    ],
  ],
)


menu8 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="🥪 Chicken Clubsandwich",callback_data="set1"),
      InlineKeyboardButton(text="🥪 Turkey Clubsandwich",callback_data="set5")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back16")
    ],
  ],
)


menuson7 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="1",callback_data="son1"),
      InlineKeyboardButton(text="2",callback_data="son2"),
      InlineKeyboardButton(text="3",callback_data="son3")
    ],
    [
      InlineKeyboardButton(text="4",callback_data="son4"),
      InlineKeyboardButton(text="5",callback_data="son5"),
      InlineKeyboardButton(text="6",callback_data="son6")
    ],
    [
      InlineKeyboardButton(text="7",callback_data="son7"),
      InlineKeyboardButton(text="8",callback_data="son8"),
      InlineKeyboardButton(text="9",callback_data="son9")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back17")
    ],
  ],
)



menu9 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="🥩 Mol go'shtli",callback_data="donar1"),
      InlineKeyboardButton(text="🍗 Tovuq go'shtli",callback_data="donar2")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back18")
    ],
  ],
)


menuson8 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="1",callback_data="son1"),
      InlineKeyboardButton(text="2",callback_data="son2"),
      InlineKeyboardButton(text="3",callback_data="son3")
    ],
    [
      InlineKeyboardButton(text="4",callback_data="son4"),
      InlineKeyboardButton(text="5",callback_data="son5"),
      InlineKeyboardButton(text="6",callback_data="son6")
    ],
    [
      InlineKeyboardButton(text="7",callback_data="son7"),
      InlineKeyboardButton(text="8",callback_data="son8"),
      InlineKeyboardButton(text="9",callback_data="son9")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back19")
    ],
  ],
)



menu10 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="🍰 Mevali tort",callback_data="fruitcake"),
      InlineKeyboardButton(text="🧁 Cheesecake",callback_data="cheesecake")
    ],
    [
      InlineKeyboardButton(text="🍩 Shokoladli pirojniy",callback_data="choco"),
      InlineKeyboardButton(text="🍮 Medovik pirojniy",callback_data="med")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back20")
    ],
  ],
)


menuson9 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="1",callback_data="son1"),
      InlineKeyboardButton(text="2",callback_data="son2"),
      InlineKeyboardButton(text="3",callback_data="son3")
    ],
    [
      InlineKeyboardButton(text="4",callback_data="son4"),
      InlineKeyboardButton(text="5",callback_data="son5"),
      InlineKeyboardButton(text="6",callback_data="son6")
    ],
    [
      InlineKeyboardButton(text="7",callback_data="son7"),
      InlineKeyboardButton(text="8",callback_data="son8"),
      InlineKeyboardButton(text="9",callback_data="son9")
    ],
    [
      InlineKeyboardButton(text="🔙 Orqaga",callback_data="back21")
    ],
  ],
)



ichimlik_menyu1 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "🍵 Choy/☕️ kofe",callback_data = 'choy'),InlineKeyboardButton(text = "🥤 Yaxna ichimliklar",callback_data = "yaxna")
    ],
    [
        InlineKeyboardButton(text = "🧋 Fresh/sok",callback_data = 'sok')
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga5')
    ],
  ],
)
# kofelar
ichimlik_menyu2 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "☕️ Kofelar",callback_data = 'kofe'),InlineKeyboardButton(text = "🍵 Choylar",callback_data = "choylar")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga6')
    ],
  ],
)

ichimlik_menyu3 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "☕️ Americano",callback_data = 'americano'),InlineKeyboardButton(text = "☕️ Capuchino",callback_data = "capuchino")
    ],
    [
        InlineKeyboardButton(text = "☕️ Kofe 3v1",callback_data = '3v1'),InlineKeyboardButton(text = "☕️ Latte",callback_data = "latte")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga7')
    ],
  ],
)

ichimlik_menyu10= InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "🍵 Ko'k choy",callback_data = 'kuk'),InlineKeyboardButton(text = "🍵 Qora choy",callback_data = "qora")
    ],
    [
        InlineKeyboardButton(text = "🍵 Limon choy",callback_data = 'limon')
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga13')
    ],
  ],
)


# yaxna

ichimlik_menyu4 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "🍸 Fanta 1,5 l",callback_data = 'fanta'),InlineKeyboardButton(text = "🥤 Coca cola 1,5 l",callback_data = "cola")
    ],
    [
        InlineKeyboardButton(text = "🍷 Pepsi 1,5 l",callback_data = 'pepsi'),InlineKeyboardButton(text = "🍾 Sprite 1,5 l ",callback_data = "sprite")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga8')
    ],
  ],
)

 # Fresh 


ichimlik_menyu9 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "🍹 Mojito fresh",callback_data = 'mojito'),InlineKeyboardButton(text = "🧃 Mevali sok",callback_data = "meva")
    ],
    
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga9')
    ],
  ],
)

ichimlik_menyu5 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga10')
    ],
  ],
)

ichimlik_menyu6 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga11')
    ],
  ],
)


ichimlik_menyu7 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga12')
    ],
  ],
)


ichimlik_menyu8 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga14')
    ],
  ],
)



ichimlik_menyu11 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga15')
    ],
  ],
)

ichimlik_menyu12 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga16')
    ],
  ],
)


ichimlik_menyu13 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga17')
    ],
  ],
)


ichimlik_menyu14 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga18')
    ],
  ],
)


ichimlik_menyu15 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga19')
    ],
  ],
)


ichimlik_menyu16 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "1",callback_data = "e1"),InlineKeyboardButton(text = "2",callback_data = "e2"),InlineKeyboardButton(text = "3",callback_data = "e3")
    ],
    [
        InlineKeyboardButton(text = "4",callback_data = "e4"),InlineKeyboardButton(text = "5",callback_data = "e5"),InlineKeyboardButton(text = "6",callback_data = "e6")
    ],
    [
        InlineKeyboardButton(text = "7",callback_data = "e7"),InlineKeyboardButton(text = "8",callback_data = "e8"),InlineKeyboardButton(text = "...",callback_data = "e9")
    ],
    [
        InlineKeyboardButton(text = "🔙 Orqaga",callback_data = 'orqaga20')
    ],
  ],
)