def novocpf():
    from random import randint
    
    cpf = []
    val1 = []
    val2 = []

    def generate():
        n = 0 

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

        # Lógica com list comprehension pra transformar todos os elementos de cpf em str (digito i)
        # e armazenar na ordem certa na lista, depois unir tudo em uma str.
        cpf_digits = ''.join([str(i) for i in cpf])

        return cpf_digits

    
    def validate(value):
        # 11 é o número final do cpf e o módulo utilizado pelas validações.
        validador = 11 - (sum(value) % 11)
    
        # 0 é um dígito validador se o resultado do resto e da subtração for maior que 10. Caso contrário, será o próprio resultado.
        if validador >= 10:
            cpf.append(0)
        else:
            cpf.append(validador)  


    def format(cpf):
        # Tenho que declarar 'strcpf' dentro da função, a cobra não aceita o dado que está fora
        strcpf = ''
        # Crio um operador que recebe o valor de cpf, para não operar com o valor de cpf (poderá ser usado depois)
        oprt = [i for i in cpf]

        #   Adicionar 3 na iteração, pois 3 caracteres são adicionados ao cpf.
        for i in range(len(oprt) + 3):
            if i == 3 or i == 7:
                oprt.insert(i, '.')
            
            if i == 11:
                oprt.insert(i, '-')
            strcpf += str(oprt[i])
        
        return strcpf


    def match_cpf(cpf):
        cpf_states = {
            1: 'DF, GO, MS, MT e TO',
            2: 'AC, AM, AP, PA, RO e RR',
            3: 'CE, MA e PI',
            4: 'AL, PB, PE, RN',
            5: 'BA e SE',
            6: 'MG',
            7: 'ES e RJ',
            8: 'SP',
            9: 'PR e SC',
            0: 'RS'
        }

        # O nono dígito do CPF é o identificador do estado de registro.
        return cpf_states.get(cpf[8])
         
    
    print(f'Seu novo CPF é: {generate()}')
    print(f'Seu novo CPF formatado é: {format(cpf)}')
    print(f'Esse CPF é valido em: {match_cpf(cpf)}!')
    print('\n''Polícia Federal diz: Por que você quer gerar um CPF?''\n')

novocpf()


