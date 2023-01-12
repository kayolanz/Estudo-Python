menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
quantidade_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do deposito: "))


        if valor > 0:
            saldo +=  valor
            extrato += f"Deposito: R$ {valor:.2f}\n"


        else: 
            print("Operacao Incorreta! O valor informado e Invalido.")
    
    elif opcao == "2":
        valor = float(input("Digite o Valor para Saque: "))

        passou_saldo = valor > saldo

        passou_limite = valor > limite

        passou_saques = quantidade_saques >= LIMITE_SAQUES

        if passou_saldo:
            print("Operacao Incorreta! Voce nao tem saldo suficiente.")

        elif passou_limite:
            print("Operacao Incorreta! O valor do saque excede o limite.")
    
        elif passou_saques:
            print("Operacao Incorreta! Numero maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            quantidade_saques += 1
    
        else:
            print("Operacao Incorreta! o valor informado e invalido.")

    elif opcao == "3":
        print("\n================== EXTRATO ================== ")
        print("Nao houve alteracoes em sua conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================")

    elif opcao == "0":
        break

    else:
        print("Operacao Incorreta, por favor selecione novamente a operacao desejada")



