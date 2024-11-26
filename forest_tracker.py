from aqt import mw
from .constants import REVIEWS_FOR_FULL_TREE
from .constants import TREE_TYPES
from .constants import TREE_DATA
from .utils import get_tree_info_by_key

class ForestTracker:
    def __init__(self):
        self.config = self.load_config()
        self.tree_data = TREE_DATA
        
    def load_config(self):
        config = mw.addonManager.getConfig(__name__) or {}
        if not config:
            config = {
                "forest": [],  # List of completed trees
                "current_tree": {
                    "type": "AppleTree",
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
            
    def reload_config(self):
        self.config = self.load_config()

    def get_tree_stage(self):
        # Calculate the current stage based on progress
        progress = self.config["current_tree"]["progress"]
        stage_size = REVIEWS_FOR_FULL_TREE / self.get_tree_info("image_count")
        stage = min(self.get_tree_info("image_count"), max(1, int(progress / stage_size) + 1))
        return stage
    
    def get_tree_type(self):
        # Get the tree type string from config
        return self.config["current_tree"]["type"]
    
    def get_tree_info(self, key):
        # Get the image type for the current tree
        tree_type = self.get_tree_type()
        return get_tree_info_by_key(self.tree_data, tree_type, key)