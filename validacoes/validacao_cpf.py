import re

def valida_cpf(cpf):
    expr = re.compile(r'\d{3}\.?\d{3}\.?\d{3}-?\d{2}')
    if expr.match(cpf):
        return 1
    else:
        return 0
  
def limpar_cpf(cpf):
    cpf_limpo = re.sub(r'\D', '', cpf)
    return cpf_limpo