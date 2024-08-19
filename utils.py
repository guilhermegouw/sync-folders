import os
import shutil
import subprocess
import json


CONNECTIONS_FILE = "connections.json"

def copy_folder(src, dst):
    """Copy all files and directories from src to dst."""
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

def save_connection(config):
    """Save the configuration to the JSON file."""
    with open(CONNECTIONS_FILE, 'w') as file:
        json.dump(config, file, indent=4)


def git_pull(repo_path):
    """Pull the latest changes from the remote repository and check for conflicts."""
    try:
        result = subprocess.run(['git', 'pull'], cwd=repo_path, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if "CONFLICT" in result.stdout.decode() or "CONFLICT" in result.stderr.decode():
            print("Merge conflicts detected! Please resolve them manually in the repository.")
    except subprocess.CalledProcessError:
        print("Failed to pull the latest changes. Please check the repository status.")

def git_commit_and_push(repo_path):
    """Commit and push changes to the remote repository."""
    try:
        subprocess.run(['git', 'add', '.'], cwd=repo_path, check=True)
        subprocess.run(['git', 'commit', '-m', 'Synced changes from Obsidian vault'], cwd=repo_path, check=True)
        subprocess.run(['git', 'push'], cwd=repo_path, check=True)
        print("Committed and pushed changes to the remote repository.")
    except subprocess.CalledProcessError:
        print("Failed to commit and push changes. Please check the repository status.")

def load_connections():
    """Load the configuration from the JSON file."""
    if os.path.exists(CONNECTIONS_FILE):
        with open(CONNECTIONS_FILE, 'r') as file:
            return json.load(file)
    return {}

