import pygame
import math

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
 

surface_size = (5, 5)
bullet_surface = pygame.Surface(surface_size)
bullet_surface.fill(WHITE)


U = 70
sina = 0.5
theta = 30
g = 9

theta_rad = math.radians(theta)
#force  x
speedx = U*math.cos(theta_rad)
def y_pos(x,y,t): 
    y +=g 
    return y

rect = pygame.Rect(10, 400, 20, 20)

# path stuff
path_list = []
path_delay = 1

def draw_path():
    for i in path_list:
        screen.blit(bullet_surface, (i[0],i[1]))

speed = [speedx,400]
running = True
pause = True
curr_path_delay = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_SPACE and not pause:
            pause = True


    screen.fill(BLACK)
    
    # move rect
    rect.x += speedx
    rect.y -= y_pos(rect.x)
    
    # speed[1] = speed[1] - rect.y
    print("move",speed,rect)
    # if rect.left < 0 or rect.right > screen_size[0]: 
    #     speed[0] = -speed[0]

    screen.blit(bullet_surface, (rect.x,rect.y))
    
    curr_path_delay +=1
    if curr_path_delay == path_delay:
        path_list.append((rect.x,rect.y))
        curr_path_delay = 0
    
    draw_path()

    pygame.display.update()
    clock.tick(5)
 
pygame.quit()