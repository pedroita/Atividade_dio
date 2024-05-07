
import datetime


def filtrar_conta(cpf, contas):
    list_conta = [conta for conta in contas if conta["cpf"] == cpf]
    return list_conta[0] if list_conta else None

def realizar_deposito(cpf, contas, extrato, saldo):
    conta_usuario = filtrar_conta(cpf, contas)

    if not conta_usuario:
        print("Erro! o numerod o CPF passado não existe")
    else:
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        now = datetime.datetime.now()  # Obter data e hora atuais

        if valor_deposito > 0:
            conta_usuario["saldo"]+=valor_deposito
            extrato = conta_usuario["extrato"]  # Atualiza o extrato
            extrato.append(f"Depósito:\tR$ {valor_deposito:.2f} Realizado no dia {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso na conta {conta_usuario['numero_conta']} o saldo algora é { conta_usuario["saldo"]}")
        else:
            print("Digite um valor válido!")

    return saldo, extrato