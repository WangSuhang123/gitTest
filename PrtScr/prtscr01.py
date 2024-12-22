import tkinter as tk
from PIL import ImageGrab
import keyboard

def select_area_and_screenshot():
    # 创建全屏透明窗口
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # 全屏
    root.attributes('-alpha', 0.3)  # 半透明
    root.config(bg='black')

    start_x = start_y = end_x = end_y = None

    def on_mouse_press(event):
        nonlocal start_x, start_y
        start_x, start_y = event.x, event.y

    def on_mouse_release(event):
        nonlocal start_x, start_y, end_x, end_y
        end_x, end_y = event.x, event.y

        # 关闭窗口
        root.destroy()

        # 计算截图区域
        left = min(start_x, end_x)
        top = min(start_y, end_y)
        right = max(start_x, end_x)
        bottom = max(start_y, end_y)

        # 截取屏幕并保存
        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
        filename = "screenshot.png"
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")

    # 绑定鼠标事件
    root.bind("<Button-1>", on_mouse_press)  # 按下鼠标左键
    root.bind("<ButtonRelease-1>", on_mouse_release)  # 释放鼠标左键

    # 启动 Tkinter 窗口
    root.mainloop()

# 监听快捷键 Ctrl+Shift+S
keyboard.add_hotkey('ctrl+shift+s', select_area_and_screenshot)

print("Press Ctrl+Shift+S to take a screenshot of a selected area.")
print("Press Ctrl+C to exit the program.")

# 阻塞主线程等待快捷键触发
keyboard.wait()
