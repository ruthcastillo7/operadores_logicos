# OPERADORES LOGICOS
Nos permiten trabajar con valores de tipo booleano. Un valor booleano o bool solo puede tomar valores True o False,
# ejemplos
1. `and`: y
2. `or`: o
3. `not`: negacion
4. `!`: negacion
>ejemplo
```python
#8. Algoritmo que compara si dos números son iguales, diferentes o si uno es el doble del otro:
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
```
