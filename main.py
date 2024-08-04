import pygame
import math



U = 110
theta = 60
g = 9



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
 
pygame.init()
screen_size = (1500, 800)
 
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame")

bullet = pygame.image.load("square.png")
rect = bullet.get_rect()
 
clock = pygame.time.Clock()


surface_size = (6, 6)
bullet_surface = pygame.Surface(surface_size)
bullet_surface.fill(RED)

trail_size = (5, 5)
trail_surface = pygame.Surface(trail_size)
trail_surface.fill(WHITE)

theta_rad = math.radians(theta)
#force  x
speedx = U*math.cos(theta_rad)
def y_pos(x): 
    y = x * math.tan(theta_rad) - (g * x**2) / (2 * (U**2) * (math.cos(theta_rad)**2))
    print(x,y)
    return y


rect = pygame.Rect(10, 400, 20, 20)

# path stuff
path_list = []
path_delay = 1

def draw_trail():
    for i in path_list:
        screen.blit(trail_surface, (i[0],i[1]))

speed = [speedx,400]
running = True
pause = True
curr_path_delay = 0

deltatime = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

    screen.fill(BLACK)
    
    # move rect
    rect.x += speedx
    rect.y = screen_size[1] - y_pos(rect.x)
    # rect.move_ip((speedx,screen_size[1] - y_pos(rect.x)))
    # speedx += speedx
    screen.blit(bullet_surface, (rect.x,rect.y))

    # speed[1] = speed[1] - rect.y
    print("move",speed,rect)

    curr_path_delay +=1
    if curr_path_delay == path_delay:
        path_list.append((rect.x,rect.y))
        curr_path_delay = 0

    draw_trail()
   

    pygame.display.update()
    deltatime = clock.tick(10)

 
pygame.quit()