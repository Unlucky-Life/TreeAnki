from .constants import ADDON_NAME, REVIEWS_FOR_FULL_TREE
from .forest_tracker import ForestTracker
from aqt import mw
from aqt.webview import WebContent

def prepare_html(html, content, context):
    tracker = ForestTracker()
    stage = tracker.get_tree_stage()
    progress = tracker.config["current_tree"]["progress"]
    image_type = tracker.get_tree_info("image_type")
    treeType = tracker.get_tree_type()
    general_url = f"""/_addons/{ADDON_NAME}/web/iframe"""
    html_code = create_iframe_html(general_url, treeType, stage, progress, REVIEWS_FOR_FULL_TREE, "block", image_type)
    return html + html_code

def on_webview_will_set_content(web_content: WebContent, context) -> None:
    mw.addonManager.setWebExports(__name__, r"web/.*\.(css|js|jpg|gif|html|ttf|png|mp3)")
    web_content.css.append(f"/_addons/{ADDON_NAME}/web/iframe.css")
    web_content.js.append(f"/_addons/{ADDON_NAME}/web/toggleOpacity.js")

def create_iframe_html(general_url, treeType, stage, progress, max, display, image_type):
    html_code = """<div id="spacer">&nbsp;</div>"""
    html_code += f"""<div id="TreeWindow" class="draggable"><iframe id="Trefame" src='{general_url}/treeFrame.html?treeType={treeType}&stage={stage}&current={progress}&max={max}&image_type={image_type}' style="display:{display};"></iframe></div>"""
    html_code += """
        <script>
            const draggable = document.getElementById('TreeWindow');
            let isDragging = false;
            let offsetX, offsetY;

            // Retrieve saved coordinates from the CSS variables (if any)
            const savedX = getComputedStyle(document.documentElement).getPropertyValue('--window-left');
            const savedY = getComputedStyle(document.documentElement).getPropertyValue('--window-top');

            // Set initial position if saved coordinates exist
            if (savedX && savedY) {
                draggable.style.left = savedX;
                draggable.style.top = savedY;
            }

            // Mousedown-Event
            draggable.addEventListener('mousedown', (e) => {
                isDragging = true;
                offsetX = e.clientX - draggable.offsetLeft;
                offsetY = e.clientY - draggable.offsetTop;
                draggable.style.cursor = 'grabbing';
            });

            // Mousemove-Event
            window.addEventListener('mousemove', (e) => {
                if (!isDragging) return;

                const x = e.clientX - offsetX;
                const y = e.clientY - offsetY;

                draggable.style.left = `${x}px`;
                draggable.style.top = `${y}px`;
            });

            // Mouseup-Event
            window.addEventListener('mouseup', () => {
                if (!isDragging) return;
                isDragging = false;
                draggable.style.cursor = 'move';

                // Save the new position in the global CSS variables
                const currentX = draggable.offsetLeft;
                const currentY = draggable.offsetTop;

                // Set the new coordinates as global CSS variables
                document.documentElement.style.setProperty('--window-left', `${currentX}px`);
                document.documentElement.style.setProperty('--window-top', `${currentY}px`);
            });
        </script>
    """

    return html_code