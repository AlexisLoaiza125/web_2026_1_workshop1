class Matrix:
    """
    Clase con métodos para operaciones sobre matrices.
    Incluye operaciones aritméticas, propiedades y transformaciones matriciales.
    """

    def suma_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Dimensiones incompatibles")

        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] + B[i][j])
            resultado.append(fila)
        return resultado
    pass

    def resta_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Dimensiones incompatibles")

        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] - B[i][j])
            resultado.append(fila)

        return resultado
    pass

    def multiplicar_matrices(self, A, B):
        if len(A[0]) != len(B):
            raise ValueError("Dimensiones incompatibles para multiplicación")

        resultado = []

        for i in range(len(A)):
            fila = []
            for j in range(len(B[0])):
                suma = 0
                for k in range(len(B)):
                    suma += A[i][k] * B[k][j]
                fila.append(suma)
            resultado.append(fila)

        return resultado
    pass

    def multiplicar_escalar(self, matriz, escalar):
        resultado = []

        for fila in matriz:
            nueva_fila = []
            for elemento in fila:
                nueva_fila.append(elemento * escalar)
            resultado.append(nueva_fila)

        return resultado
    pass

    def transpuesta(self, matriz):
        if not matriz:
            return []
        filas = len(matriz)
        columnas = len(matriz[0])

        resultado = []

        for j in range(columnas):
            fila = []
            for i in range(filas):
                fila.append(matriz[i][j])
            resultado.append(fila)

        return resultado
    pass 

    def es_cuadrada(self, matriz):
        if not matriz:
            return False
        return len(matriz) == len(matriz[0])
    pass

    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False

        n = len(matriz)

        for i in range(n):
            for j in range(n):
                if matriz[i][j] != matriz[j][i]:
                    return False

        return True
    pass

    def traza(self, matriz):
        if len(matriz) != len(matriz[0]):
            raise ValueError("La matriz no es cuadrada")
    
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][i]
    
        return suma
    pass

    def determinante_2x2(self, matriz):
        if len(matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("La matriz no es 2x2")
    
        a = matriz[0][0]
        b = matriz[0][1]
        c = matriz[1][0]
        d = matriz[1][1]
    
        return a*d - b*c
    pass

    def determinante_3x3(self, matriz):
        if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            raise ValueError("La matriz no es 3x3")

        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]

        return (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)
    pass

    def identidad(self, n):
        matriz = []
    
        for i in range(n):
            fila = []
            for j in range(n):
                if i == j:
                    fila.append(1)
                else:
                    fila.append(0)
            matriz.append(fila)
    
        return matriz
    pass

    def diagonal(self, matriz):
        if len(matriz) != len(matriz[0]):
            raise ValueError("La matriz no es cuadrada")
    
        diag = []
    
        for i in range(len(matriz)):
            diag.append(matriz[i][i])
    
        return diag
    pass

    def es_diagonal(self, matriz):
        if len(matriz) != len(matriz[0]):
            return False
    
        n = len(matriz)
    
        for i in range(n):
            for j in range(n):
                if i != j and matriz[i][j] != 0:
                    return False
    
        return True
    pass

    def rotar_90(self, matriz):
        """
        Rota una matriz 90 grados en sentido horario.

        Args:
            matriz (list): Matriz (lista de listas)

        Returns:
            list: Matriz rotada 90 grados en sentido horario

        Ejemplo:
            rotar_90([[1, 2], [3, 4]]) -> [[3, 1], [4, 2]]
            rotar_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        """
        pass

    def buscar_en_matriz(self, matriz, valor):
        """
        Busca un valor en la matriz y retorna todas las posiciones donde se encuentra.

        Args:
            matriz (list): Matriz (lista de listas)
            valor: Valor a buscar en la matriz

        Returns:
            list: Lista de tuplas (fila, columna) con las posiciones del valor.
                  Retorna lista vacía si no se encuentra.

        Ejemplo:
            buscar_en_matriz([[1, 2, 3], [4, 2, 6], [7, 8, 2]], 2) -> [(0, 1), (1, 1), (2, 2)]
            buscar_en_matriz([[1, 2], [3, 4]], 9) -> []
        """
        pass
