# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()


# screen = pygame.display.set_mode((1280, 720))
# 获取显示器的尺寸
display_info = pygame.display.Info()
screen_width, screen_height = display_info.current_w / 2, display_info.current_h / 2

# 创建一个全屏且可调整大小的窗口
screen = pygame.display.set_mode((screen_width, screen_height),  pygame.RESIZABLE)

# 设置标题（可选）
pygame.display.set_caption("Fullscreen & Resizeable Window")

print(screen_height)

clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # pygame.draw.circle(screen, "red", player_pos, 20, width=0, draw_top_right=0, draw_top_left=0, draw_bottom_left=0, draw_bottom_right=0)
    pygame.draw.rect(screen, "red", pygame.Rect(player_pos, (screen.get_width() / 20, screen.get_width() / 20)), 20, 0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_q]:
        running = False

    # 重力感
    if 0<= player_pos.y < screen_height - screen.get_width() / 20:
        player_pos.y += 200 * dt
    elif player_pos.y < 0:
        player_pos.y = 0
    else:
        player_pos.y = screen_height - screen.get_width() / 20

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate independent physics.
    dt = clock.tick(60) / 500

pygame.quit()