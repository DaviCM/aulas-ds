def novocpf():
    from random import randint
    
    n = 0
    strcpf = ''
    cpf = []
    val1 = []
    val2 = []
    
    def validate(value):
        # Soma os elementos do CPF até então, pega o resto da divisão por 11 e subtrai por 11, de acordo com a fórmula para descobrir o dígito validador.
        validador = 11 - (sum(value) % 11)
    
        # 0 é um dígito validador se o resultado do resto e da subtração for maior que 10. Caso contrário, será o próprio resultado.
        if validador >= 10:
            cpf.append(0)
        else:
            cpf.append(validador)  

    
    # Gera os 9 primeiros dígitos do CPF e a lista de valores para validação do 1° dígito.
    for i in reversed(range(2, 11)):
        digit = randint(0, 9)
        cpf.append(digit)
        val1.append(digit * i)
    validate(val1)
    
    # Gera a lista de valores para validação do 2° dígito.
    for i in reversed(range(2, 12)):
        val2.append(cpf[n] * i)
        n += 1
    validate(val2)
    
    # Trasnforma o CPF em STR.
    for i in range(len(cpf) + 3):
        if i == 3 or i == 7:
            cpf.insert(i, '.')
            
        if i == 11:
            cpf.insert(i, '-')
        strcpf += str(cpf[i])
        
    print(f'Parabéns! Seu novo CPF é: {strcpf}!')
    print('Já pode falsificar o RG!')
    
novocpf()


