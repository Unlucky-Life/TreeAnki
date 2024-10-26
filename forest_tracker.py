from aqt import mw
from .constants import REVIEWS_FOR_FULL_TREE
from .constants import TREE_TYPES

class ForestTracker:
    def __init__(self):
        self.config = self.load_config()
        
    def load_config(self):
        config = mw.addonManager.getConfig(__name__) or {}
        if not config:
            config = {
                "forest": [],  # List of completed trees
                "current_tree": {
                    "type": "oak",
                    "progress": 0
                },
                "total_reviews": 0
            }
            self.save_config(config)
        return config
    
    def save_config(self, config):
        mw.addonManager.writeConfig(__name__, config)
    
    def add_review(self):
        self.config["total_reviews"] += 1
        self.config["current_tree"]["progress"] += 1
        
        if self.config["current_tree"]["progress"] >= REVIEWS_FOR_FULL_TREE:
            # Plant completed tree in forest
            self.config["forest"].append({
                "type": self.config["current_tree"]["type"],
                "x": len(self.config["forest"]) * 50,
                "y": 200
            })
            self.config["current_tree"]["progress"] = 0
            
        self.save_config(self.config)
    
    def set_tree_type(self, tree_type):
        if tree_type in TREE_TYPES:
            self.config["current_tree"]["type"] = tree_type
            self.save_config(self.config)