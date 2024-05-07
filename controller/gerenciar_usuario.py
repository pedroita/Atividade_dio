from validacoes.validacao_cpf import limpar_cpf, valida_cpf



def filtrar_usuario(cpf,usuarios):
    list_user = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return list_user[0] if list_user else None

def criar_usario(usuarios):
    print("Menu de criação de usuario, siga os passos abaixo!!")
    cpf = input("Digite seu CPF: ")
    if valida_cpf (cpf):
        cpf_corrigido = limpar_cpf(cpf)
        usuario = filtrar_usuario(cpf_corrigido,usuarios)
        if not usuario :
            nome = input("Infome o nome do titular: ")
            data_nascimento = input("Informe a data de nascimentodo titula (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
            print( "Usuario criado com sucesso!!")
            
        else:
            print ( f" O usuario  {usuario['nome']} já existe!")
                
    else:
        print("\nCPF inválido! Digite um CPF valido")