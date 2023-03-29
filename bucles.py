# while y el for
# Un bucle WHILE repite su bucle de c+odigo mientras su condición es TRUE.

# Para detener el bucle creamos una variable antes de crear el bucle
control = True

while control == True:
    print("Hola mundo")

    control = False

    print("Se monstró una vez")

# Para controlar las veces que se repite un buble while comenzamos con una variable establecida en un número. Llamamos a esta variable: Contador.

contador = 1

while contador < 10:
    print(contador)
    contador += 1


# Calculo de interes compuesto

cuenta = 1000
interes = 0.11
annos = 50

print("Monto inicial: ", cuenta)

contador = 1

while contador <= annos:
    interes_compuesto = cuenta * interes
    cuenta += interes_compuesto
    cuenta += 100
    print("Año: ",contador,": ",cuenta)
    contador += 1


# Hacer un programa que calcule la suma, resta, multiplicación y división de dos números ingresados por el usuario.

# Hacer un programa que calcule el área y la circunferencia de un círculo.

# Hacer un programa que calcule el promedio de una lista de números ingresados por el usuario.

# Hacer un programa que determine si un número ingresado por el usuario es par o impar.

# Hacer un programa que calcule la tabla de multiplicar de un número ingresado por el usuario.

# Hacer un programa que cuente la cantidad de letras y números en un texto ingresado por el usuario.

# Hacer un programa que ordene una lista de números ingresados por el usuario en orden ascendente o descendente.



