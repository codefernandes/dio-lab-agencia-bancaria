menu = """

[D] Realizar Depósito
[S] Realizar Saque
[E] Visualizar Extrato
[Q] Sair do Sistema

=> """

saldo_conta = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.upper() == "D":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo_conta += valor
            extrato += f"Depósito de: R$ {valor:.2f}\n"
        else:
            print("Atenção! O valor informado é válido.")

    elif opcao.upper() == "S":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo_conta
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente para realizar este saque.")

        elif excedeu_limite:
            print("O valor do saque excede o limite diário de saques.")

        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo_conta -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido.")

    elif opcao.upper() == "E":
        print("\n================ EXTRATO ================")
        print("Não foram encontradas lançamentos bancários." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_conta:.2f}")
        print("==========================================")

    elif opcao.upper() == "Q":
        break
    
    else:
        print("Opção inválida. Por favor selecione novamente a opção desejada.")
