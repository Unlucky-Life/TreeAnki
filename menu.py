from aqt.qt import *
from aqt import mw
from .gui.overview import ForestOverviewWindow

def show_forest_overview():
    if hasattr(mw, 'forest_overview'):
        mw.forest_overview.refresh()
        mw.forest_overview.show()
        mw.forest_overview.raise_()
    else:
        mw.forest_overview = ForestOverviewWindow()
        mw.forest_overview.show()

def setup_menu():
    forest_action = QAction("Forest Overview", mw)
    forest_action.setShortcut("Ctrl+Shift+F")
    forest_action.triggered.connect(show_forest_overview)
    
    tools_menu = mw.form.menuTools
    tools_menu.addSeparator()
    tools_menu.addAction(forest_action)