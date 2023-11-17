def calcularValorZ(estring, Z):
    n = len(estring)
    L, R = 0, 0
    k = 0

    for i in range(1, n):
        if i <= R:
            k = i - L
            if Z[k] < R - i + 1:
                Z[i] = Z[k]
            else:
                L = i
                while R < n and estring[R - L] == estring[R]:
                    R += 1
                Z[i] = R - L
                R -= 1
        else:
            L, R = i, i
            while R < n and estring[R - L] == estring[R]:
                R += 1
            Z[i] = R - L
            R -= 1

def buscar(texto, patron):
    supercadena = patron + "#" + texto

    l = len(supercadena)
    Z = [0] * l
    calcularValorZ(supercadena, Z)

    for i in range(l):
        if Z[i] == len(patron):
            return True

    return False

def palindromo(s):
    n = len(s)
    k = 0
    max_length = 0
    start_index = 0

    while k < n:
        j = 1
        while k - j >= 0 and k + j < n:
            if s[k - j] == s[k + j]:
                j += 1
            else:
                break

        if j > 1 and 2 * j - 1 > max_length:
            max_length = 2 * j - 1
            start_index = k - j + 1

        k += 1

    return start_index, start_index + max_length - 1

def substring_mas_largo(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    result = 0
    end_index = 0

    # Matriz para almacenar la longitud de la subcadena común más larga
    matrix = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

    for i in range(len_str1 + 1):
        for j in range(len_str2 + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > result:
                    result = matrix[i][j]
                    end_index = i - 1
            else:
                matrix[i][j] = 0

    start_index = end_index - result + 1
    return start_index + 1, end_index + 1

def main():
    archivos_transmission = ["transmission1.txt", "transmission2.txt"]
    archivos_mcode = ["mcode1.txt", "mcode2.txt", "mcode3.txt"]

    print("Parte 1:")
    for transmission in archivos_transmission:
        for mcode in archivos_mcode:
            with open(transmission, "r") as f_transmission, open(mcode, "r") as f_mcode:
                transmission_content = f_transmission.read().replace("\n", "")
                mcode_content = f_mcode.read().replace("\n", "")

            if buscar(transmission_content, mcode_content):
                print(f"true {mcode} se encuentra en {transmission}")
            else:
                print(f"false {mcode} no se encuentra en {transmission}")

    print("\nParte 2:")
    for transmission in archivos_transmission:
        with open(transmission, "r") as f_transmission:
            transmission_content = f_transmission.read().replace("\n", "")

        start, end = palindromo(transmission_content)
        print(f"El código espejeado se encuentra entre los caracteres: {start} - {end}")

    print("\nParte 3:")
    with open(archivos_transmission[0], "r") as f_transmission1:
        transmission1_content = f_transmission1.read().replace("\n", "")

    with open(archivos_transmission[1], "r") as f_transmission2:
        transmission2_content = f_transmission2.read().replace("\n", "")

    start, end = substring_mas_largo(transmission1_content, transmission2_content)
    print(f"El substring más largo se puede observar entre {start} - {end} de transmission1")


main()
