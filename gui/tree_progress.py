from aqt.qt import *
from aqt import mw
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtCore import QByteArray, QRectF
from PyQt6.QtGui import QPainter
from ..forest_tracker import ForestTracker
from ..constants import REVIEWS_FOR_SMALL_TREE, REVIEWS_FOR_FULL_TREE, TREE_TYPES

class TreeProgressWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.forest_tracker = ForestTracker()
        self.setFixedSize(100, 150)
        
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.updatePosition)
        self.update_timer.start(50)
    
    def updatePosition(self):
        if mw and mw.reviewer and mw.reviewer.bottom:
            bottom_web = mw.reviewer.bottom.web
            if bottom_web:
                bottom_rect = bottom_web.geometry()
                main_window_rect = mw.geometry()
                
                x = self.width() + 5
                y = main_window_rect.height() - bottom_rect.height() - self.height() - 10
                
                self.move(x, y)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        self.forest_tracker = ForestTracker()
        current_tree = self.forest_tracker.config["current_tree"]
        progress = current_tree["progress"]
        tree_type = current_tree["type"]
        
        if progress < REVIEWS_FOR_SMALL_TREE:
            svg = TREE_TYPES[tree_type]["sprout"]
        elif progress < REVIEWS_FOR_FULL_TREE:
            svg = TREE_TYPES[tree_type]["small"]
        else:
            svg = TREE_TYPES[tree_type]["full"]
            
        renderer = QSvgRenderer(QByteArray(svg.encode()))
        renderer.render(painter, QRectF(0, 0, 100, 100))
        
        painter.drawText(QRect(0, 110, 100, 20), 
                        Qt.AlignmentFlag.AlignCenter, 
                        f"{progress}/{REVIEWS_FOR_FULL_TREE}")