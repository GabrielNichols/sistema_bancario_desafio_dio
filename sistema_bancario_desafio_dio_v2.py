'''
desafio:
    separar funções exsitentes (deposito, saque, extrato) em funções separadas;
        função deposito deve receber os argumentos apenas por posição (saldo, valor, extrato) e retornar o saldo e extrato atualizados;
        função saque deve receber os argumentos apenas por nome (saldo, valor, extrato, limite, numero_saque_feito, saque_diario) e retornar o saldo e extrato atualizados;
        função extrato deve receber os argumentos por posição (saldo) e nome (extrato)
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

menu = """

                    Banco Py
                
                [1] Depositar
                [2] Sacar
                [3] Extrato
                [4] Sair

"""

saque_diario = 3
limite_de_saque = 500
numero_saque_feito = 0
saldo = 0
extrato = []

def adicionar_transacao(tipo, valor):
    extrato.append({"Tipo": tipo, "Valor": valor})

while True:
    
    opcao = input(menu)

    if opcao == "1":
        while True:
            
            try:
                valor_deposito = float(input(f"""
            Digite o valor que deseja depositar: """))
                if int(valor_deposito) > 0:
                    adicionar_transacao("Depósito", valor_deposito)
                    print(f"""
                          Deposito de R$:{valor_deposito:.2f} realizado com sucesso!
                          """)
                    break
                else:
                    print("Valor inválido. Digite um valor válido.")

            except ValueError:
                print("Valor inválido. Digite um valor válido.")

        saldo += valor_deposito

        print(f"""
              
                Seu saldo atualmente é de R$:{saldo:.02f}
                
                """)
        
        time.sleep(2)
        

    elif opcao == "2":
        while True:
            if saldo > 0:
                if numero_saque_feito < saque_diario:
                    try:
                        valor_saque = float(input("Digite o valor que deseja sacar: "))
                        if valor_saque > 0 and valor_saque <= limite_de_saque and valor_saque <= saldo:
                            saldo -= valor_saque
                            adicionar_transacao("Saque", valor_saque)
                            numero_saque_feito += 1
                            print(f"""
                                  Saque de R$:{valor_saque:.2f} realizado com sucesso!
                                  """)
                            print(f"""

                    Seu saldo atualmente é de R$:{saldo:.02f}

                    """)
                            time.sleep(2)
                            break
                        else:
                            print("Valor inválido. Digite um valor válido dentro dos limites.")
                    except ValueError:
                        print("Valor inválido. Digite um valor válido.")

                else:
                    print("Limite diário de saques atingido.")
                    time.sleep(2)
                    break
            else:
                print("""
Sem quantia disponível para saque...""")
                time.sleep(2)
                break

    elif opcao == "3":
            print("""
            
Extrato:
            """)
            for transacao in extrato:
                tipo = transacao["Tipo"]
                valor = transacao["Valor"]
                print(f"{tipo}: R$:{valor:.2f}")
            print(f"""---------------------
Saldo total R$:{saldo:.02f}""")
            time.sleep(2)



    elif opcao == "4":
        print("""


        Obrigado por ser nosso cliente!

        """)
        time.sleep(2)
        break

    else:
        print("""
              Digite uma operação válida!
              """)
