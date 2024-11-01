import random
from .constants import TREE_TYPES
from .forest_tracker import ForestTracker

def on_deck_browser_will_render_content(deck_browser, content):
    forest_tracker = ForestTracker()
    forest = forest_tracker.config["forest"]
    
    forest_html = """
        <div id="forest-overview" style="
            position: relative;
            width: 100%;
            height: 200px;
            padding: 10px;
            overflow: hidden;
            margin-top: 2em;
            background-color: #f0f0f0;
        ">
            <h3>Your Anki Forest</h3>
    """
    
    container_width = 1000  # Assuming a fixed width for the container
    container_height = 200
    tree_size = 50
    padding = 10
    
    # Create a grid to track occupied positions
    grid = [[False for _ in range(container_width // tree_size)] for _ in range(container_height // tree_size)]
    
    for tree in forest:
        placed = False
        for _ in range(10):  # Try 10 times to place the tree
            row = random.randint(0, (container_height // tree_size) - 1)
            col = random.randint(0, (container_width // tree_size) - 1)
            
            if not grid[row][col]:
                x = col * tree_size + random.randint(-padding, padding)
                y = row * tree_size + random.randint(-padding, padding)
                
                # Ensure the tree is within bounds
                x = max(0, min(x, container_width - tree_size))
                y = max(0, min(y, container_height - tree_size))
                
                grid[row][col] = True
                svg = TREE_TYPES[tree["type"]]["full"]
                tree_html = f'<div style="position: absolute; left: {x}px; top: {y}px; width: {tree_size}px; height: {tree_size}px;">{svg}</div>'
                forest_html += tree_html
                placed = True
                break
        
        if not placed:
            # If we couldn't place the tree in the grid, place it randomly
            x = random.randint(0, container_width - tree_size)
            y = random.randint(0, container_height - tree_size)
            svg = TREE_TYPES[tree["type"]]["full"]
            tree_html = f'<div style="position: absolute; left: {x}px; top: {y}px; width: {tree_size}px; height: {tree_size}px;">{svg}</div>'
            forest_html += tree_html
    
    forest_html += "</div>"
    content.stats += forest_html