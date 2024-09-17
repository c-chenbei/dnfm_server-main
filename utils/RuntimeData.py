from config import WINDOW_WIDTH

DEVICE_WIDTH: int
DEVICE_HEIGHT: int
RATE: float
SCALE: float = 0


def setDeviceResolution(width: int, height: int):
    global DEVICE_WIDTH, DEVICE_HEIGHT, RATE, SCALE
    DEVICE_WIDTH = width
    DEVICE_HEIGHT = height
    RATE = DEVICE_HEIGHT/DEVICE_WIDTH
    if WINDOW_WIDTH != 0:
        SCALE = WINDOW_WIDTH/DEVICE_WIDTH
    else:
        SCALE = 1


def log():
    global DEVICE_WIDTH, DEVICE_HEIGHT, RATE, SCALE
    print(f"手机分辨率:{DEVICE_HEIGHT}*{DEVICE_WIDTH}, RATE:{RATE}, SCALE:{SCALE}")
