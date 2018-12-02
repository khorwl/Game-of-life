from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import (QWidget, QPushButton, QDesktopWidget, QInputDialog)

from timer import *

from automaton import Automaton
from primitives.field import *


class Window(QWidget):

    def __init__(self):
        super().__init__()

        text, ok = QInputDialog.getText(self, ' ', 'Enter height and width:')
        if ok:
            try:
                import re
                height, width = map(int, re.split(' |,|x|X|:|;', text))
                self._robot = Automaton(Field(height, width))
            except:
                exit()
        else:
            exit()

        self._init_ui()

        self.run = False
        Timer(self.on_timer, 0.2)

    def center(self):
        form_window = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        form_window.moveCenter(center_point)
        self.move(form_window.topLeft())

    def _init_ui(self):
        self.setFixedSize(700, 490)
        self.center()
        self.setWindowTitle('Game of Life')

        generate_field = QPushButton('Generate field', self)
        generate_field.resize(100, 40)
        generate_field.move(560, 70)

        start_button = QPushButton('Start', self)
        start_button.resize(100, 40)
        start_button.move(560, 140)

        stop_button = QPushButton('Stop', self)
        stop_button.resize(100, 40)
        stop_button.move(560, 210)

        next_generation = QPushButton('Next', self)
        next_generation.resize(100, 40)
        next_generation.move(560, 280)

        next_steps = QPushButton('Next steps', self)
        next_steps.resize(100, 40)
        next_steps.move(560, 350)

        previous_generation = QPushButton('Previous', self)
        previous_generation.resize(100, 40)
        previous_generation.move(560, 420)

        generate_field.clicked.connect(self.on_generate_field)
        start_button.clicked.connect(self.on_start_button)
        stop_button.clicked.connect(self.on_stop_button)
        next_generation.clicked.connect(self.on_next_button)
        next_steps.clicked.connect(self.on_next_steps)
        # create_dict.clicked.connect(self.on_create_dict)
        previous_generation.clicked.connect(self.on_previous_generation)

        self.show()

    def on_previous_generation(self):
        self.run = False
        self._robot.set_previous_position()
        self.update()

    def on_generate_field(self):
        self.run = False
        self._robot.generate_first_generation()
        self.update()

    def on_start_button(self):
        self.run = True

    def on_stop_button(self):
        self.run = False

    def on_next_button(self):
        self.set_next()

    def on_next_steps(self):
        self.run = False
        text, ok = QInputDialog.getText(self, ' ', 'Enter count steps:')
        if ok:
            count_steps = int(text)
            for i in range(count_steps):
                self._robot.set_next_generation()
        self.update()

    def set_next(self):
        self._robot.set_next_generation()
        self.update()

    def on_timer(self):
        if self.run:
            self.set_next()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_rectangles(qp)
        qp.end()

    def mousePressEvent(self, event):
        x = (QPoint(event.pos()).x() - 50) // 20
        y = (QPoint(event.pos()).y() - 50) // 20

        if x < 0 or y < 0 or x >= self._robot.field.width or y >= self._robot.field.height:
            return

        self._robot.field.set(y, x, Cell((self._robot.field.get(y, x).value + 1) % 4))
        self.update()

    def draw_rectangles(self, qp):
        qp.setPen(QColor(0, 0, 0))

        for i in range(self._robot.field.height):
            for j in range(self._robot.field.width):
                if self._robot.field.get(i, j) == Cell.ALIVE:
                    qp.setBrush(QColor("#ff8597"))
                    qp.drawRect(50 + j * 20, 50 + i * 20, 20, 20)
                elif self._robot.field.get(i, j) == Cell.DEAD:
                    qp.setBrush(QColor(255, 255, 255))
                    qp.drawRect(50 + j * 20, 50 + i * 20, 20, 20)
                elif self._robot.field.get(i, j) == Cell.ALWAYS_ALIVE:
                    qp.setBrush(QColor("#32cd32"))  # 32cd32186318
                    qp.drawRect(50 + j * 20, 50 + i * 20, 20, 20)
                else:
                    qp.setBrush(QColor("#030804"))
                    qp.drawRect(50 + j * 20, 50 + i * 20, 20, 20)
