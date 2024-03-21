'''1. Desarrolla un programa que solicite al usuario que ingrese su edad y luego calcule y
muestre cuántos años le faltan para alcanzar los 100 años.'''

max = 100
edad = int (input("Ingrese su edad: "))

res = max - edad
type(res)
print(f"le faltan {res} años para llegar a los {max} años")