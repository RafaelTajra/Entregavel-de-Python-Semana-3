# calculadora.py

def dividir(numero1, numero2):
    """
    Divide o primeiro número pelo segundo.

    Parâmetros:
        numero1 (float): Número que será dividido.
        numero2 (float): Número pelo qual será feita a divisão.

    Retorno:
        float: Resultado da divisão.
        str: Mensagem de erro caso o divisor seja zero.
    """
    if numero2 == 0:
        return "Erro: não é possível dividir por zero."

    return numero1 / numero2


from calculadora import dividir

resultado = dividir(10, 2)
print(resultado)  # 5.0

resultado = dividir(10, 0)
print(resultado)  # Erro: não é possível dividir por zero.
