import random

'''
ENG:

create() - the function itself

length -> length

counts -> number of passwords

chars -> sets whether the password contains letters

nums -> whether the password contains numbers

symbols -> whether the password contains symbols

lowerSimbol -> sets whether the character "_" in the text with expanded space
lowerSymbolDistance -> sets the spacing of the "_" character in the text
    For example:
        psd = create(lowerSymbol=True, lowerSymbolDistance=3)
        print (psd)

    Conclusion:
        gm4_eFO_EF  # An underscore will be placed every 3 characters

If you don't enter any arguments, the function will return 1 password, 8 characters long.

Example:

    password=create(chars=false, length=16, counts=5)

    print(password)

Conclusion:
    5418074420043687
    4983825832454167
    4180923973205412
    0552142655641343
    7774606619186375


RU:

create() - сама функция

length -> длина пароля

counts -> количество паролей

chars -> задает будут ли в пароле буквы

nums -> задает будут ли в пароле цифры

symbols -> задает будут ли в пароле символы

lowerSimbol -> задает будет ли символ "_" в тексте с определенным промежутком
lowerSymbolDistance -> задает промежуток расставления символа "_" в тексте
    Например:
        psd = create(lowerSymbol = True, lowerSymbolDistance = 3)
        print(psd)

    Вывод:
        gm4_eFO_EF   # Каждые 3 символа будет ставиться нижнее подчеркивание

Если вы не введете аргументы, то функция вернет 1 пароль длиною 8 символов.

Пример:

    password = create(chars=False, length=16, counts=5)

    print(password)

Вывод:
    5418074420043687
    4983825832454167
    4180923973205412
    0552142655641343
    7774606619186375
'''

# Генерация пароля
def create(**Args):
    
    count = 8
    count2 = 1
    chars1 = 1
    num1 = 1
    sym1 = 0
    lowerSymbol = 0
    lowerSymbolDistance = 3
    erno = False
    
    if len(Args) > 0:
        for i in Args:
            get = str(i)
            if get == 'length':
                count = Args[get]
            elif get == 'counts':
                count2 = Args[get]
            elif get == 'chars':
                chars1 = Args[get]
            elif get == 'nums':
                num1 = Args[get]
            elif get == 'symbols':
                sym1 = Args[get]
            elif get == 'lowerSymbol':
                lowerSymbol = Args[get]
            elif get == 'lowerSymbolDistance':
                lowerSymbolDistance = Args[get]
            
            else:
                print(f'\n"{get}" is not defineted')
                erno = True
                break
                
        if chars1 == True:
            chars1 = 1
        if chars1 == False:
            chars1 = 0
            
        if num1 == True:
            num1 = 1
        if num1 == False:
            num1 = 0
        
        if sym1 == True:
            sym1 = 1
        if sym1 == False:
            sym1 = 0
        
        if lowerSymbol == True:
            lowerSymbol = 1
        if lowerSymbol == False:
            lowerSymbol = 0
    
    # Символы для пароля
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    num = '0123456789'
    sym = '_*+!@#$%&^=/'
    
    error = False
    endText = ''
    
    # Проверяет какие символы можно добавлять в пароль
    allSym = ''
    if chars1 == 1:
        allSym += chars
    if num1 == 1:
        allSym += num
    if sym1 == 1:
        allSym += sym
    
    # Если три последних аргумента равняються - 0
    if chars1 == 0 and num1 == 0 and sym1 == 0:
        error = True
    
    # Старт
    if error == False and erno == False:
        for i in range(count2):
            text = ''
            reps = 0
            for i in range(count):
                reps += 1
                text += random.choice(allSym)

                if reps == lowerSymbolDistance and lowerSymbol == 1:
                    text += '_'
                    reps = 0
                
            endText += f'{text}\n'
            
        endText = endText[0:-1]
        return endText
    
    # Ошибка
    if error == True and erno == False:
        print('Error: the password must contain at least letters or numbers or symbols')