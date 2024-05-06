import datetime

def menu_operacoes():
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuario
[q] Sair

=> """
    return menu

def realizar_deposito(saldo, valor, extrato):
    now = datetime.datetime.now()
    if valor>0:
        saldo += valor
        extrato.append(f"Depósito:\tR$ {valor:.2f} Realizado no dia {now.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("Digite um valor valido!")
    return saldo, extrato

def realizar_saque(saldo, valor, extrato, limite_retirada, numero_saques, limite_saques):
    now = datetime.datetime.now()

    exedeu_saldo = valor > saldo
    exedeu_limite = valor > limite_retirada
    exedeu_saque = numero_saques >= limite_saques
    
    if exedeu_saldo: 
        return saldo, extrato, f"O valor R$ {valor} é maior que seu saldo"
    elif exedeu_limite:
        return saldo, extrato, "O valor de retirada é maior que o limite diário de saque"
    elif exedeu_saque:
        return saldo, extrato, "Você estourou o número de limite de saque diário"
    
    if valor>0:
        saldo -= valor
        numero_saques += 1
        extrato.append(f"Saque:\t\t R${valor:.2f} Realizado no dia {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print ("Saque realizado com sucesso!")
    else:
        print("Valor para saque INVALIDO!!")
    return saldo, extrato, "" 

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    LIMITE_SAQUE = 3
    saldo = 0
    limite_de_retirada_diario = 500.00
    extrato = []
    numero_saques = 0
    
    while True:
        opcao = input(menu_operacoes())
        
        if opcao.lower() == 'd':
            valor_deposito = float(input("Digite o valor que deseja depositar: "))
            saldo, extrato = realizar_deposito(saldo, valor_deposito, extrato)
            print(f"O saldo da conta agora é R$ {saldo:.2f}")
        elif opcao.lower() == 's':
            valor_saque = float(input("Quanto você deseja sacar? "))
            saldo, extrato, mensagem = realizar_saque(saldo, valor_saque, extrato, limite_de_retirada_diario, numero_saques, LIMITE_SAQUE)
            print(f"O saldo da sua conta agora é {saldo:.2f}")
            if mensagem:
                print(mensagem)
        elif opcao.lower() == 'e':
            exibir_extrato(saldo, extrato)
        elif opcao.lower() == 'q':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

main()



def criar_usario(usario):
    return

def filtrar_usario(cpf,usuario):
    return 