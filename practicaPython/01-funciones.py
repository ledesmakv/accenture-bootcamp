# Definimos una funcion donde si un numero es par retorna True, si no, False
def es_par(numero):
    return (numero % 2 == 0)

i = 1
while (i <= 6):
    # Va a imprimir 'i es par?: True/False'
    print(i, 'es par?: ', es_par(i))
    i += 1
