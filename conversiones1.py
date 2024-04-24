
# Para ello considere las siguientes tasas de conversión de Peso Chileno:

# a Sol peruano: 0.0046
# ● a Peso Argentino: 0.093
# ● a Dólar Americano: 0.00013
# Además, ingrese un 4to argumento que sea el valor en peso chileno a convertir. El programa
# debe devolver el valor en peso chileno convertido en las 3 divisas ingresadas.
# Al ejecutar el programa se espera el siguiente output:
# python conversiones.py 0.0046 0.093 0.0013 10000
# Respuesta esperada:
# Los 10000 pesos equivalen a:
# 46.0 Soles
# 930.0 Pesos Argentinos
# 13.0 Dólares






# conversiones.py
import sys

# Verificar si se proporcionaron los argumentos correctos en la línea de comandos
if len(sys.argv) != 5:
    print("Por favor ingrese las tasas de conversión y el valor en peso chileno a convertir.")
else:
    try:
        # Convertir los argumentos de la línea de comandos a números de punto flotante para las tasas de conversión y el valor en pesos chilenos
        tasa_sol = float(sys.argv[1])
        tasa_peso_argentino = float(sys.argv[2])
        tasa_dolar = float(sys.argv[3])
        valor_peso_chileno = float(sys.argv[4])

        # Calcular los valores convertidos para soles, pesos argentinos y dólares estadounidenses
        valor_soles = valor_peso_chileno * tasa_sol
        valor_pesos_argentinos = valor_peso_chileno * tasa_peso_argentino
        valor_dolares = valor_peso_chileno * tasa_dolar

        # Imprimir el valor en pesos chilenos para contexto
        print(f"Los {valor_peso_chileno} pesos equivalen a:")
        # Imprimir los valores convertidos para soles, pesos argentinos y dólares estadounidenses
        print(f"{valor_soles:.1f} Soles")
        print(f"{valor_pesos_argentinos:.1f} Pesos Argentinos")
        print(f"{valor_dolares:.1f} Dólares")
    except ValueError:
        # Manejar la excepción ValueError si los argumentos de entrada no se pueden convertir a números
        print("Por favor asegúrese de ingresar números válidos como argumentos.")
