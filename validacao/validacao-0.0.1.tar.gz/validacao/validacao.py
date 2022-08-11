# Função de validacao de CPF: 
def cpf(documento):
    num_cpf = [int(i) for i in documento if i.isdigit()]
    if (len(num_cpf) != 11) or (str(num_cpf) in ['00000000191','12345678909']):
        return False
    if num_cpf == num_cpf[::-1]:
        return False
    for j in range(9, 11):
        calculo = sum((num_cpf[num] * ((j+1) - num) for num in range(0, j)))
        digit = ((calculo * 10) % 11) % 10
        if digit != num_cpf[j]:
            return False
    return True