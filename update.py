import subprocess
import os

repo_dir = os.path.dirname(os.path.abspath(__file__))
print("Updating Git repo in:", repo_dir)
subprocess.run(["git", "pull"], cwd=repo_dir)
