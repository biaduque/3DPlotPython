# Tirado de: https://thepythoncodingbook.com/2021/12/11/simulating-3d-solar-system-python-matplotlib/

import matplotlib.pyplot as plt
import math

from vetores import Vector

class SolarSystem:
    '''
    size:: Tamanho do cubo que receberá o sistema solar
    bodies:: Receberá todos os corpos dentro do sistema solar
    fig; ax:: Parâmetros responsáveis pelo plot do sistema
    '''

    # Função de inicialização do sistema solar
    def __init__(self, size):
        self.size = size
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size / 50, self.size / 50),
        )
        self.fig.tight_layout()
        self.ax.view_init(0, 0)

    # Função para adicionar novos corpos celestes ao sistema solar
    def add_body(self, body):
        self.bodies.append(body)
    
    # Função para atualizar a posição todos os corpos celestes do sistema solar
    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()

    # Função para desenhar todos os corpos no sistema solar
    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        plt.pause(0.001)
        self.ax.clear()
    
class SolarSystemBody:
    '''
    min_display_size:: Parâmetro que recebe o menor valor para que o objeto plotado não seja muito pequeno
    display_log_base:: Parâmetro que recebe o valor da escala logaritmica para converter a massa para o tamanho do plot
    solar_system:: Parâmetro que recebe o objeto sistema solar
    mass:: Parâmetro que recebe o valor relativo da massa do corpo celeste
    position:: Parâmetro que recebe a posição do corpo celeste no sistema solar
    velocity:: Parâmetro que recebe a velocidade do corpo celeste no sistema solar
    display_size:: Parâmetro que recebe o tamanho de exibição do corpo no sistema
    colour:: Parâmetro que recebe a cor na qual o corpo celeste será plotado
    '''

    min_display_size = 10
    display_log_base = 1.3

    # Função de inicialização de um corpo celeste
    def __init__(
        self,
        solar_system,
        mass,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        self.colour = "pink"

        self.solar_system.add_body(self)
    
    # Função para mover o corpo celeste no sistema solar
    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2],
        )
    
    # Função para desenho do corpo celeste
    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size + self.position[0] / 30,
            color=self.colour
        )

    # Função para calculo da aceleração da gravidade
    def accelerate_due_to_gravity(self, other):
        distance = Vector(*other.position) - Vector(*self.position)
        distance_mag = distance.get_magnitude()
        force_mag = self.mass * other.mass / (distance_mag ** 2)
        force = distance.normalize() * force_mag
        reverse = 1
        for body in self, other:
            acceleration = force / body.mass
            body.velocity += acceleration * reverse
            reverse = -1