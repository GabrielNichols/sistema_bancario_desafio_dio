'''
desafio:
    separar funções exsitentes (deposito, saque, extrato) em funções separadas;
        função deposito deve receber os argumentos apenas por posição (/);
        função saque deve receber os argumentos apenas por nome (*);
        função extrato deve receber os argumentos por posição (/) e nome (*);
    criar duas novas funções: cadastrar usuario (cliente) e cadastrar conta bancaria;
        criar usuário:
            deve armazenar em um dicionario os dados do usuario (nome, data de nascimento, cpf(só numeros (verificar sómente numeros)), endereço(string com: lougradouro, numero, bairro, cidade, estado));
                verificar se o cpf já existe no sistema;
                    verificação de erro: cpf já cadastrado;
                retornar confirmação de cadastro;
        criar conta bancaria:
            deve armazenar em um dicionario com usuário: agencia (fixo 0001) e numero da conta
                usuário pode ter mais de uma conta, mas uma conta pertencia a apenas um usuário;
                    verificar se o usuário existe no sistema;
                        verificação de erro: usuário não existe;
        criarfunção de menu de opções:
            deve conter as opções: deposito, saque, extrato, sair, cadastrar usuário, cadastrar conta bancaria;
        criar função main:
            deve conter o menu de opções;
'''
import time

# Variáveis globais
saque_diario = 3
limite_de_saque = 500
numero_saque_feito = 0
saldo = 0
extrato = []
usuarios = {}
contas_bancarias = {}


def menu():
    menu = """
    
                    Banco Py
                
                [1] Depositar
                [2] Sacar
                [3] Extrato
                [4] Listar usuários
                [5] Cadastrar usuário
                [6] Cadastrar conta bancária
                [7] Sair
                
"""
    return input(menu)


def deposito(valor_deposito, /):
    global saldo, extrato

    if valor_deposito > 0:
        extrato.append({"Tipo": "Depósito", "Valor": valor_deposito})
        saldo += valor_deposito
        print(f"Depósito de R$:{valor_deposito:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. Digite um valor válido.")

    print(f"\nSeu saldo atualmente é de R$:{saldo:.02f}")
    time.sleep(2)


def saque(*, valor_saque):
    global saldo, extrato, numero_saque_feito

    if saldo > 0:
        if numero_saque_feito < saque_diario:
            if valor_saque > 0 and valor_saque <= limite_de_saque and valor_saque <= saldo:
                saldo -= valor_saque
                extrato.append({"Tipo": "Saque", "Valor": valor_saque})
                numero_saque_feito += 1
                print(f"Saque de R$:{valor_saque:.2f} realizado com sucesso!")
                print(f"\nSeu saldo atualmente é de R$:{saldo:.02f}")
            else:
                print("Valor inválido. Digite um valor válido dentro dos limites.")
        else:
            print("Limite diário de saques atingido.")
    else:
        print("Sem quantia disponível para saque...")

    time.sleep(2)


def exibir_extrato(saldo, /, *, extrato):
    print("\nExtrato:")
    for transacao in extrato:
        tipo = transacao["Tipo"]
        valor = transacao["Valor"]
        print(f"{tipo}: R$:{valor:.2f}")
    print(f"---------------------\nSaldo total R$:{saldo:.02f}")
    time.sleep(2)


def listar_usuarios():
    print("\nLista de usuários:")
    for cpf, usuario in usuarios.items():
        print(f"CPF: {cpf}")
        for key, value in usuario.items():
            if key == "Contas Bancárias":
                print("Contas Bancárias:")
                for conta in value:
                    print(f"    - Número da Conta: {conta}")
                    print(f"      Agência: {contas_bancarias[conta]['Agência']}")
            else:
                print(f"{key}: {value}")
        print("---------------------")
    time.sleep(2)


def cadastrar_usuario():
    while True:
        nome = input("Digite o nome do usuário: ")
        cpf = input("Digite o CPF do usuário (somente números): ")

        # Verificar se o CPF contém somente números
        if not cpf.isdigit():
            print("CPF inválido. Digite somente números.")
            continue

        # Verificar se o CPF já existe no sistema
        if cpf in usuarios:
            print("CPF já cadastrado.")
            continue

        data_nascimento = input("Digite a data de nascimento do usuário (dia/mês/ano): ")

        # Verificar o formato da data de nascimento
        try:
            dia, mes, ano = data_nascimento.split("/")
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)

            # Verificar se a data de nascimento é válida
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 9999):
                print("Data de nascimento inválida. Digite uma data válida.")
                continue

            break

        except ValueError:
            print("Formato inválido. Digite a data de nascimento no formato correto.")

    logradouro = input("Digite o logradouro do endereço: ")
    numero = input("Digite o número do endereço: ")
    bairro = input("Digite o bairro do endereço: ")
    cidade_estado = input("Digite a cidade e estado do endereço: ")

    endereco = f"{logradouro}, {numero}, {bairro}, {cidade_estado}"

    # Imprimir a verificação dos dados inseridos
    print("\nDados do usuário:")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Data de Nascimento: {data_nascimento}")
    print(f"Endereço: {endereco}")

    confirmacao = input("\nOs dados estão corretos? (S/N): ")
    if confirmacao.lower() != "s":
        print("Cadastro cancelado.")
        return

    # Armazenar os dados do usuário no dicionário
    usuarios[cpf] = {
        "Nome": nome,
        "Data de Nascimento": data_nascimento,
        "Endereço": {
            "Logradouro": logradouro,
            "Número": numero,
            "Bairro": bairro,
            "Cidade-Estado": cidade_estado
        },
        "Contas Bancárias": []
    }

    print("Usuário cadastrado com sucesso!")


def cadastrar_conta_bancaria():
    cpf = input("Digite o CPF do usuário para cadastrar a conta bancária: ")

    # Verificar se o usuário existe no sistema
    if cpf not in usuarios:
        print("Usuário não existe.")
        return

    agencia = "0001"
    numero_conta = input("Digite o número da conta bancária: ")

    # Armazenar a conta bancária no dicionário
    contas_bancarias[numero_conta] = {
        "Usuário": usuarios[cpf],
        "Agência": agencia
    }

    # Associar a conta bancária ao usuário correspondente
    usuarios[cpf]["Contas Bancárias"].append(numero_conta)

    print("Conta bancária cadastrada com sucesso!")


def main():
    while True:
        opcao = menu()

        if opcao == "1":
            while True:
                try:
                    valor_deposito = float(input("Digite o valor que deseja depositar: "))
                    deposito(valor_deposito)
                    break
                except ValueError:
                    print("Valor inválido. Digite um valor válido.")

        if opcao == "2":
            while True:
                try:
                    valor_saque = float(input("Digite o valor que deseja sacar: "))
                    saque(valor_saque=valor_saque)
                    break
                except ValueError:
                    print("Valor inválido. Digite um valor válido.")

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            listar_usuarios()

        elif opcao == "5":
            cadastrar_usuario()

        elif opcao == "6":
            cadastrar_conta_bancaria()

        elif opcao == "7":
            print("\nObrigado por ser nosso cliente!")
            time.sleep(2)
            break

        else:
            print("\nDigite uma operação válida!")


if __name__ == "__main__":
    main()
