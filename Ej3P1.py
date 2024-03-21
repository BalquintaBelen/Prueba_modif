"""3. Crea un programa que calcule la suma de los primeros 100 números naturales
utilizando un bucle for"""
suma = 0
max = range(100)
print("empieza la cuenta")
i = 1
for i in max:
    suma = suma + i
    print(f"{suma} + {i} = {suma}")
print(suma)