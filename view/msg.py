import textwrap

def menu_operacoes():
    menu = """
[c]  Criar Usuario 
[nc] Nova conta
[d]  Depositar
[lc] Lista Contas
[lu] Lista Usuarios
[s]  Sacar
[e]  Extrato
[q] Sair

=> """
    return input(textwrap.dedent(menu))