from aqt.qt import *
from .tree_selection import TreeSelectionDialog
from .tree_progress import TreeProgressWidget
from .forest_display import ForestDisplayWidget
from ..forest_tracker import ForestTracker
from ..constants import REVIEWS_FOR_FULL_TREE

class ForestOverviewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.forest_tracker = ForestTracker()
        self.setWindowTitle("Your Anki Forest")
        self.setup_ui()
        
    def setup_ui(self):
        self.setMinimumSize(650, 500)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        # Stats section
        stats_group = QGroupBox("Forest Statistics")
        stats_layout = QHBoxLayout()
        
        total_trees = len(self.forest_tracker.config["forest"])
        current_progress = self.forest_tracker.config["current_tree"]["progress"]
        total_reviews = self.forest_tracker.config["total_reviews"]
        
        stats_layout.addWidget(QLabel(f"Total Trees: {total_trees}"))
        stats_layout.addWidget(QLabel(f"Total Reviews: {total_reviews}"))
        stats_layout.addWidget(QLabel(
            f"Current Tree Progress: {current_progress}/{REVIEWS_FOR_FULL_TREE}"))
        
        stats_group.setLayout(stats_layout)
        layout.addWidget(stats_group)
        
        # Tree selection
        tree_controls = QHBoxLayout()
        select_button = QPushButton("Select Next Tree")
        select_button.clicked.connect(self.show_tree_selection)
        tree_controls.addWidget(select_button)
        
        # Current tree preview
        #current_tree_label = QLabel("Current Growing Tree:")
        #tree_controls.addWidget(current_tree_label)
        #self.current_tree_widget = TreeProgressWidget()
        #self.current_tree_widget.setFixedSize(100, 150)
        #tree_controls.addWidget(self.current_tree_widget) 
        #tree_controls.addStretch()
        #layout.addLayout(tree_controls)
        
        # Forest display
        forest_scroll = QScrollArea()
        forest_scroll.setWidgetResizable(True)
        forest_scroll.setMinimumHeight(200)
        
        self.forest_display = ForestDisplayWidget()
        forest_scroll.setWidget(self.forest_display)
        layout.addWidget(forest_scroll)
        
        self.setLayout(layout)
    
    def show_tree_selection(self):
        dialog = TreeSelectionDialog(self)
        if dialog.exec():
            selected_tree = dialog.get_selected_tree()
            self.forest_tracker.set_tree_type(selected_tree)
            #self.current_tree_widget.update()
            self.forest_display.update()
    
    def refresh(self):
        #self.current_tree_widget.update()
        self.forest_display.update()
