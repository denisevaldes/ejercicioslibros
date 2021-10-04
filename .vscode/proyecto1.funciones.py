import random


def crear_matriz(filas, columnas, cantidad_filas, cantidad_columnas):

    for indice in range(0,cantidad_filas):
        #lista columna se blanquea por cada ciclo interno cumplido
        columnas = []
        # se entra a ciclo referente a columnas dentro de determinada fila
        for subindice in range(0, cantidad_columnas):
            # si se esta en fila 1 (indice = 0)
            if indice == 0:
                # si se esta en columna 1 (subindice = 0)
                # punto (0,0)
                if subindice == 0:
                    casilla = "   "
                # si se esta en columna mayor a 1 (subindice != 0)
                # ej: punto(0,2)
                else:
                    casilla = f" {subindice} "
            # si se esta en fila mayor a 1 (indice != 0)
            else:
                # si se esta en columna 1 (subindice = 0)
                if subindice == 0:
                    casilla = f"  {indice}|"
                # si se esta en columna mayor a 1 (subindice != 0)
                # ej: punto(2,2)
                else:
                    casilla = "  |"
            #se agrega casilla a lista 'columnas' 
            columnas.append(casilla)
        #cerrado ciclo interno (relativo de columnas), se agrega lista 'columnas' dentro de lista 'filas'
        filas.append(columnas)
    return filas
    #particula = "x|"

    #filas[2][2] = particula
def visualizacion_matriz(cantidad_filas,cantidad_columnas, filas):

    for i in range(0,cantidad_filas):
        print("\n")
        for sub in range(0,cantidad_columnas):
            print(filas[i][sub], end="")        
    print("\n")

def main():
    filas = []
    columnas = []
    cantidad_filas = random.randrange(4,10)
    #para probar programa
    #cantidad_filas = 4
    cantidad_columnas = cantidad_filas
    matriz = crear_matriz(filas, columnas, cantidad_filas, cantidad_columnas)
    visualizacion_matriz(cantidad_filas,cantidad_columnas, filas)

if __name__ == "__main__":
    main()
   