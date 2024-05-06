#Algoritmo que compara si dos números son iguales, diferentes o si uno es el doble del otro:
#ingresar dos numeros
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
#comparar si aon diferentes, iguales o si uno es doble que el otro
if num1 == num2:
    print("Los números son iguales.")
elif num1 * 2 == num2 or num2 * 2 == num1:
    print("Uno de los números es el doble del otro.")
else:
    print("Los números son diferentes y ninguno es el doble del otro.")
