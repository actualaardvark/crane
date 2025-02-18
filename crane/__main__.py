import logging
import os
import time

import cv2

LOGGER = logging.getLogger(__name__)
DECIMATION_FACTOR = 2
logging.basicConfig(filename=f"{__name__}.log", level=logging.INFO)
CAM = cv2.VideoCapture(0)
ret, frame = CAM.read()
frame_height, frame_width, _ = frame.shape
decimate_point: tuple[int, int] = (
    int(frame_width / DECIMATION_FACTOR),
    int(frame_height / DECIMATION_FACTOR),
)
VIDEO = cv2.VideoWriter(
    "./pipeline_debug/video.avi", -1, 1, (frame_height, frame_width)
)


def makepathifnotexist(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


framecounter: int = 0
while True:
    start = time.time()
    ret, frame = CAM.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    makepathifnotexist(f"./pipeline_debug/{framecounter}")
    cv2.imwrite(f"./pipeline_debug/{framecounter}/grayscale.png", gray)
    decimate = cv2.resize(gray, decimate_point, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(f"./pipeline_debug/{framecounter}/decimate.png", decimate)
    grad_x, grad_y = (
        cv2.Sobel(
            decimate,
            cv2.CV_16S,
            1,
            0,
            ksize=3,
            scale=1,
            delta=0,
            borderType=cv2.BORDER_DEFAULT,
        ),
        cv2.Sobel(
            decimate,
            cv2.CV_16S,
            0,
            1,
            ksize=3,
            scale=1,
            delta=0,
            borderType=cv2.BORDER_DEFAULT,
        ),
    )

    abs_grad_x, abs_grad_y = (cv2.convertScaleAbs(grad_x), cv2.convertScaleAbs(grad_y))
    sobeled = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    cv2.imwrite(f"./pipeline_debug/{framecounter}/sobeled.png", sobeled)
    VIDEO.write(sobeled)
    end = time.time()
    print(end - start)
    # framecounter += 1

# when everything done, release the capture
CAM.release()
