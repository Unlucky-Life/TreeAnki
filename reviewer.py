from aqt.qt import *
from aqt import mw
from .forest_tracker import ForestTracker

def remove_tree_from_reviewer():
    if hasattr(mw.reviewer, 'tree_widget') and mw.reviewer.tree_widget:
        # Stop the update timer before cleanup
        mw.reviewer.tree_widget.update_timer.stop()
        mw.reviewer.tree_widget.hide()
        mw.reviewer.tree_widget.deleteLater()
        mw.reviewer.tree_widget = None

def on_review_complete(reviewer, card, ease):
    forest_tracker = ForestTracker()
    forest_tracker.add_review()
    
    # Force immediate update of the tree widget
    if hasattr(reviewer, 'tree_widget') and reviewer.tree_widget:
        reviewer.tree_widget.update()
        reviewer.tree_widget.updatePosition()
    
def state_change_hk(new_state, old_state):
    if old_state == "review":
        remove_tree_from_reviewer()