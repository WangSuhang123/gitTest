import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent, QPixmap, QPainter
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QScreen


class CaptureProgram(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screenshot Tool")
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()

    def init_ui(self):
        # UI setup
        self.label = QLabel("Press Ctrl + Alt + S to take a screenshot", self)
        self.label.setGeometry(50, 50, 300, 50)
        self.label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(self.label)

    def keyPressEvent(self, event: QKeyEvent):
        """监听Ctrl + Alt + Q的按键事件"""
        if event.key() == Qt.Key_S and event.modifiers() == (Qt.ControlModifier | Qt.AltModifier):
            self.startCaptureImage()

    def startCaptureImage(self):
        """开始截图"""
        capture_image = self.capture_screen()
        self.onCompleteCapture(capture_image)

    def capture_screen(self):
        """进行全屏截图"""
        screen = QApplication.primaryScreen()
        if screen:
            capture_pixmap = screen.grabWindow(0)
            return capture_pixmap
        return QPixmap()

    def onCompleteCapture(self, capture_image: QPixmap):
        """在界面上显示截图"""
        self.label.setPixmap(capture_image.scaled(self.label.size(), Qt.AspectRatioMode.KeepAspectRatio))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CaptureProgram()
    main_window.show()
    sys.exit(app.exec())
