def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('贪吃蛇')
    light = (100, 100, 100)  # 蛇的颜色
    dark = (200, 200, 200)  # 食物颜色
    font1 = pygame.font.SysFont('SimHei', 24)  # 得分的字体
    font2 = pygame.font.Font(None, 72)  # GAME OVER 的字体
    red = (200, 30, 30)  # GAME OVER 的字体颜色
    fwidth, fheight = font2.size('GAME OVER')
    line_width = 1  # 网格线宽度
    black = (0, 0, 0)  # 网格线颜色
    bgcolor = (40, 40, 60)  # 背景色
 
    # 方向，起始向右
    pos_x = 1
    pos_y = 0
    # 如果蛇正在向右移动，那么快速点击向下向左，由于程序刷新没那么快，向下事件会被向左覆盖掉，导致蛇后退，直接GAME OVER
    # b 变量就是用于防止这种情况的发生
    b = True
    # 范围
    scope_x = (0, SCREEN_WIDTH // SIZE - 1)
    scope_y = (2, SCREEN_HEIGHT // SIZE - 1)
    # 蛇
    snake = deque()
    # 食物
    food_x = 0
    food_y = 0
