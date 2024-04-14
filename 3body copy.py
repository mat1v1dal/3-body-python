import pygame, math

pygame.init()

WIDTH, HEIGHT = 800, 800

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("3 BODY SIMULATION")
G = 3
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
GREEN = (0, 255, 0)

class Body:
    def __init__(self, mass, pos, vel, color):
        self.pos = pos
        self.mass = mass
        self.color = color
        self.vel = vel
        self.trayectoria = []
    
    def calculateForce(self, other_body):
        dist_x = other_body.pos[0] - self.pos[0]
        dist_y = other_body.pos[1] - self.pos[1]
        dist_abs = math.sqrt((dist_x**2) + (dist_y**2) + 1)

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

        self.trayectoria.append((self.pos[0], self.pos[1]))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.pos[0]), int(self.pos[1])), 20)

    def draw_trayectoria(self, surface):
        if len(self.trayectoria) > 1:
            pygame.draw.lines(surface, self.color, False, self.trayectoria, 2)
def main():
    body1 = Body(1, [399, 400], [2, 0], BLUE)
    body2 = Body(1, [400, 400], [-3, 0], RED)
    body3 = Body(1, [401, 400], [1, 0], GREEN)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        force1_x, force1_y = body1.calculateForce(body2)
        force2_x, force2_y = body2.calculateForce(body1)
        force1_x_third, force1_y_third = body1.calculateForce(body3)
        force3_x, force3_y = body3.calculateForce(body1)
        force2_x_third, force2_y_third = body2.calculateForce(body3)
        force3_x_second, force3_y_second = body3.calculateForce(body2)

        time = 1
        body1.update_vel(force1_x + force1_x_third, force1_y + force1_y_third, time)
        body2.update_vel(force2_x + force2_x_third, force2_y + force2_y_third, time)
        body3.update_vel(force3_x + force3_x_second, force3_y + force3_y_second, time)


        WIN.fill(BLACK)
        body1.draw(WIN)
        body2.draw(WIN)
        body3.draw(WIN)
        body1.draw_trayectoria(WIN)
        body2.draw_trayectoria(WIN)
        body3.draw_trayectoria(WIN)
        pygame.display.update()

    pygame.quit()

main()
