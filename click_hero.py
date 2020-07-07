from uiautomator import device as d
import time
import random

# 点亮屏幕
d.screen.on()
info = d.info
print(info)  # 1920 * 1080

screen_height = info.get('displayHeight')
screen_width = info.get('displayWidth')

while 1:
    x_center = screen_width / 2
    y_center = screen_height / 2 - 100

    # 雷戒
    # d.click(x_center, y_center)
    # d.click(x_center, y_center - 50)
    # d.click(x_center, y_center - 100)

    # 火戒
    # time.sleep(.15)
    # d.click(x_center, y_center)

    # 冰戒
    time.sleep(2)
    d.swipe(x_center, y_center, x_center, y_center, 100);

