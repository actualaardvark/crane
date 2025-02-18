import cv2
import os

CAM = cv2.VideoCapture(0)


def makepathifnotexist(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


framecounter: int = 0
while True:
    ret, frame = CAM.read()
    frame_height, frame_width, _ = frame.shape
    decimate_factor = 2
    decimate_point: tuple[int, int] = (
        int(frame_width / decimate_factor),
        int(frame_height / decimate_factor),
    )
    print(decimate_point)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    makepathifnotexist(f"./pipeline_debug/{framecounter}")
    cv2.imwrite(f"./pipeline_debug/{framecounter}/grayscale.png", gray)
    decimate = cv2.resize(gray, decimate_point, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(f"./pipeline_debug/{framecounter}/decimate.png", decimate)
    # framecounter += 1

# When everything done, release the capture
CAM.release()

cv2.imwrite("./pipeline_debug/grayscale.png", SOURCE_IMAGE)
# decimated = cv2.resize(src=SOURCE_IMAGE, 128, 128)
