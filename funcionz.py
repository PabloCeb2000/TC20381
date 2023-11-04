# Función - Z (Z-Score) O(N+M)

"""
Busqueda de patrones en un texto
    * Patrón long M
    * Patrón long N

Tradicional: O(NM)
    N~M --> O(N^2)
KMP: O(N+M) --> O(2N) =- O(N)

Función Z:
    * Guardar la longitud de la subcadena más larga comenzando en la posición i
    * La subcadena también es un prefijo de la cadena original

    
indice:  0 1 2 3 4 5 6 7 8 9 10 11
texto:   a a b c a a b x a a a  z
valor z: x 1 0 0 3 1 0 0 2 2 1  0
(long de subcadena, que es un prefijo)

Z[0]: * No importa 
      * cualquier subcadena comenzando en 0 es prefijo de str
      * longitud variable: 0...N-1

Z[1]: * long de subcadena más larga y prefijo de str
"""

# Algoritmo

def calularValorZ(estring, Z):
    n = len(estring) # O(N)
    L = 0
    R = 0
    k = 0

    for i in range(n): # O(N) (este no vale)
        if i > R:
            L = i
            R = i
            while((R < n) and estring[R - L] == estring[R]): # O(N) (en el peor de los casos)
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            k = i - L
            if Z[k] < (R - i + 1):
                Z[i] = Z[k]
            else:
                L = i
                while(R < n and estring[R - L] == estring[R]): # O(N) (en el peor de los casos)
                    R += 1
                Z[i] = R - L
                R -= 1

"""
Analisis de palindromos, pseudcodigo.
"""
"""
complejidad de -> O(N^2)
ciclo (verificar caracter x caracter <-> indice k):  O(N) -> FOR(k=0, k<N,k +=1 )
    centro = caracter en posición k
    expansión

    ciclo( h-j <- centro (k) -> h+j): O(N) -> for ( j=1, j>= 0 and j<N, j +=1)
        if (texto[k-j] == texto[k +j ]) :
                sigue avanzando
            else: 
                detener comparación
"""
def palindromo(s):
    n = len(s) # O(N)
    print(n)
    k= 0
    while k<n :
        centro  =  s[k]
        j= 1
        while j >= 0  and j < n: 
            if (k+j < n ):
                if (s[k-j] == s[k+j]):
                    print("Si es")
                    j+=1
                else:
                    break
                    print("No es palindromo")
            else:
                break
                
        k +=1
            
                    




def buscar(texto, patron):
    supercadena = patron + "#" + texto

    l = len(supercadena)
    Z = [0] * l

    calularValorZ(supercadena, Z)
    for i in range(l):
        if(Z[i] == len(patron)):
            print(f"Se localizó la cadena en la posición {i}" )

    

def main():
    texto = "Donde esta Wally"
    patron = "Wally"
    buscar(texto, patron)

    palindromo("baaa")
main()
