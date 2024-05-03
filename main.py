import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

#variaveis
deposito = 0
saque = 0
extrato  = []
LIMITE_SAQUE_DIARIO = 3
limite_de_retirada_diario = 500.00
saldo = 0
now = datetime.datetime.now()
cont_saque_diario = 0
valor_sacado_desejado = 0
while True:
    opcao = input(menu)
    if opcao == 'd' or opcao == 'D':
        deposito = float(input("Digite o valor que queira depoistar: "))
        saldo += deposito
        extrato.append(f"O deposito foi de R${deposito:.2f}  realizado no dia {now.strftime('%Y-%m-%d %H:%M:%S')}  e o valor foi R${saque:.2f}  ")

        print (f"Seu saldo atual é de : {saldo}")
    elif opcao == 'S' or opcao == 's':
         saque = float(input("Quanto você deseja sacar? "))
         if saque>saldo:
             print("não é possivel sacar você não possue esse saldo")
         elif saque <= saldo and cont_saque_diario<LIMITE_SAQUE_DIARIO:
             saldo-= saque
             cont_saque_diario= cont_saque_diario+1
             extrato.append(f"Saque realizado em {now.strftime('%Y-%m-%d %H:%M:%S')} e o valor foi de R${saque:.2f}  ")
             print (f"seu saldo é de {saldo}")
         else:
             print(f"Você estourou o limite de saque, seu limite é {LIMITE_SAQUE_DIARIO}")
    elif opcao == "e" or opcao == "E":
        if not extrato:
            print("ainda não houveram movimentações")
        else:
            for registro in extrato:
                print (registro)
    elif opcao == "q" or opcao == "Q":
        print ("saindo.....")
        break
    else:
        print("opção invalida")
    

