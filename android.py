from uiautomator import device as d
import time
import random

# 点亮屏幕
d.screen.on()
info = d.info
print(info) # 1920 * 1080

screen_height = info.get('displayHeight')
screen_width = info.get('displayWidth')


def print_click(x, y, second):
    print('点击坐标为(' + str(round(x, 2)) + ', ' + str(round(y, 2)) + '), ' + str(round(second, 2)) + '秒后再次点击')


while 1:
    # android靠中间区域都是打开菜单，右边大概五分之一才能翻页
    x = random.uniform(screen_width * 4 / 5 + 20, screen_width - 20)
    y = random.uniform(screen_width / 2, screen_width * 2 / 3)
    second = random.uniform(12, 30)
    d.click(x, y)
    print_click(x, y, second)
    time.sleep(second)
