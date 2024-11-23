from .constants import ADDON_NAME, REVIEWS_FOR_FULL_TREE
from .forest_tracker import ForestTracker
from aqt import mw
from aqt.webview import WebContent

def prepare_html(html, content, context):
    tracker = ForestTracker()
    stage = tracker.get_tree_stage()
    progress = tracker.config["current_tree"]["progress"]
    treeType = tracker.get_tree_type_number()
    general_url = f"""/_addons/{ADDON_NAME}/web/iframe"""
    html_code = create_iframe_html(general_url, treeType, stage, progress, REVIEWS_FOR_FULL_TREE, "block")
    return html + html_code

def on_webview_will_set_content(web_content: WebContent, context) -> None:
    mw.addonManager.setWebExports(__name__, r"web/.*\.(css|js|jpg|gif|html|ttf|png|mp3)")
    web_content.css.append(f"/_addons/{ADDON_NAME}/web/iframe.css")
    web_content.js.append(f"/_addons/{ADDON_NAME}/web/toggleOpacity.js")

def create_iframe_html(general_url, treeType, stage, progress, max, display):
    html_code = """<div id="spacer">&nbsp;</div>"""
    html_code += f"""<div id="TreeWindow"><iframe id="Trefame" src='{general_url}/treeFrame.html?treeType={treeType}&stage={stage}&current={progress}&max={max}' width=240px height=280px style="display:{display};"></iframe></div>"""
    return html_code