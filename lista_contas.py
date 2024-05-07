def listar_contas(contas):
    if not contas:
        print("Não há contas criadas ainda.")
    else:
        print("Contas criadas:")
        for conta in contas:
            print("Número da Conta:", conta["numero_conta"])
            print("Agência:", conta["agencia"])
            print("CPF:", conta["cpf"])
            print("Saldo:", conta["saldo"])
            print("Limite de Saque:", conta["limite_saque"])
            print("Limite de Retirada:", conta["limite_retirada"])
            print("Extrato:", conta["extrato"])
            print("-------------------------")