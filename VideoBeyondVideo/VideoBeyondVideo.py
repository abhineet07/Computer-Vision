import cv2
import numpy as np

myVideo = cv2.VideoCapture("D:\\Videos\\sample.mp4")

cap = cv2.VideoCapture(0)
_, frame = cap.read()
# print(frame.shape())

while True:
    _, frame = cap.read()
    o = frame.copy()
    _, myframes = myVideo.read()
    myresize = cv2.resize(myframes, (640, 480))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    bgr = [40, 158, 16]
    minrange = np.array([50, 50, 50])
    maxrange = np.array([70, 255, 255])
    thresh = 40

    minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
    maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

    mask = cv2.inRange(hsv, minrange, maxrange)
    mask2 = cv2.bitwise_not(mask)

    vfx1 = cv2.bitwise_and(myresize, myresize, mask=mask)
    vfx2 = cv2.bitwise_and(o, o, mask=mask2)
    vfx3 = cv2.add(vfx1, vfx2)

    cv2.imshow('vfx3', vfx3)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

