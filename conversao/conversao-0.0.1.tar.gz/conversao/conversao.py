# Função de conversão de temperatura: 
def temperatura(graus, de, para):
    try:
        float(graus)
        check_num = True
    except ValueError:
        check_num = False
        return 'Erro! A quantidade da temperatura em graus, deve ser um número.'

    de = de.upper() 
    para = para.upper() 

    if ((de in ['C','CELSIUS']) and (para in ['F','FAHRENHEIT']) and (check_num ==True)):
        graus = float(graus)
        temp_c_para_f = 1.8 * graus + 32
        return temp_c_para_f
    elif ((de in ['F','FAHRENHEIT']) & (para in ['C','CELSIUS']) and (check_num ==True)):
        graus = float(graus)
        temp_f_para_c = (graus - 32) / 1.8
        return temp_f_para_c

    elif ((de in ['C','CELSIUS']) and (para in ['K','KELVIN']) and (check_num ==True)):
        graus = float(graus)
        temp_c_para_k = graus + 273.15
        return temp_c_para_k
    elif ((de in ['K','KELVIN']) & (para in ['C','CELSIUS']) and (check_num ==True)):
        graus = float(graus)
        temp_k_para_c = graus -273.15
        return temp_k_para_c

    elif ((de in ['F','FAHRENHEIT']) and (para in ['K','KELVIN']) and (check_num ==True)):
        graus = float(graus)
        temp_f_para_k = (graus - 32) / 1.8 + 273.15
        return temp_f_para_k

    elif ((de in ['K','KELVIN']) & (para in ['F','FAHRENHEIT']) and (check_num ==True)):
        graus = float(graus)
        temp_k_para_f = (graus - 273.15) * 1.8 + 32
        return temp_k_para_f

    elif ((de == para) and (check_num ==True)):
        graus = float(graus)
        temp_ = graus
        return temp_ 
    else: 
        erro = 'Erro! Alguma variavél está incorreta.'
    return erro