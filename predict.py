
import cv2
from ssd import SSD

ssd = SSD()

while True:
    img = input('Input image filename:')
    try:
        """
        用PIL处理图像在trt下检测效果很差
        """
        image = cv2.imread(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = ssd.detect_image(image)
        r_image.save("img.jpg")
        r_image.show()
