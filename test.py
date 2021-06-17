import sys
import subprocess

try:
    import spotdl
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'spotdl'])
