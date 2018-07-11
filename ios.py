import wda

c = wda.Client('http://localhost:8100')
print(c.status())

# 打开app，如果传的bundle id为空，默认为当前app
# s = c.session('com.tencent.weread')
s = c.session()

# 屏幕尺寸
print(s.window_size()) # iPhone 7p: Size(width=414, height=736)

import threading
import random


def toFixed(num, ndigits=2):
    return round(num, ndigits)


def fun_timer():
    # 随机点击坐标
    x = random.uniform(300, 400)
    y = random.uniform(400, 700)
    s.tap(x, y)
    global timer
    # 随机时间，正常阅读一页的时间为12-30秒
    second = random.uniform(12, 30)
    timer = threading.Timer(second, fun_timer)
    print('点击坐标为(' + str(toFixed(x)) + ', ' + str(toFixed(y)) + '), ' + str(toFixed(second)) + '秒后再次点击')
    timer.start()

# 打开3秒后开始循环
timer = threading.Timer(3, fun_timer)
timer.start()
