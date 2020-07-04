from uiautomator import device as d
import time
import random

# 点亮屏幕
d.screen.on()
info = d.info
print(info)  # 1920 * 1080

screen_height = info.get('displayHeight')
screen_width = info.get('displayWidth')

def print_click(sx, sy, ex, ey, second):
    print(str(round(second, 2)) + '秒后拖拽(' + str(round(sx, 2)) + ', ' + str(round(sy, 2)) + '), 到(' + str(
        round(ex, 2)) + ',' + str(round(ey, 2)) + ')')

while 1:
    time.sleep(0.01)
    d.click(screen_width / 2, screen_height / 2)
