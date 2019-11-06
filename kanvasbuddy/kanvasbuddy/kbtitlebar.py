# The KanvasBuddy Krita plugin is licensed under CC BY-NC-SA 4.0

# You are free to:
# Share — copy and redistribute the material in any medium or format
# Adapt — remix, transform, and build upon the material

# Under the following terms:
# Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
# NonCommercial — You may not use the material for commercial purposes.
# ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.
# No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QToolButton, QStyle
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt

class KBTitleBar(QWidget):

    def __init__(self, parent):
        super(KBTitleBar, self).__init__(parent)
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(2, 1, 2, 1)

        self.title = QLabel("KanvasBuddy")
        font = self.font()
        font.setPixelSize(9)
        self.title.setFont(font)
        self.title.setStyleSheet("""
            color: grey;
        """)

        self.btn_close = QToolButton()
        self.btn_close.setFixedSize(10, 10)
        self.btn_close.setIconSize(QSize(7,7))
        self.btn_close.clicked.connect(self.parent.close)
        self.btn_close.setIcon(parent.style().standardIcon(QStyle.SP_DockWidgetCloseButton))

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_close)
        self.setLayout(self.layout)

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False