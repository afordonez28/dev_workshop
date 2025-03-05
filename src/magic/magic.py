class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    """
    
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def secuencia_fibonacci(self, n):
        secuencia = [0, 1]
        for i in range(2, n):
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia[:n]
    
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        return [num for num in range(2, n + 1) if self.es_primo(num)]
    
    def es_numero_perfecto(self, n):
        if n < 2:
            return False
    
        suma_divisores = 1  # Comenzamos con 1 porque siempre es divisor
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                suma_divisores += i
                if i != n // i:  # Evitar sumar dos veces el mismo divisor en cuadrados perfectos
                    suma_divisores += n // i

        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        triangulo = [[1] * (i + 1) for i in range(filas)]
        for i in range(2, filas):
            for j in range(1, i):
                triangulo[i][j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
        return triangulo
    
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        return sum(int(digito) for digito in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        digitos = [int(d) for d in str(n)]
        return sum(d ** len(digitos) for d in digitos) == n
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        suma_objetivo = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_objetivo:
                return False
        
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False
        
        return True