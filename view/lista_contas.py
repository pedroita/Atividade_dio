def listar_contas(contas):
    print("Listando contas...")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            CPF Titular:\t{conta['cpf']}
        """
        print("=" * 100)
        print(linha)