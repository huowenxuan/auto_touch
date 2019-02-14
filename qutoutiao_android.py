from uiautomator import device as d
import time
import random

# 点亮屏幕
d.screen.on()
info = d.info
print(info) # 1920 * 1080

screen_height = info.get('displayHeight')
screen_width = info.get('displayWidth')

def print_click(sx, sy, ex, ey, second):
    print(str(round(second, 2)) + '秒后拖拽(' + str(round(sx, 2)) + ', ' + str(round(sy, 2)) + '), 到(' +  str(round(ex, 2)) + ',' +  str(round(ey, 2)) + ')')

while 1:
    sx = random.uniform(20, screen_width / 3 * 2)
    sy = random.uniform(screen_height / 2, screen_height - 150)
    ex = random.uniform(20, screen_width / 3 * 2)
    ey = random.uniform(50, screen_height / 2)
    second = random.uniform(20, 40)
    print_click(sx, sy, ex, ey, second)
    time.sleep(second)
    steps = random.uniform(10, 30)
    d.swipe(sx, sy, ex, ey, steps)


