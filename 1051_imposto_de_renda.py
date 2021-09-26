dinheiro = float(input())


if 0 <= dinheiro < 2000.00:
    print("Isento")
elif 2000.01 <= dinheiro <= 3000.00:
    valor_taxado = dinheiro - 2000.00
    imposto = valor_taxado * 0.08
    print(imposto)
elif 3000.01 <= dinheiro <= 4500.00:
    valor_taxado = dinheiro - 3000.00
    imposto1 = valor_taxado * 0.18
    print(imposto1)
    print(valor_taxado)
    if 1000.00 <= valor_taxado <= 3000.00:
        valor_taxado2 = valor_taxado - 2000.00
        imposto2 = valor_taxado2 * 0.08
        result = imposto1 + imposto2
        print(result)
