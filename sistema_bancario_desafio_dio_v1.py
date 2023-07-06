'''
deve ter:
deposito, saque e extrato


deposito:

depositar valores positivos para conta (certificar que é positivo)
apenas 1 usuario
depositos armazenados em uma variavel e exibidos na operação extrato (operação tipo:{deposito}:{valor})

saque:

maximo de 3 saques diarios de no maximo 500 reais cada (certificar valor e quantidade de saques)
se não houver saldo em conta, informar "Operação não é possivel, saldo indisponivel
todos os saques devem ser armazenados em uma variável e exibidos na operação extrato (operação tipo:{saque}:{valor})

extrato:

deve exibir todas as operações de deposito e saque e seus valores

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
