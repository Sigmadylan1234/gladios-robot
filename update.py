import subprocess
import os
import sys

# Get path to this repo
repo_dir = os.path.dirname(os.path.abspath(__file__))
main_script = os.path.join(repo_dir, "main.py")

print("🔄 Pulling latest updates from GitHub...")
subprocess.run(["git", "pull"], cwd=repo_dir)

# Restart the GLaDOS script after pulling
print("🚀 Launching GLaDOS AI...")
python_exe = sys.executable  # Path to python.exe
subprocess.run([python_exe, main_script])
