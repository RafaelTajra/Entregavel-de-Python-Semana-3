def senha_valida(senha):
    """Retorna True quando a senha possui 8 ou mais caracteres."""
    return len(senha) >= 8


print(senha_valida("python123"))  # True
print(senha_valida("abc"))        # False
