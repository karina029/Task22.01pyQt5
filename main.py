from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *
app = QApplication([])
my_win = QWidget()
my_win.resize(800, 400)
my_win.move(400, 400)
my_win.setWindowTitle("Task2")
btn = QPushButton()
text = QLabel("Дізнатися переможця прямо зараз!")
text2 = QLabel('Переможець може бути тільки один')
text.move(150, 50)
text2.move(150, -100)
text2 = QLabel()
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(text2, alignment=Qt.AlignCenter)
line.addWidget(btn, alignment=Qt.AlignCenter)
my_win.setLayout(line)
# Створити конструктор який буде на віхд приймати параметри кнопки
# Метод який буде приховувати кнопку
# Метод який буде відображати кнопку
# Метод який буде другувати кнопку
class Title:
    def __init__(self, x, y, title_text):
        self.x = x
        self.y = y
        self.title = title_text
        self.appearance = True
    def hide (self):
        self.appearance = False
        print(self.title, '- приховано')
    def print_info (self):
        print("Кнопка:", self.title)
        print("Розташування: ",'(' + str(self.x) + ',' + str(self.y) + ')')
        print("Видимість:", self.appearance)
    def show (self):
        self.appearance = True
        print(self.title, '- відображається')
title = Title(100,100,'btn')
btn.clicked.connect(title.print_info)
btn.clicked.connect(title.show)
my_win.show()
app.exec_()