import uiautomator2 as u2
import time
import random

d = u2.connect() # 通过USB adb链接
# d = u2.connect('192.168.1.104') # 通过ip地址连接
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
    d.long_click(x_center, y_center, 2)

