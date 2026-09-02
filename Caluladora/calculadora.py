while True:
    print(f'\n--- calculadora ---')
    print(f'1. soma')
    print(f'2. subtração')
    print(f'3. multiplicação')
    print(f'4. divisão')
    print(f'0. sair')

    opcao = int(input('\ndigite o número da operação desejada: '))

    if opcao == 0:
        print(f'\n----fim da calculadora----')
        break

    elif opcao in [1, 2, 3, 4]:   
        num1 = float(input('\ndigite o primeiro número: '))
        num2 = float(input('digite o segundo número: '))
        
        if opcao == 1:
            print(f'\n\t----SOMA----')
            resultado = num1 + num2
            print(f'\n{num1} + {num2} = {resultado}')
            print(f'\nRESULTADO: {resultado:.2f}')

        elif opcao == 2:
            print(f'\n\t----SUBTRAÇÃO----')
            resultado = num1 - num2
            print(f'\n{num1} - {num2} = {resultado}')
            print(f'\nRESULTADO: {resultado:.2f}')

        elif opcao == 3:
            print(f'\n\t----MULTIPLICAÇÃO----')
            resultado = num1 * num2
            print(f'\n{num1} x {num2} = {resultado:.5f}')
            print(f'\nRESULTADO: {resultado:.2f}')

        elif opcao == 4:
            print(f'\n\t----DIVISÃO----')
            if num2 == 0:
                print(f'\nNão é possível dividir por zero!')
            else:
                resultado = num1 / num2
                print(f'\n{num1} ÷ {num2} = {resultado:.5f}')
                print(f'\nRESULTADO: {resultado:.2f}')

    else:
        print(f'\nopção inválida, tente novamente!')