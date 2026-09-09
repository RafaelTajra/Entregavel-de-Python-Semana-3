def calcular_caixa(*precos):
    """Retorna o total, o maior preço e a média dos preços informados."""
    if not precos:
        return 0, None, 0

    total = sum(precos)
    mais_caro = max(precos)
    media = total / len(precos)

    return total, mais_caro, media


total, mais_caro, media = calcular_caixa(10.0, 25.0, 15.0)

print(total)       # 50.0
print(mais_caro)   # 25.0
print(media)       # 16.666...
