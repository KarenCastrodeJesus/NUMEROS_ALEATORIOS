# Generar 20 numeros aleatorios entre 0 y 1

a = 5
c = 3
m = 16
x = 7

print("Numeros aleatorios:")

for i in range(20):
    x = (a * x + c) % m
    r = x / m
    print(r, end=" ")
