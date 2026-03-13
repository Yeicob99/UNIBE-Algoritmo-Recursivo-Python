def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

numero = int(input("Ingrese un número: "))

resultado = fibonacci(numero)

print("Resultado:", resultado)