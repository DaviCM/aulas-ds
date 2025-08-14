def novocpf():
    from random import randint
    
    n = 0
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

    
    def format(cpf):
        # Tenho que declarar 'strcpf' dentro da função, ele não aceita o dado que está fora
        strcpf = ''
        cpf_f = [i for i in cpf]
        
        for i in range(len(cpf_f) + 3):
            if i == 3 or i == 7:
                cpf_f.insert(i, '.')
            
            if i == 11:
                cpf_f.insert(i, '-')
            strcpf += str(cpf_f[i])
        
        return strcpf


    def match_cpf(cpf):
        match cpf[8]:
            case 1:
                est = 'DF, GO, MS, MT e TO'
            case 2:
                est = 'AC, AM, AP, PA, RO e RR'
            case 3:
                est = 'CE, MA e PI'
            case 4:
                est = 'AL, PB, PE, RN'
            case 5:
                est = 'BA e SE'
            case 6:
                est = 'MG'
            case 7:
                est = 'ES e RJ'
            case 8:
                est = 'SP'
            case 9:
                est = 'PR e SC'
            case 0:
                est = 'RS'
                
        return est
         
    
    # Gera os 9 primeiros dígitos do CPF e a lista de valores para validação do 1° dígito.
    # 2 e 11 = iterará de 10 até 2, os 9 dígitos base do CPF.
    for i in reversed(range(2, 11)):
        digit = randint(0, 9)
        cpf.append(digit)
        val1.append(digit * i)
    validate(val1)
    
    # Gera a lista de valores para validação do 2° dígito.
    # 2 e 12 = iterará de 11 até 2, os 9 dígitos base do CPF + o 1° verificador.
    for i in reversed(range(2, 12)):
        val2.append(cpf[n] * i)
        n += 1
    validate(val2)
    
    # Formata o CPF gerado, com pontuação e conversão em STR.
    strcpf = format(cpf)
    
    # Lógica com list comprehension pra transformar todos os elementos de cpf em str e armazenar
    # na ordem certa na lista, depois unir tudo em uma str.   
    print(f'Seu novo CPF é: {''.join([str(cpf[i]) for i in range(len(cpf))])}')
    print(f'Seu novo CPF formatado é: {strcpf}')
    print(f'Seu CPF é valido em: {match_cpf(cpf)}!')
    print('\n''Boa sorte falsificando sua identidade! (Código penal - Art. 299)')
    
novocpf()


