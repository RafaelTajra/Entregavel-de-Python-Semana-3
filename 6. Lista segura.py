def adicionar_sem_alterar(lista_original, item):
    """Retorna uma nova lista com o item, sem alterar a lista recebida."""
    nova_lista = lista_original.copy()
    nova_lista.append(item)
    return nova_lista


numeros = [1, 2, 3]
resultado = adicionar_sem_alterar(numeros, 4)

print(numeros)    # [1, 2, 3]
print(resultado)  # [1, 2, 3, 4]
