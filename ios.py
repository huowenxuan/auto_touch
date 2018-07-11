import wda
import time
import random

c = wda.Client('http://localhost:8100')
print(c.status())

# 打开app，如果传的bundle id为空，默认为当前app
# s = c.session('com.tencent.weread')
s = c.session()

# 屏幕尺寸
size = s.window_size()
screen_width = size[0]
screen_height = size[1]
print(size) # iPhone 7p: Size(width=414, height=736)


def print_click(x, y, second):
    print('点击坐标为(' + str(round(x, 2)) + ', ' + str(round(y, 2)) + '), 间隔' + str(round(second, 2)) + '秒')


while 1:
    # 随机点击坐标
    x = random.uniform(screen_width * 2 / 3, screen_width - 20)
    y = random.uniform(screen_height / 2, screen_height - 50)
    second = random.uniform(12, 30)
    time.sleep(second)
    s.tap(x, y)
    print_click(x, y, second)

