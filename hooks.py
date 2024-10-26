
from anki.hooks import addHook, wrap
from aqt import gui_hooks
from .browser import on_deck_browser_will_render_content
from .reviewer import add_tree_to_reviewer, remove_tree_from_reviewer, on_review_complete, state_change_hk
from .menu import setup_menu

def setupHooks():
    addHook("profileLoaded", setup_menu)
    gui_hooks.reviewer_will_end.append(remove_tree_from_reviewer)
    gui_hooks.state_did_change.append(state_change_hk)
    gui_hooks.deck_browser_will_render_content.append(on_deck_browser_will_render_content)
    gui_hooks.reviewer_did_show_question.append(add_tree_to_reviewer)
    gui_hooks.reviewer_did_answer_card.append(on_review_complete)