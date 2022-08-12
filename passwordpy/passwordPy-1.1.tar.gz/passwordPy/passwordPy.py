import random

# Генерация пароля
def create(**Args):
    
    # Настройки пароля по умолчанию
    count = 8
    count2 = 1
    chars1 = 1
    num1 = 1
    sym1 = 0
    lowerSymbol = 0
    lowerSymbolDistance = 3
    lowerLetters = 1
    upperLetters = 1
    returnList = 0
    erno = False
    
    # Проверяет какие аргументы были введены
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
            elif get == 'lowerLetters':
                lowerLetters = Args[get]
            elif get == 'upperLetters':
                upperLetters = Args[get]
            elif get == 'returnList':
                returnList = Args[get]
            
            else:
                print(f'{get}" is not defineted')
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
        
        if lowerLetters == True:
            lowerLetters = 1
        if lowerLetters == False:
            lowerLetters = 0
            
        if upperLetters == True:
            upperLetters = 1
        if upperLetters == False:
            upperLetters = 0
        
        if returnList == True:
            returnList = 1
        if returnList == False:
            returnList = 0
    
    # Символы для пароля
    charsLower = 'qwertyuiopasdfghjklzxcvbnm'
    charsUpper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    num = '0123456789'
    sym = '_*+!@#$%&^=/'
    
    # Переменные
    error = False
    endText = ''
    endTextList = []
    
    if chars1 == 1 and lowerLetters == 0 and upperLetters == 0:
        print('Error in passwordSettings: must contain uppercase or lowercase letters')
        erno = True

    # Проверяет какие символы можно добавлять в пароль
    allSym = ''
    if chars1 == 1:

        if lowerLetters == 1:
            allSym += charsLower

        if upperLetters == 1:
            allSym += charsUpper

    if num1 == 1:
        allSym += num
    if sym1 == 1:
        allSym += sym
    
    # Если chars, nums и symbols = 0 -> Ошибка 
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
            
            if returnList == 0:
                endText += f'{text}\n'
            elif returnList == 1:
                endTextList.append(f'{text}')
        
        if returnList == 0:
            endText = endText[0:-1]
            return endText
        elif returnList == 1:
            return endTextList
    
    # Ошибка
    if error == True and erno == False:
        print('Error in passwordSettings: the password must contain at least letters or numbers or symbols')