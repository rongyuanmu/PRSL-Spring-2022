import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import numpy as np
import mediapipe as mp

cap = cv2.VideoCapture(0)
wid = 640
hei = 480
cap.set(4, wid)  # 设置显示宽度
cap.set(3, hei)  # 设置显示高度
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()
bk_image = cv2.imread("background.jpg")
bk_image = cv2.resize(bk_image, [wid, hei])

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, bk_image, threshold=0.9)

    # # foreground clustering
    # vectorized = imgOut.reshape((-1,3))
    # vectorized = np.float32(vectorized)

    # # perform kmeans clustering
    # ## 停止条件
    # criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1)
    # ## 初始化中心数和尝试的次数
    # K = 3
    # attempts=4
    # _,label,center = cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
    # center = np.uint8(center)
    # label.flatten().shape,center.shape
    # res = center[label.flatten()]
    # imgOut = res.reshape((imgOut.shape))

    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    _, imgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))

    cv2.imshow("Image", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break