from aqt import mw
from pathlib import Path
from .modularSprites import retrieve_sprites_info

REVIEWS_FOR_SMALL_TREE = 500
REVIEWS_FOR_FULL_TREE = 1000

ADDON_NAME = mw.addonManager.addonFromModule(__name__)
ADDON_PATH = Path(__file__).parents[0]
SPRITES_PATH = ADDON_PATH / "web" / "iframe" / "trees"

### Sources:
### Oak:
#  Made by SVG Repo: https://www.svgrepo.com/svg/57942/sprout
#  Made by SVG Repo: https://www.svgrepo.com/svg/475453/tree
#  Made by SVG Repo: https://www.svgrepo.com/svg/475465/tree
### Bush: 
#  Made by streetmix: https://github.com/streetmix/illustrations
#  Made by SVG Repo: https://www.svgrepo.com/svg/276098/bush
#  Made by SVG Repo: https://www.svgrepo.com/svg/3643/bush
### Flower:
#  Made by joypixels: https://github.com/joypixels/emojione
#  Made by SVG Repo: https://www.svgrepo.com/svg/244756/sprout
#  Made by SVG Repo: https://www.svgrepo.com/svg/244748/flower
###
TREE_DATA = retrieve_sprites_info(SPRITES_PATH)
TREE_TYPES = list(TREE_DATA.keys())