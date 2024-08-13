while True:
    # Passo 1: Receber ao menos 2 números de entrada do usuário
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    # Passo 2: Converta os valores recebidos pelo usuário para número inteiro (int) ou ponto flutuante (float);
    num1 = float(num1)
    num2 = float(num2)
    
    # Passo 3: Implementar as operações matemáticas
    print("Escolha a operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    operacao = input("Digite o número correspondente à operação desejada: ")

    # Passo 4: Adicionar um laço de repetição ou condicional
    if operacao == '1':
        resultado = num1 + num2
        print(f"O resultado da adição é: {resultado}")
    elif operacao == '2':
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif operacao == '3':
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif operacao == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida.")

    # Perguntar se o usuário quer realizar outra operação
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        print("Encerrando o programa.")
        break

semsaber = 2