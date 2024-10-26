import random

from .constants import TREE_TYPES
from .forest_tracker import ForestTracker

def on_deck_browser_will_render_content(deck_browser, content):
    forest_tracker = ForestTracker()
    forest = forest_tracker.config["forest"]
    
    forest_html = """
        <div id="forest-overview" style="
            position: absolute;
            width: 100%;
            height: 200px;
            background-color: #f0f0f0;
            padding: 10px;
            overflow: hidden;
            margin-top:2em;
        ">
            <h3>Your Anki Forest</h3>
    """
    
    placed_positions = []
    tree_size = 50
    padding = 10

    def is_overlapping(x, y):
        for px, py in placed_positions:
            if abs(px - x) < tree_size + padding and abs(py - y) < tree_size + padding:
                return True
        return False

    # Randomly place trees in the forest but make sure to keep the headline free and try not overlap with other trees
    for tree in forest:
        for _ in range(3):
            x = random.randint(0, 90)
            y = random.randint(40, 150)
            if not is_overlapping(x, y):
                break
        placed_positions.append((x, y))
        
        svg = TREE_TYPES[tree["type"]]["full"]
        tree_html = f'<div style="position: absolute; left: {x}%; top: {y}px; width:{tree_size}px; height:{tree_size}px;">{svg}</div>'
        forest_html += tree_html
    
    forest_html += "</div>"
    content.stats += forest_html