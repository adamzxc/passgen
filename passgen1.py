import random
def main():
    words = ["Abdominalyous", "Midasos", "Soapous", "CookThePassword", "Cool", "Vesdeee", "VLesu", "Gribi", "Mechtayut", "ODozhde", "Porbos", "bongo", "kongo", "pongo", "huongo", "chsia", "czechia", "kozak", "commsa", "minecraft", "console", "aww", "Bongo", "Kongo", "Pongo", "Huongo", "Chsia", "Czechia", "Kozak", "Commsa", "Minecraft", "Console", "Aww"]
    ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    #Выбираются слова
    wordone = random.choice(words)
    wordtwo = random.choice(words)
    wordthree = random.choice(words)
    wordfour = random.choice(words)
    word6 = random.choice(words)
    word7 = random.choice(words)
    word8 = random.choice(words)
    word9 = random.choice(words)
    word10 = random.choice(words)
    word11 = random.choice(words)
    word12 = random.choice(words)

    #Выбираются цифры
    intone = random.choice(ints)
    inttwo = random.choice(ints)
    intthree = random.choice(ints)
    intfour = random.choice(ints)
    int5 = random.choice(ints)
    int6 = random.choice(ints)
    int7 = random.choice(ints)
    int8 = random.choice(ints)
    int9 = random.choice(ints)
    int10 = random.choice(ints)
    int11 = random.choice(ints)
    int12 = random.choice(ints)
    int13 = random.choice(ints)
    int14 = random.choice(ints)
    int15 = random.choice(ints)
    int16 = random.choice(ints)
    int17 = random.choice(ints)
    int18 = random.choice(ints)
    int19 = random.choice(ints)
    int20 = random.choice(ints)

    passwd1 = wordone + wordthree + wordtwo + wordfour + word6 + word7 + word8 + word9 + word10 + word11 + word12 + str(intone) + str(inttwo) + str(intthree) + str(intfour) + str(int5) + str(int6) + str(int7) + str(int8) + str(int9) + str(int10) + str(int11) + str(int12) + str(int13) + str(int14) + str(int15) + str(int16) + str(int17) + str(int18) + str(int19) + str(int20)

    #Выбираются слова ещё раз
    wordone1 = random.choice(words)
    wordtwo1 = random.choice(words)
    wordthree1 = random.choice(words)
    wordfour1 = random.choice(words)
    word61 = random.choice(words)
    word71 = random.choice(words)
    word81 = random.choice(words)

    #Выбираются цифры опять
    intone1 = random.choice(ints)
    inttwo1 = random.choice(ints)
    intthree1 = random.choice(ints)
    intfour1 = random.choice(ints)
    int51 = random.choice(ints)
    int61 = random.choice(ints)
    int71 = random.choice(ints)
    int81 = random.choice(ints)

    passwd2 = wordone1 + wordthree1 + wordtwo1 + wordfour1 + word61 + word71 + word81 + str(intone1) + str(inttwo1) + str(intthree1) + str(intfour1) + str(int51) + str(int61) + str(int71) + str(int81)
    finalpass = passwd1 + passwd2
    print("Пароль сгенерирован: " + finalpass)
# Функция для мелкого размера пароля
def short():
    words = ["Abdominalyous", "Midasos", "Soapous", "CookThePassword", "Cool", "Vesdeee", "VLesu", "Gribi", "Mechtayut", "ODozhde", "Porbos", "bongo", "kongo", "pongo", "huongo", "chsia", "czechia", "kozak", "commsa", "minecraft", "console", "aww", "Bongo", "Kongo", "Pongo", "Huongo", "Chsia", "Czechia", "Kozak", "Commsa", "Minecraft", "Console", "Aww"]
    ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    wordw1 = random.choice(words)
    wordw2 = random.choice(words)
    intw1 = random.choice(ints)
    intw2 = random.choice(ints)
    finalpass = wordw1 + wordw2 + str(intw1) + str(intw2)
    print("Пароль сгенерирован: " + finalpass)
# Функция для среднего размера пароля
def mid():
    words = ["Abdominalyous", "Midasos", "Soapous", "CookThePassword", "Cool", "Vesdeee", "VLesu", "Gribi", "Mechtayut", "ODozhde", "Porbos", "bongo", "kongo", "pongo", "huongo", "chsia", "czechia", "kozak", "commsa", "minecraft", "console", "aww", "Bongo", "Kongo", "Pongo", "Huongo", "Chsia", "Czechia", "Kozak", "Commsa", "Minecraft", "Console", "Aww"]
    ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    wordw1 = random.choice(words)
    wordw2 = random.choice(words)
    wordw3 = random.choice(words)
    wordw4 = random.choice(words)
    intw1 = random.choice(ints)
    intw2 = random.choice(ints)
    intw3 = random.choice(ints)
    intw4 = random.choice(ints)
    finalpass = wordw1 + wordw2 + wordw3 + wordw4 + str(intw1) + str(intw2) + str(intw3) + str(intw4)
    print("Пароль сгенерирован: " + finalpass)

# Мой копирайт
print("Password generator by adamzxc prog.")
# Переменная для выбора длины пароля
choicer = input("Which password do you want to create (Long/Short/Medium) (L/S/M)? ")
if choicer == "Long":
    main()
if choicer == "L":
    main()
if choicer == "Short":
    short()
if choicer == "S":
    short()
if choicer == "Medium":
    mid()
if choicer == "M":
    mid()
