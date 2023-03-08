# son 4 tipos de variables
# String 

name = "Christopher"
last_name = "Murillo"

# Integer
id = 113990099

# Float 
cash = 10.5

# Bool 

active = True

# Comparaciones de las variables
# Como verificar si el PIN ingresado por un usuario coincide con su PIN guardado

entered_pin = 5448
expected_pin = 5448

result = entered_pin == expected_pin

print(result)

# Comparaciones con desigualdad. Tenemos que usar el operador !=

result_1 = 2 != 2
print(result_1)

one = 1
two = 2
print("------------------------------")
print(one == two)
print(one != two)


# Vamos a hacer un interruptor de luz inteligente que apague las luces si es de día y las encienda si es de noche
print("------------------------------")
is_day = False
lights_on = not is_day

print("Daytime?")
print(is_day)

print("Lights on?")
print(lights_on)

# Con las comparaciones vamos a hacer un código que rastree los datos de ventas de una tienda de pantalones
print("------------------------------")

stock = 600
jeans_sold = 500
target = 500

target_hit = jeans_sold == target
print("Hit jeans sale target: ")
print(target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock: ")
print(in_stock)
print(current_stock)


# Podemos usar comparaciones para verificar si un número es mayor o menor que otro número

print("------------------------------")

print(2 < 200)
print(2 > 200)

print(201 <= 200)
print(2 >= 200)

print("------------------------------")

# Comparaciones de cadenas de texto

my_answer = "lowr"
solution = "low"

print(my_answer == solution)
print(my_answer != solution)

# Ejercicio de medidor de frecuencia cardiaca, usando comparaciones para verificar si la frecuencia cardiaca es demasiada baja o alta y le diremos al paciente si debe preocuparse.
print("------------------------------")

heart_rate = 177

too_low = heart_rate < 60
too_high = heart_rate > 100

print("Heart rate low?")
print(too_low)

print("Heart rate high?")
print(too_high)

num1 = 25
num2 = 30
result = num1 - num2
print(result)

print("------------------------------")

edad = 17
resultado = edad >= 18
print("Es mayor de edad?")
print(resultado)

print("------------------------------")

# Usemos comparaciones de string para etiquetar los datos adquiridos a través de la encuesta de usuarios de una aplicación de fitness.
# Verificamos las respuestas de la encuesta de los usuaios con respcto a la frecuencia e intensidad de la actividad, las etiquetaremos y mostraremos los resultados.

frecuencia = "Diaria"
intensidad = "Alta"

activo = frecuencia == "Diaria"
print("El usuario es activo?")
print(activo)

intenso = intensidad == "Alta"
print("El usuario es intenso?")
print(intenso)

print(f"La edad de Christopher es: {edad} y su apellido es Murillo, la intensidad de ejercicio es: {intensidad} y la frecuencia es {frecuencia}")
