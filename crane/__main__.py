import numpy as np
import cv2

SOURCE_IMAGE = cv2.imread("./input.png", cv2.IMREAD_GRAYSCALE)
CAM = cv2.VideoCapture(0)

frame_width = int(CAM.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(CAM.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    # Capture frame-by-frame
    ret, frame = CAM.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imwrite("./1.png", gray)

# When everything done, release the capture
CAM.release()

cv2.imwrite("./pipeline_debug/grayscale.png", SOURCE_IMAGE)
# decimated = cv2.resize(src=SOURCE_IMAGE, 128, 128)
