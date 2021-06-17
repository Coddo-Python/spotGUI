import webview
import subprocess
import sys
import json


def main():
    # Activate Loading Screen
    with open("pages/html/loading.html", "r", encoding='utf-8') as f:
        window.load_html(f.read())
    with open("pages/css/loading.css", "r", encoding='utf-8') as f:
        window.load_css(f.read())
    # Load stuff
    try:
        import spotdl
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'spotdl'])
    # Load Data (TODO later)
    # Deactivate Loading Screen
    window.evaluate_js("document.documentElement.style.setProperty('--animation', 'fadeOut forwards 0.8s');")


window = webview.create_window(title="SpotGUI")
webview.start(func=main)
