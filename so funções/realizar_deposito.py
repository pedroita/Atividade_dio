import datetime


def realizar_deposito(saldo, valor, extrato):
    now = datetime.datetime.now()
    if valor>0:
        saldo += valor
        extrato.append(f"Depósito:\tR$ {valor:.2f} Realizado no dia {now.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("Digite um valor valido!")
    return saldo, extrato