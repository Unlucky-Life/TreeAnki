     
def on_deck_browser_will_render_content(deck_browser, content):
    forest_html = """
        <div id="forest-overview" style="
            position: absolute;
            bottom: 20px;
            width: 100%;
            height: 200px;
            background-color: #f0f0f0;
            padding: 10px;
        ">
            <h3>Your Anki Forest</h3>
        </div>
    """
    content.stats += forest_html