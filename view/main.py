from controller.gerenciamento_contas import criar_conta
from controller.gerenciar_saque import realizar_saque
from controller.gerenciar_usuario import criar_usario
from controller.gerencimento_deposito import realizar_deposito
from lista_contas import listar_contas

from validacoes.validacao_cpf import limpar_cpf, valida_cpf
from view.exibir_extrato import exibir_extrato
from view.lista_usuarios import listar_usuarios
from view.msg import menu_operacoes


def main():
    AGENCIA = "0001"
    LIMITE_SAQUE = 3
    saldo = 0
    limite_de_retirada_diario = 500.00
    extrato = []
    usuarios = []
    contas = []

    while True:
        opcao = menu_operacoes()

        if opcao.lower() == 'c':
            print("Criando um novo usuario....")

            criar_usario(usuarios)

        if opcao.lower() == "nc":
            print("Crindo conta.....")
            cpf = input("Digite o CPF que você quer vincular a conta : ")
            if valida_cpf(cpf) == 1:
                cpf_corrigido = limpar_cpf(cpf)
                criar_conta(cpf_corrigido, AGENCIA, LIMITE_SAQUE, saldo,
                            limite_de_retirada_diario, contas, usuarios, extrato)
            else:
                print(f"O {cpf} que você forneceu está errado ou não existe na base de dados")

        if opcao.lower() == 'd':
            print("Reaalizando deposito.....")

            cpf = input("Digite o numero do cpf da conta que voce deseja realizar o deposito: ")
            if valida_cpf(cpf) == 1:
                realizar_deposito(cpf, contas, extrato,saldo)
        if opcao.lower() == 's':
            print("Realizando saque...")
            cpf = input("Digite o CPF da conta que voce deseja realizar o saque: ")
            if valida_cpf(cpf) == "ok":
                realizar_saque(cpf, contas, extrato,saldo)
                
        if opcao.lower() == 'lc':
            print("Listando contas....")
            listar_contas(contas)
        if opcao.lower() == 'lu':
            print("Usuarioss")
            listar_usuarios(usuarios)

        if opcao.lower() == 'e':
            print("Extrado..")
            exibir_extrato(saldo,extrato)
            
        elif opcao.lower() == 'q':
            print("Saindo...")
            break
        else:
            print("")
            
