emails = []

email_validados = set()
def validar_email(emails, email_validados):
    for validar in emails:
        if '@gmail' in validar or '@outlook' in validar or '@hotmail' in validar:
            email_validados.add(validar)

    return email_validados

while True: 
    config = int(input('1 - CADASTRAR \t 2 - RENOMEAR \t 3 - VALIDAR E-MAIL \t 4 - SAIR: '))

    if config == 1:
        symbols = ['!', '#', '%', '$']
        tentativas_cadastrar = 3
        cadastrar_email = input('Digite um email: ')
        for simbolo in symbols:
            if simbolo in cadastrar_email:
                print('Erro ao cadastrar, tente novamente: ')
                for tentar_novamente in range(tentativas_cadastrar):
                    cadastrar_email = input('Digite novamente: ')

                    if simbolo in cadastrar_email:
                        print('Erro ao cadastrar.')
                    else:
                        print('E-mail cadastrado')
                        emails.append(cadastrar_email)
                        break
            else:
                emails.append(cadastrar_email)
    
    elif config == 2:
        while True:
            config_renomear = int(input('1 - PESQUISAR \t 2 - SAIR: '))

            if config_renomear == 1:
                renomear_email = input('Digite o e-mail que quer renomear: ')
                
                if renomear_email in emails:
                    email_change = input('Renomeie o e-mail: ')
                    email = renomear_email.replace(renomear_email, email_change)
                    emails.append(email_change)
                    
                    email_renomeado = {
                        'Antigo email': renomear_email,
                        'Novo E-mail': email
                    }

                    for ae, ne in email_renomeado.items():
                        print(f'{ae}: {ne}')

                else:
                    print('E-mail inexistente.')
            
            elif config_renomear == 2:
                break

    elif config == 3:
        validar_email(emails, email_validados)
        print(email_validados)
    
    elif config == 4:
        print('Você saiu do sistema.')
        break