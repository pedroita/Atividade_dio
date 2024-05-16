import datetime


def realizar_saque(saldo, valor, extrato, limite_retirada, numero_saques, limite_saques):
    now = datetime.datetime.now()

    exedeu_saldo = valor > saldo
    exedeu_limite = valor > limite_retirada
    exedeu_saque = numero_saques >= limite_saques
    
    if exedeu_saldo: 
        return saldo, extrato, f"O valor R$ {valor} é maior que seu saldo"
    if exedeu_limite:
        return saldo, extrato, "O valor de retirada é maior que o limite diário de saque"
    if exedeu_saque:
        return saldo, extrato, "Você estourou o número de limite de saque diário"
    
    if valor>0:
        saldo -= valor
        extrato.append(f"Saque:\t\t R${valor:.2f} Realizado no dia {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print ("Saque realizado com sucesso!")
        numero_saques += 1
    else:
        print("Valor para saque INVALIDO!!")
    
    return saldo, extrato, numero_saques