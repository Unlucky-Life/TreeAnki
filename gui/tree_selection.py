from aqt.qt import *
from ..forest_tracker import ForestTracker
from ..constants import TREE_TYPES

class TreeSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.forest_tracker = ForestTracker()
        self.setup_ui()
        
    def setup_ui(self):
        self.setWindowTitle("Select Your Next Tree")
        layout = QVBoxLayout()
        
        # Create radio buttons for each tree type
        self.tree_buttons = {}
        for tree_type in TREE_TYPES.keys():
            btn = QRadioButton(tree_type.capitalize())
            if tree_type == self.forest_tracker.config["current_tree"]["type"]:
                btn.setChecked(True)
            self.tree_buttons[tree_type] = btn
            layout.addWidget(btn)
        
        # Add OK button
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)
        
        self.setLayout(layout)
    
    def get_selected_tree(self):
        for tree_type, btn in self.tree_buttons.items():
            if btn.isChecked():
                return tree_type
        return "AppleTree"  # Default