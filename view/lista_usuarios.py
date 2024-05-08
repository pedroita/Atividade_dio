def listar_usuarios(usuarios):
    print("Listando contas...")
    for usuario in usuarios:
        linha = f"""\
            Nome:\t{usuario['nome']}
            Data de Nascimento:\t\t{usuario['data_nascimento']}
            CPF Titular:\t{usuario['cpf']}
        """
        print("=" * 100)
        print(linha)