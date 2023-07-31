import pygame
from error import logs

pygame.init()
screen = pygame.display.set_mode((1250,600))
clock = pygame.time.Clock()
dt = 0
pygame.display.toggle_fullscreen()
dim = pygame.display.get_window_size()
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
entity_2 = pygame.Vector2(player_pos.x, player_pos.y)

def Main():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill("purple")
        pygame.draw.circle(screen, "blue", entity_2, 40)
        pygame.draw.circle(screen, "red", player_pos, 40)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            tempo_1 = player_pos.y - 300 * dt
            if not tempo_1 == 0 and not tempo_1 < 0:
                player_pos.y -= 300 * dt

        if keys[pygame.K_s]:
            tempo_2 = player_pos.y + 300 * dt
            if not tempo_2 >= dim[1]:
                player_pos.y += 300 * dt

        if keys[pygame.K_q]:
            tempo_3 = player_pos.x - 300 * dt
            if not tempo_3 == 0 and not tempo_3 < 0:
                player_pos.x -= 300 * dt

        if keys[pygame.K_d]:
            tempo_4 = player_pos.x + 300 * dt
            if not tempo_4 >= dim[0]:
                player_pos.x += 300 * dt

        tempo_2_1 = player_pos.x - 50
        tempo_2_2 = player_pos.y - 50
        if not tempo_2_1 >= dim[0] and not tempo_2_1 == 0 and not tempo_2_1 < 0:
            entity_2.x = player_pos.x - 50
        if not tempo_2_2 >= dim[1] and not tempo_2_2 == 0 and not tempo_2_2 < 0:
            entity_2.y = player_pos.y - 50
        pygame.display.flip()

        dt = clock.tick(60) / 1020


try:
    Main()
except Exception as ER:
    logs(ER)