class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        a = 0
        b = 1
        
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
    pass
    
    def secuencia_fibonacci(self, n):
        resultado = []
        a = 0
        b = 1
        
        for _ in range(n):
            resultado.append(a)
            a, b = b, a + b
        
        return resultado
    pass
    
    def es_primo(self, n):
        if n < 2:
            return False
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    pass
    
    def generar_primos(self, n):
        primos = []
        
        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)
        
        return primos
    pass
    
    def es_numero_perfecto(self, n):
        if n <= 1:
            return False
        
        suma = 0
        
        for i in range(1, n):
            if n % i == 0:
                suma += i
        
        return suma == n
    pass
    
    def triangulo_pascal(self, filas):
        triangulo = []
    
        for i in range(filas):
            fila = [1] * (i + 1)
        
            for j in range(1, i):
                fila[j] = triangulo[i-1][j-1] + triangulo[i-1][j]
        
            triangulo.append(fila)
    
        return triangulo
    pass
    
    def factorial(self, n):
        if n < 0:
            return None
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    pass
    
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    pass
    
    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b)
    pass 

    def suma_digitos(self, n):
        suma = 0
        for digito in str(abs(n)):
            suma += int(digito)
        return suma
    pass
    
    def es_numero_armstrong(self, n):
        digitos = str(n)
        potencia = len(digitos)
    
        suma = 0
        for d in digitos:
            suma += int(d) ** potencia
    
        return suma == n
    pass
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
    
        suma_objetivo = sum(matriz[0])
    
        # filas
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
    
        # columnas
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_objetivo:
                return False
    
        # diagonal principal
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
    
        # diagonal secundaria
        if sum(matriz[i][n - i - 1] for i in range(n)) != suma_objetivo:
         return False
    
        return True
    pass