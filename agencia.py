
import textwrap

def menu():
    menu = """\n
    =============== MENU ===============
    [d]\tRealizar novo Depósito
    [s]\tRealizar novo Saque
    [e]\tVisualizar Extrato
    [nc]\tCadastrar nova Conta corrente 
    [lc]\tListar Contas correntes
    [nu]\tCadastrar novo Usuário
    [q]\tSair do Sistema
    =>  """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor >0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ O depósito não foi realizado com sucesso. Valor inválido! @@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Aviso: Você não possui saldo suficiente para esta operação @@@")
    
    elif excedeu_limite:
        print("\n@@@ Aviso: O saque excede o o seu limite @@@")
    
    elif excedeu_saques:
        print("\n@@@ Aviso: Número de saques excedido @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Aviso: O valor informado é inválido @@@")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n=== Extrato ===")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ O CPF informado já está em uso @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informa a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/sigla do estado): ")
    usuarios.apend({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso !!! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n=== A conta foi criada com sucesso! ===")
        return {"agencia":agencia, "numero_conta":numero_conta, "cpf":cpf}
    
    print("\n@@@ O usário não pode ser encontrado. Por favor, cadastre o usuário antes de criar a conta @@@")



def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: \t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

        
    

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao.upper() == "D":
            valor = float(input("Informe o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao.upper() == "S":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )


        elif opcao.upper() == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao.upper() == "NU":
            criar_usuario(usuarios)

        elif opcao.upper() == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao.upper() == "LC":
            listar_contas(contas)

        elif opcao.upper() == "Q":
            break
    
        else:
            print("Opção inválida. Por favor selecione novamente a opção desejada.")


main() 
