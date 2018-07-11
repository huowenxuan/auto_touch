from uiautomator import device as d
import time
import random

# 点亮屏幕
d.screen.on()
print(d.info) # 1920 * 1080


def toFixed(num, ndigits=2):
    return round(num, ndigits)


while 1:
    # android靠中间区域都是打开菜单，右边大概四分之一才能翻页
    x = random.uniform(800, 1050)
    y = random.uniform(1200, 1800)
    d.click(x, y)
    second = random.uniform(12, 30)
    time.sleep(second)
    print('点击坐标为(' + str(toFixed(x)) + ', ' + str(toFixed(y)) + '), ' + str(toFixed(second)) + '秒后再次点击')
