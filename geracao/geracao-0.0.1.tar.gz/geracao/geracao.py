# Função de geração de CPFs: 
from random import randint
def cpf(quantidade):
    lista_cpf =[]
    for i in range(0,quantidade):
        while True:
            num_cpf = [randint(0, 9) for i in range(9)]
            if num_cpf != num_cpf[::-1]:
                break
        for i in range(9, 11):
            calculo = sum((num_cpf[num] * ((i + 1) - num) for num in range(0, i)))
            digito = ((calculo * 10) % 11) % 10
            num_cpf.append(digito)
        lista_cpf.append(str(''.join(map(str, num_cpf))))
    return lista_cpf