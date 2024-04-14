import pygame
import sys
import math

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulador de Interacción Gravitacional")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Parámetros de simulación
G = 1  # Constante de gravitación
mass1 = 1000  # Masa del primer cuerpo
mass2 = 500  # Masa del segundo cuerpo
pos1 = [WIDTH // 4, HEIGHT // 2]  # Posición inicial del primer cuerpo
pos2 = [3 * WIDTH // 4, HEIGHT // 2]  # Posición inicial del segundo cuerpo
vel1 = [0, -0.5]  # Velocidad inicial del primer cuerpo
vel2 = [0, 0.5]  # Velocidad inicial del segundo cuerpo

def calculate_gravity(pos1, pos2, mass1, mass2):
    # Calcular la distancia entre los cuerpos
    dist = math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)

    # Calcular la fuerza gravitacional
    force = G * mass1 * mass2 / (dist**2)

    # Calcular la dirección de la fuerza
    angle = math.atan2(pos2[1] - pos1[1], pos2[0] - pos1[0])
    force_x = force * math.cos(angle)
    force_y = force * math.sin(angle)

    return force_x, force_y

# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calcular la fuerza gravitacional sobre los cuerpos
    force1_x, force1_y = calculate_gravity(pos1, pos2, mass1, mass2)
    force2_x, force2_y = calculate_gravity(pos2, pos1, mass2, mass1)

    # Calcular la aceleración a partir de la fuerza (F = ma)
    acc1_x = force1_x / mass1
    acc1_y = force1_y / mass1
    acc2_x = force2_x / mass2
    acc2_y = force2_y / mass2

    # Actualizar la velocidad (v = u + at)
    vel1[0] += acc1_x
    vel1[1] += acc1_y
    vel2[0] += acc2_x
    vel2[1] += acc2_y

    # Actualizar la posición (s = ut + 0.5at^2)
    pos1[0] += vel1[0]
    pos1[1] += vel1[1]
    pos2[0] += vel2[0]
    pos2[1] += vel2[1]

    # Dibujar los cuerpos en pantalla
    win.fill(WHITE)
    pygame.draw.circle(win, BLUE, (int(pos1[0]), int(pos1[1])), 20)
    pygame.draw.circle(win, RED, (int(pos2[0]), int(pos2[1])), 20)
    pygame.display.update()

    # Controlar la velocidad de la simulación
    clock.tick(60)