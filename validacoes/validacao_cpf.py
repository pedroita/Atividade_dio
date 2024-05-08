import re

def valida_cpf(cpf):
    cpf_corrigido = limpar_cpf(cpf)
    
    if cpf_corrigido is None or len(cpf_corrigido)!=11:
        return 0
    else:
        return 1
  
def limpar_cpf(cpf):
    cpf_limpo = re.sub(r'\D', '', cpf)
    return cpf_limpo