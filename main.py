from utils.yolov5_onnx import YOLOv5
from scrcpy_adb import ScrcpyADB
from game_control import GameControl
from game_action import GameAction
import queue
import os
from ui.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication
import sys


class AutoCleaningQueue(queue.Queue):
    def put(self, item, block=True, timeout=None):
        if self.full():
            self.get()  # 自动丢弃最旧的元素
        super().put(item, block, timeout)


if __name__ == '__main__':

    current_dir = os.path.dirname(os.path.abspath(__file__))
    pathOnnx = os.path.join(current_dir, "./utils/dnfm.onnx")
    pathButtonsJson = os.path.join(current_dir, "./buttons.json")
    image_queue = AutoCleaningQueue(maxsize=3)
    infer_queue = AutoCleaningQueue(maxsize=3)
    show_queue = AutoCleaningQueue(maxsize=3)

    # 初始化窗口
    app = QApplication(sys.argv)
    window = MainWindow()
    # 初始化各个组件
    client = ScrcpyADB(image_queue, max_fps=15)
    yolo = YOLOv5(pathOnnx, image_queue, infer_queue, window.onFrame)
    control = GameControl(client, pathButtonsJson)
    action = GameAction(control, infer_queue)
    # 显示窗口
    window.setComponents(client, yolo, action)
    window.resizeToDefault()
    window.show()
    app.exec_()
