import uiautomator2 as u2
import time
import random
import sys

ip = ''

# 获取参数，作为ip
argv = sys.argv
if len(argv) > 1:
    ip = argv[1]

# 有ip则是通过wifi连接，否则通过usb adb连接
# 先尝试wifi连接
try:
    d = u2.connect(ip)
except:
    d = u2.connect()
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

