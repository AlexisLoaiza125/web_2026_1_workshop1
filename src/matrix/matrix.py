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
        """
        Calcula la traza de una matriz cuadrada (suma de los elementos de la diagonal principal).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            number: La suma de los elementos de la diagonal principal

        Raises:
            ValueError: Si la matriz no es cuadrada

        Ejemplo:
            traza([[1, 2], [3, 4]]) -> 5
            traza([[1, 0, 0], [0, 5, 0], [0, 0, 9]]) -> 15
        """
        pass

    def determinante_2x2(self, matriz):
        """
        Calcula el determinante de una matriz 2x2.
        det([[a, b], [c, d]]) = a*d - b*c

        Args:
            matriz (list): Matriz 2x2 (lista de listas)

        Returns:
            number: El determinante de la matriz

        Raises:
            ValueError: Si la matriz no es 2x2

        Ejemplo:
            determinante_2x2([[3, 8], [4, 6]]) -> -14
            determinante_2x2([[1, 2], [3, 4]]) -> -2
        """
        pass

    def determinante_3x3(self, matriz):
        """
        Calcula el determinante de una matriz 3x3 usando la regla de Sarrus.

        Args:
            matriz (list): Matriz 3x3 (lista de listas)

        Returns:
            number: El determinante de la matriz

        Raises:
            ValueError: Si la matriz no es 3x3

        Ejemplo:
            determinante_3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> 0
            determinante_3x3([[1, 0, 0], [0, 2, 0], [0, 0, 3]]) -> 6
        """
        pass

    def identidad(self, n):
        """
        Genera una matriz identidad de tamaño n x n.
        La diagonal principal tiene 1s y el resto 0s.

        Args:
            n (int): Tamaño de la matriz identidad

        Returns:
            list: Matriz identidad n x n

        Ejemplo:
            identidad(2) -> [[1, 0], [0, 1]]
            identidad(3) -> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        """
        pass

    def diagonal(self, matriz):
        """
        Extrae los elementos de la diagonal principal de una matriz cuadrada.

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            list: Lista con los elementos de la diagonal principal

        Raises:
            ValueError: Si la matriz no es cuadrada

        Ejemplo:
            diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1, 5, 9]
            diagonal([[3, 0], [0, 7]]) -> [3, 7]
        """
        pass

    def es_diagonal(self, matriz):
        """
        Verifica si una matriz cuadrada es diagonal
        (todos los elementos fuera de la diagonal principal son cero).

        Args:
            matriz (list): Matriz cuadrada (lista de listas)

        Returns:
            bool: True si la matriz es diagonal, False en caso contrario

        Ejemplo:
            es_diagonal([[3, 0], [0, 7]]) -> True
            es_diagonal([[1, 2], [0, 4]]) -> False
        """
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
