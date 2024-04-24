

with open("lorem_ipsum.txt", "r") as file:  # Abrir el archivo "lorem_ipsum.txt" en modo lectura
    texto = file.read()  # Leer el contenido del archivo y almacenarlo en la variable "texto"

    # Utilizar un conjunto para obtener los caracteres distintos
    caracteres_distintos = set(texto)

    # Contar la cantidad de caracteres distintos
    cant_caracteres_distintos = len(caracteres_distintos)

    palabras = texto.split()  # Dividir el texto en palabras utilizando el método .split()
    # Utilizar un conjunto para obtener las palabras distintas
    palabras_distintas = set(palabras)

    # Contar la cantidad de palabras distintas
    cant_palabras_distintas = len(palabras_distintas)


print(
    f"El número de caracteres distintos en el texto es: {cant_caracteres_distintos}")
print(
    f"El número de palabras distintas en el texto es: {cant_palabras_distintas}")
