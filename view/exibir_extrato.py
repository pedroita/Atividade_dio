def exibir_extrato(extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    #print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

