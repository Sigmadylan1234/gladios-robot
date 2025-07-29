import subprocess
import os
import sys

# Get the folder where this script is located
repo_dir = os.path.dirname(os.path.abspath(__file__))

print("🔄 Updating GitHub repository in:", repo_dir)
subprocess.run(["git", "pull"], cwd=repo_dir)

# List of required Python packages
required_packages = [
    "speechrecognition",
    "pyttsx3",
    "pyaudio",
    "requests"
]

print("📦 Installing required Python packages...")
for package in required_packages:
    subprocess.run([sys.executable, "-m", "pip", "install", package])
