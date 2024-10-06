import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)  # Set maxHands to 2 to detect both hands
offset = 20
imgSize = 300
counter = 0

folder = r"C:\Users\HP\Desktop\SIH\Data\P"

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        for hand in hands:  # Iterate over the detected hands
            x, y, w, h = hand['bbox']

            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

            imgCrop = img[y-offset:y + h + offset, x-offset:x + w + offset]
            imgCropShape = imgCrop.shape

            aspectRatio = h / w

            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize-wCal)/2)
                imgWhite[:, wGap: wCal + wGap] = imgResize

            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap: hCal + hGap, :] = imgResize

            # Display the cropped and processed image for each hand
            cv2.imshow(f'ImageCrop_{counter}', imgCrop)
            cv2.imshow(f'ImageWhite_{counter}', imgWhite)

        # Save the entire frame (with both hands) when 's' is pressed
        key = cv2.waitKey(1)
        if key == ord("s"):
            counter += 1
            cv2.imwrite(f'{folder}/Image_{time.time()}_{counter}.jpg', img)  # Save the entire frame
            print(f'Saved Image {counter}')
    
    cv2.imshow('Image', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()