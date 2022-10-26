#-------------------------------------#
#   调用摄像头或者视频进行检测
#   调用摄像头直接运行即可
#   调用视频可以将cv2.VideoCapture()指定路径
#   视频的保存并不难，可以百度一下看看
#-------------------------------------#
import time

import cv2
import numpy as np
from PIL import Image

from ssd import SSD

ssd = SSD()
capture = cv2.VideoCapture(0)
fps = 0.0

while(True):
    t1 = time.time()
    ref, frame = capture.read()
    frame = np.array(ssd.detect_image(frame))
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    fps = (fps + (1./(time.time()-t1))) / 2
    print("fps= %.2f"%(fps))
    frame = cv2.putText(frame, "fps= %.2f"%(fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("video",frame)
    c = cv2.waitKey(1) & 0xff
    if c == 27:
        capture.release()
        break
