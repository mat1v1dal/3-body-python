import pygame, math, clock, random

pygame.init()

WIDTH, HEIGHT = 1600, 1000

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("3 BODY SIMULATION")
G = 1
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)

class Body:
    def __init__(self, mass, pos, vel, color):
        self.pos = pos
        self.mass = mass
        self.color = color
        self.vel = vel
    
    def calculateForce(self, other_body):
        dist_x = other_body.pos[0] - self.pos[0]
        dist_y = other_body.pos[1] - self.pos[1]
        dist_abs = math.sqrt((dist_x**2) + (dist_y**2))

        gforce = (G*self.mass*other_body.mass)/dist_abs**2
        gforce_x =  gforce * (dist_x/dist_abs)
        gforce_y = gforce * (dist_y/dist_abs)

        return gforce_x,gforce_y

    def update_vel(self, gforce_x, gforce_y, time):
        acc_x = gforce_x/self.mass
        acc_y = gforce_y/self.mass

        self.vel[0] += acc_x * time
        self.vel[1] += acc_y * time

        self.pos[0] += self.vel[0] * time
        self.pos[1] += self.vel[1] * time

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.pos[0]), int(self.pos[1])), 20)


def main():
    body1 = Body(1000, [WIDTH // 4, HEIGHT // 2], [0, -1], BLUE)
    body2 = Body(9000, [3 * WIDTH // 4, HEIGHT // 2], [0, 0.5], RED)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        pygame.display.update()
        WIN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        force1_x, force1_y = body1.calculateForce(body2)
        force2_x, force2_y = body2.calculateForce(body1)

        time = 1
        body1.update_vel(force1_x, force1_y, time)
        body2.update_vel(force2_x, force2_y, time)

        WIN.fill(WHITE)
        body1.draw(WIN)
        body2.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()
