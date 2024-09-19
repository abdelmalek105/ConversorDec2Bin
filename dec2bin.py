# ------------------------------------------------------
# Convierte un número decimal positivo a binario usando un 
#   determinado número de bits.
# El binario resultante es un string e.g. "101"
# Se usa la función bin() que transforma e.g. 3 en "0b11".
# En esta función se quita el "0b" para dejar el "11"
# ------------------------------------------------------
def dec2bin(numero_decimal, numero_bits):
    if numero_decimal >= 0
        numero_binario = bin(numero_decimal)[2:]  # quita el "0b" del principio
        numero_binario = numero_binario.zfill(numero_bits)  # añade 0's a la izquierda si hace falta
    else:
        # Convertir el número negativo al complemento a dos
        numero_binario = bin((1 << numero_bits) + numero_decimal)[2:]  # quita el "0b" y obtiene complemento a dos
        numero_binario = numero_binario[-numero_bits:]  # se asegura que el resultado tenga el número de bits correcto
    
    return numero_binario

# ----------------------------------------
# MAIN
# ----------------------------------------
if __name__ == "__main__":
    numero_decimal = int(input("Escribe el número en decimal que quieres convertir: "))
    numero_bits = int(input("Cuantos bits tendrá el número binario: "))
    numero_binario = dec2bin(numero_decimal, numero_bits)
    print("El número " + str(numero_decimal) + " es " + numero_binario + " en binario con " + str(numero_bits) + " bits.")
