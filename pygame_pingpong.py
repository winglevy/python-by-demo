import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scored Bouncing Ball with Bricks")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 球的属性
ball_radius = 10
ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
ball_speed = [2, 2]

# 平台的属性
paddle_width = 100
paddle_height = 10
paddle_pos = [SCREEN_WIDTH // 2 - paddle_width // 2, SCREEN_HEIGHT - 30]

# 障碍物（砖块）列表，这里增加了数量以便演示加分效果
obstacles = []
for i in range(10):
    for j in range(5):
        obstacles.append(pygame.Rect(i * 60 + 20, j * 40 + 20, 50, 20))

# 分数
score = 0
font = pygame.font.Font(None, 36)


def draw_objects(score):
    """绘制屏幕上的元素，包括分数"""
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)
    pygame.draw.rect(screen, WHITE, (paddle_pos[0], paddle_pos[1], paddle_width, paddle_height))

    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    # 显示分数
    score_text = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()


def update_score(hit_obstacle=False):
    """更新分数，如果球击中了砖块则加分"""
    global score
    if hit_obstacle:
        score += 10


def move_ball(obstacles):
    """移动球并处理边界碰撞、障碍物碰撞以及得分更新"""
    global ball_pos, ball_speed

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # 检查球是否触碰上下边界
    if ball_pos[1] <= ball_radius or ball_pos[1] >= SCREEN_HEIGHT - ball_radius:
        ball_speed[1] = -ball_speed[1]

    # 检查球是否触碰左右边界
    if ball_pos[0] <= ball_radius or ball_pos[0] >= SCREEN_WIDTH - ball_radius:
        return False  # 失败，球出界

    # 检查球是否触碰障碍物并移除触碰的障碍物，同时加分
    for obstacle in obstacles[:]:
        if obstacle.collidepoint(ball_pos):
            ball_speed[0] = -ball_speed[0]  # 反弹
            ball_speed[1] = -ball_speed[1]
            update_score(True)  # 击中障碍物加分
            obstacles.remove(obstacle)  # 移除障碍物
            break

    return True  # 成功，球还在界内


def reset_game():
    """游戏重置逻辑，包括球的位置、速度和障碍物的重置"""
    global ball_pos, ball_speed, obstacles
    ball_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    ball_speed = [2, 2]
    obstacles = []  # 这里简单地清空障碍物列表作为重置，实际可以设计更复杂的重置逻辑
    for i in range(10):
        for j in range(5):
            obstacles.append(pygame.Rect(i * 60 + 20, j * 40 + 20, 50, 20))


def main():
    clock = pygame.time.Clock()
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:  # 'R' 键重新开始游戏
                reset_game()
                game_over = False

        keys = pygame.key.get_pressed()
        if not game_over:
            move_paddle(keys)
            ball_in_play = move_ball(obstacles)
            if not ball_in_play:
                game_over = True  # 球未被接到，游戏结束
            check_paddle_collision()
            draw_objects(score)
        else:
            screen.fill(BLACK)
            game_over_text = font.render("Game Over. Press R to Restart", True, RED)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 190, SCREEN_HEIGHT // 2 - 30))
            pygame.display.flip()

        clock.tick(60)  # 控制帧率

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
