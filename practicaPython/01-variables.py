# Accenture QA Bootcamp: Automation - 30/11/2022

# Las variables no pueden empezar con números ni contener palabras reservadas

# Número entero
numero = 420
print('Tipo de numero: ',type(numero))

# Número decimal
decimal = 420.69
print('Tipo de decimal: ', type(decimal))

# Booleano
booleano = True
print('Tipo de booleano: ', type(booleano))

# String
texto = 'hola son las 2:17 pm'
print('Tipo de texto: ', type(texto))

# Conjuntos -> son como diccionarios pero con números/valores
conjunto = {'hola'}

# Lista
lista = ['hola', 'hola', 2]
# List() -> convierte en lista
# Set() -> utilizado para eliminar elementos repetidos en una lista
lista2 = list(set(lista))
print(lista)

# Iteramos la lista e imprimimos cada elemento
for elemento in lista:
    print(elemento)

diccionario = {'key': 'value'}
diccionario = {}
diccionario['nombre'] = 'Karina'
diccionario['edad'] = 26
print(diccionario)
