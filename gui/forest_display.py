from aqt.qt import *
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtCore import QByteArray, QRectF
from PyQt6.QtGui import QPainter, QColor
from ..forest_tracker import ForestTracker
from ..constants import TREE_TYPES

class ForestDisplayWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.forest_tracker = ForestTracker()
        self.setMinimumHeight(200)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        num_trees = len(self.forest_tracker.config["forest"])
        required_width = max(600, (num_trees + 1) * 60)
        self.setMinimumWidth(required_width)
        
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor("#90A4AE"))
        painter.drawRect(0, 200, self.width(), 50)
        
        for i, tree in enumerate(self.forest_tracker.config["forest"]):
            x = i * 60 + 30
            y = 150 + (i % 3) * 10
            
            svg = TREE_TYPES[tree["type"]]["full"]
            renderer = QSvgRenderer(QByteArray(svg.encode()))
            renderer.render(painter, QRectF(x, y, 50, 50))