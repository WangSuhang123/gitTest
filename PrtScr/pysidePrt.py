import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
)
from PySide6.QtGui import QPixmap, QPainter, QColor, QImage
from PySide6.QtCore import Qt, QRectF
from PIL import ImageGrab


class SelectionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.start_point = None
        self.end_point = None
        self.setWindowTitle("Select Area")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowState(Qt.WindowFullScreen)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 使用 PIL 捕获屏幕内容
        screen_image = ImageGrab.grab()
        self.background_pixmap = QPixmap.fromImage(
            QImage(
                screen_image.tobytes("raw", "RGB"),
                screen_image.width,
                screen_image.height,
                QImage.Format_RGB888,
            )
        )

    def paintEvent(self, event):
        """绘制半透明灰色背景和选取区域"""
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background_pixmap)  # 绘制屏幕截图背景

        # 绘制半透明灰色覆盖层
        painter.setBrush(QColor(128, 128, 128, 128))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

        if self.start_point and self.end_point:
            # 清除选中区域上的灰色覆盖
            # 显示选取区域的桌面截图
            selection_rect = QRectF(self.start_point, self.end_point)
            painter.setCompositionMode(QPainter.CompositionMode_Clear)
            painter.fillRect(selection_rect, Qt.transparent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.position()

    def mouseMoveEvent(self, event):
        if self.start_point:
            self.end_point = event.position()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_point = event.position()
            self.hide()
            self.capture_area()

    def capture_area(self):
        if self.start_point and self.end_point:
            left = min(self.start_point.x(), self.end_point.x())
            top = min(self.start_point.y(), self.end_point.y())
            right = max(self.start_point.x(), self.end_point.x())
            bottom = max(self.start_point.y(), self.end_point.y())
            screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
            self.show_preview(screenshot)

    def show_preview(self, image):
        self.preview_window = PreviewWindow(image)
        self.preview_window.show()


class PreviewWindow(QWidget):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.setWindowTitle("Screenshot Preview")
        self.setFixedSize(image.width, image.height + 50)

        # Convert PIL image to QPixmap
        image_data = self.image.tobytes("raw", "RGB")
        qimage = QImage(image_data, self.image.width, self.image.height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)

        # Create layout
        self.layout = QVBoxLayout()
        self.image_label = QLabel()
        self.image_label.setPixmap(pixmap)
        self.layout.addWidget(self.image_label)

        # Add Save and Cancel buttons
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")
        self.layout.addWidget(self.save_button)
        self.layout.addWidget(self.cancel_button)

        # Connect buttons
        self.save_button.clicked.connect(self.save_image)
        self.cancel_button.clicked.connect(self.close)

        self.setLayout(self.layout)

    def save_image(self):
        options = QFileDialog.Options()
        filepath, _ = QFileDialog.getSaveFileName(self, "Save Screenshot", "", "PNG Files (*.png);;All Files (*)", options=options)
        if filepath:
            self.image.save(filepath)
            self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screenshot Tool")
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()

    def init_ui(self):
        self.label = QLabel("Press the button below to start screenshotting", self)
        self.label.setGeometry(50, 50, 300, 50)

        self.button = QPushButton("Take Screenshot", self)
        self.button.setGeometry(150, 150, 100, 50)
        self.button.clicked.connect(self.start_selection)

    def start_selection(self):
        self.selection_window = SelectionWindow()
        self.selection_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
