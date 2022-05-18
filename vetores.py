# Tirado de: https://thepythoncodingbook.com/2021/12/11/simulating-3d-solar-system-python-matplotlib/

import math

class Vector:
    # Função de inicialização do vetor
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Função para print do vetor
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    # Função que retorna o valor do item na posição desejada
    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("Ha apenas tres elementos no vetor")

    # Função de adição de dois vetores
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )
    
    # Função de subtração de dois vetores
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )
    
    # Função de multiplicação de dois vetores
    def __mul__(self, other):
        if isinstance(other, Vector):  # Vetor vezes produto
            return (
                self.x * other.x
                + self.y * other.y
                + self.z * other.z
            )
        elif isinstance(other, (int, float)):  # Multiplicação escalar
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other,
            )
        else:
            raise TypeError("Operando deve ser um Vector, int ou float.")
    
    # Função de divisão de dois vetores
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
        else:
            raise TypeError("Operando deve ser um int ou float.")
    
    # Função que retorna a magnitude do vetor
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    # Função de normalização do vetor
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )