import math
class Geometria:
    """
    Class with geometric exercises.
    Include basic and funny operations in 2D and 3D.
    """
    
    def area_rectangulo(self, base, altura):
        if base < 0 or altura < 0:
            return 0
        return base*altura
    pass
    def perimetro_rectangulo(self, base, altura):
        return 2*(base+altura)
    pass
    
    def area_circulo(self, radio):
        if radio < 0:
            return 0
        return math.pi * radio ** 2
    pass
    
    def perimetro_circulo(self, radio):
        return 2 * math.pi * radio
    pass
    
    def area_triangulo(self, base, altura):
        return (base * altura) / 2
    pass
    
    def perimetro_triangulo(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3
    pass
    
    def es_triangulo_valido(self, lado1, lado2, lado3):
        return (
            lado1 + lado2 > lado3 and
            lado1 + lado3 > lado2 and
            lado2 + lado3 > lado1
        )
    pass 
    def area_trapecio(self, base_mayor, base_menor, altura):
        return ((base_mayor + base_menor) * altura) / 2
    pass
    
    def area_rombo(self, diagonal_mayor, diagonal_menor):
        return (diagonal_mayor * diagonal_menor) / 2
    pass
    
    def area_pentagono_regular(self, lado, apotema):
        perimetro = self.perimetro_pentagono_regular(lado)
        return (perimetro * apotema) / 2
    pass
    
    def perimetro_pentagono_regular(self, lado):
        return 5 * lado   
    pass
    
    def area_hexagono_regular(self, lado, apotema):
        perimetro = self.perimetro_hexagono_regular(lado)
        return (perimetro * apotema) / 2
    pass
    
    def perimetro_hexagono_regular(self, lado):
        return 6 * lado
    pass
    
    def volumen_cubo(self, lado):
        if (lado < 0 ):
            return 0
        return lado ** 3
    pass
    
    def area_superficie_cubo(self, lado):
        return 6 * (lado ** 2)
    pass
    
    def volumen_esfera(self, radio):
        return (4/3) * math.pi * radio**3
    pass
    
    def area_superficie_esfera(self, radio):
        return 4 * math.pi * radio**2
    pass
    
    def volumen_cilindro(self, radio, altura):
        return math.pi * radio**2 * altura
    pass
    
    def area_superficie_cilindro(self, radio, altura):
        area_lateral = 2 * math.pi * radio * altura
        area_bases = 2 * math.pi * radio**2
        return area_lateral + area_bases        
    pass
    
    def distancia_entre_puntos(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    pass
    
    def punto_medio(self, x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)
    pass
    
    def pendiente_recta(self, x1, y1, x2, y2):
        if x2 == x1:
            return None  # pendiente indefinida
        return (y2 - y1) / (x2 - x1)
    pass
    
    def ecuacion_recta(self, x1, y1, x2, y2):
        # Forma general Ax + By + C = 0
        A = y2 - y1
        B = x1 - x2
        C = x2*y1 - x1*y2
        return (A, B, C)
    pass
    
    def area_poligono_regular(self, num_lados, lado, apotema):
        perimetro = self.perimetro_poligono_regular(num_lados, lado)
        return (perimetro * apotema) / 2
    pass
    
    def perimetro_poligono_regular(self, num_lados, lado):
        return num_lados * lado
    pass
