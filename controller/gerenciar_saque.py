
import datetime


def filtrar_conta(cpf, contas):
    list_conta = [conta for conta in contas if conta["cpf"] == cpf]
    return list_conta[0] if list_conta else None

def realizar_saque(cpf, contas, extrato, saldo):
    conta_usuario = filtrar_conta(cpf, contas)
    

    if not conta_usuario:
        print("Erro! o número digitado não existe")
    else:
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        saldo_atual = conta_usuario["saldo"]
        limite_saque = conta_usuario["limite_saque"]
        limite_retirada = conta_usuario["limite_retirada"]
        
        
        extrato = conta_usuario["extrato"]
        now = datetime.datetime.now() 
        numero_saques = 0
        if valor_saque > 0:
            print(f"Valor do saque: {valor_saque}")
            print(f"Saldo disponível: {saldo_atual}")
            print(f"Seu limite de saque é {limite_saque}")
            # Verifica se o valor do saque excede o saldo ou os limites
            if valor_saque > saldo_atual:
                print("Erro! O valor de saque excede o saldo disponível.")
            if numero_saques >= limite_saque:
                print("Erro! O valor de saque excede o limite diário de saque.")
            elif valor_saque > limite_retirada:
                print("Erro! O valor de saque excede o limite diário de retirada.")
            else:
                conta_usuario["saldo"]-=valor_saque
                conta_usuario["limite_retirada"] -=1
                numero_saques+=1
                extrato.append(f"Saque:\tR$ {valor_saque:.2f} Realizado no dia {now.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso na conta {conta_usuario['numero_conta']}")
        else:
            print("Digite um valor válido!")
    return saldo, extrato