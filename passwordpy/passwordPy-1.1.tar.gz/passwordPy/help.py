''''
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

upperLetters -> задает будут ли в пароле буквы верхнего регистра
lowerLetters -> задает будут ли в пароле буквы нижнего регистра

returnList -> вернет пароли в виде списка

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