
import uiautomator2 as u2
import time
import os

#连接设备并打印
d=u2.connect()
print("设备列表：",d)


print(d.info)
d.info.get(' screenOn ')
screen =  True  #屏幕状态
if screen == True:
    d.screen_on()
    d.swipe_ext("up", 0.6)
    sleep.time
else:
    d.app_start("com.meizu.media.camera")








