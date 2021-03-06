from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

til = ReplyKeyboardMarkup(
  keyboard = [
    [
        KeyboardButton(text="πΊπΏ O'zbekcha")
    ],
    [
        KeyboardButton(text="π·πΊ Π ΡΡΡΠΊΠΈΠΉ")
    ],
  ],
  resize_keyboard=True
)

con = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text="π Telefon raqamingzini yuboring", request_contact=True)
    ],
  ],
  resize_keyboard=True
)
loc = ReplyKeyboardMarkup(
  keyboard = [
    [
    KeyboardButton(text="π Lokatsiya Yuboring", request_location=True)
    ],
  ],
  resize_keyboard=True
)



menyu = ReplyKeyboardMarkup(
  keyboard = [
    [
      KeyboardButton(text="π½Menu")
    ],
    [
      KeyboardButton(text="β¬οΈ Orqaga")
    ]
  ],
  resize_keyboard=True
)


menu = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="π« Lavash",callback_data="lavash"),
      InlineKeyboardButton(text="π­ Hot-Dog",callback_data="hot")
    ],
    [
      InlineKeyboardButton(text="π Pizza",callback_data="pizza"),
      InlineKeyboardButton(text="π KFC",callback_data="kfc")
    ],
    [
      InlineKeyboardButton(text="π₯ͺ ClubSendwich",callback_data="sendwich"),
      InlineKeyboardButton(text="π± Donar",callback_data="donar")
    ],
    [
      InlineKeyboardButton(text="π§ Dessert",callback_data="dessert"),
      InlineKeyboardButton(text="πΉ Ichimliklar",callback_data="ichimliklar")
    ],
    [
      InlineKeyboardButton(text="π Orqaga",callback_data="back01")
    ],
  ],
)

menu1 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="Tovuq go'shtli lavash π",callback_data="tovuq"),
      InlineKeyboardButton(text="Mol go'shtli lavash π₯©",callback_data="gusht")
    ],
    [
      InlineKeyboardButton(text="Pishloqli Lavash π§",callback_data="sir"),
      InlineKeyboardButton(text="Tandir Lavash π₯",callback_data="tandir")
    ],
    [
      InlineKeyboardButton(text="π Orqaga",callback_data="back1")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back2")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back3")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back4")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back5")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back6")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back7")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back8")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back9")
    ],
  ],
)


menuhot = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="π­ Classic Dog",callback_data="hot1"),
      InlineKeyboardButton(text="π­ Korolevski",callback_data="hot2")
    ],
    [
      InlineKeyboardButton(text="π Orqaga",callback_data="back10")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back11")
    ],
  ],
)


menu6 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="π Margarita",callback_data="mar"),
      InlineKeyboardButton(text="π Pepperoni",callback_data="pep")
    ],
    [
      InlineKeyboardButton(text="π Orqaga",callback_data="back12")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back13")
    ],
  ],
)

menu7 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="π Basket",callback_data="bas"),
      InlineKeyboardButton(text="π Sanders basket",callback_data="san")
    ],
    [
      InlineKeyboardButton(text="π Orqaga",callback_data="back14")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back15")
    ],
  ],
)


menu8 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="π₯ͺ Chicken Clubsandwich",callback_data="set1"),
      InlineKeyboardButton(text="π₯ͺ Turkey Clubsandwich",callback_data="set5")
    ],
    [
      InlineKeyboardButton(text="π Orqaga",callback_data="back16")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back17")
    ],
  ],
)



menu9 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="π₯© Mol go'shtli",callback_data="donar1"),
      InlineKeyboardButton(text="π Tovuq go'shtli",callback_data="donar2")
    ],
    [
      InlineKeyboardButton(text="π Orqaga",callback_data="back18")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back19")
    ],
  ],
)



menu10 = InlineKeyboardMarkup(
  inline_keyboard = [
    [
      InlineKeyboardButton(text="π° Mevali tort",callback_data="fruitcake"),
      InlineKeyboardButton(text="π§ Cheesecake",callback_data="cheesecake")
    ],
    [
      InlineKeyboardButton(text="π© Shokoladli pirojniy",callback_data="choco"),
      InlineKeyboardButton(text="π? Medovik pirojniy",callback_data="med")
    ],
    [
      InlineKeyboardButton(text="π Orqaga",callback_data="back20")
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
      InlineKeyboardButton(text="π Orqaga",callback_data="back21")
    ],
  ],
)



ichimlik_menyu1 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "π΅ Choy/βοΈ kofe",callback_data = 'choy'),InlineKeyboardButton(text = "π₯€ Yaxna ichimliklar",callback_data = "yaxna")
    ],
    [
        InlineKeyboardButton(text = "π§ Fresh/sok",callback_data = 'sok')
    ],
    [
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga5')
    ],
  ],
)
# kofelar
ichimlik_menyu2 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "βοΈ Kofelar",callback_data = 'kofe'),InlineKeyboardButton(text = "π΅ Choylar",callback_data = "choylar")
    ],
    [
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga6')
    ],
  ],
)

ichimlik_menyu3 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "βοΈ Americano",callback_data = 'americano'),InlineKeyboardButton(text = "βοΈ Capuchino",callback_data = "capuchino")
    ],
    [
        InlineKeyboardButton(text = "βοΈ Kofe 3v1",callback_data = '3v1'),InlineKeyboardButton(text = "βοΈ Latte",callback_data = "latte")
    ],
    [
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga7')
    ],
  ],
)

ichimlik_menyu10= InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "π΅ Ko'k choy",callback_data = 'kuk'),InlineKeyboardButton(text = "π΅ Qora choy",callback_data = "qora")
    ],
    [
        InlineKeyboardButton(text = "π΅ Limon choy",callback_data = 'limon')
    ],
    [
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga13')
    ],
  ],
)


# yaxna

ichimlik_menyu4 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "πΈ Fanta 1,5 l",callback_data = 'fanta'),InlineKeyboardButton(text = "π₯€ Coca cola 1,5 l",callback_data = "cola")
    ],
    [
        InlineKeyboardButton(text = "π· Pepsi 1,5 l",callback_data = 'pepsi'),InlineKeyboardButton(text = "πΎ Sprite 1,5 l ",callback_data = "sprite")
    ],
    [
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga8')
    ],
  ],
)

 # Fresh 


ichimlik_menyu9 = InlineKeyboardMarkup(
    inline_keyboard = [
    [
        InlineKeyboardButton(text = "πΉ Mojito fresh",callback_data ='mojito'),InlineKeyboardButton(text = "π§ Mevali sok",callback_data ='meva'),    
    ],
    
    [
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga9')
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
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga10')
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
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga11')
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
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga12')
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
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga14')
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
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga15')
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
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga16')
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
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga17')
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
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga18')
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
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga19')
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
        InlineKeyboardButton(text = "π Orqaga",callback_data = 'orqaga20')
    ],
  ],
)