def exibir_ficha(**dados):
    """Imprime cada informação recebida em uma linha diferente."""
    for campo, valor in dados.items():
        print(f"{campo}: {valor}")


exibir_ficha(
    nome="Rafael",
    idade=18,
    curso="Engenharia de Software"
)
