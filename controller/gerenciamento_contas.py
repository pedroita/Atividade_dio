from controller.gerenciar_usuario import filtrar_usuario

def criar_conta(cpf, agencia, limite_saque, saldo, limite_retira, contas, usuarios, extrato):
    usuario = filtrar_usuario(cpf, usuarios)
    
    if not usuario:
        print(f"O número do CPF -> {cpf} ainda não é um usuário do sistema")
    else:
        numero_conta = len(contas) + 1
        nova_conta = {
            "numero_conta": numero_conta,
            "agencia": agencia,
            "cpf": cpf,
            "limite_saque": limite_saque,
            "limite_retirada": limite_retira,
            "saldo": saldo,
            "extrato": extrato
            
        }
        contas.append(nova_conta)

        print("\n=== Conta criada com sucesso! ===")
        print("Detalhes da nova conta:")
        print("Número da Conta:", nova_conta["numero_conta"])
        print("Agência:", nova_conta["agencia"])
        print("CPF:", nova_conta["cpf"])
        print("Limite de Saque:", nova_conta["limite_saque"])
        print("Limite de Retirada:", nova_conta["limite_retirada"])
        print("Saldo:", nova_conta["saldo"])
        print("Extrato:", nova_conta["extrato"])
        print("")

    return contas