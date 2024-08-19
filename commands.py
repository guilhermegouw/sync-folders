import os
from utils import copy_folder, git_pull, git_commit_and_push, load_connections, save_connection


def add_connection(name, origin, target):
    """Add a new connection to the configuration."""
    config = load_connections()

    origin = os.path.abspath(origin)
    target = os.path.abspath(target)

    config[name] = {
        "origin": origin,
        "target": target
    }
    save_connection(config)
    print(f"Connection '{name}' added successfully.")

def list_connections():
    """List all the connections."""
    config = load_connections()
    if config:
        print("Stored connections:")
        for name, connection in config.items():
            print(
                f"  - {name}: {connection['origin']} -> {connection['target']}"
            )
    else:
        print("No connections found.")

def show_connection(name):
    """Show the details of a connection."""
    config = load_connections()
    if name in config:
        print(f"Connection: {name}")
        print(f"Origin: {config[name]['origin']}")
        print(f"Target: {config[name]['target']}")
    else:
        print(f"Connection '{name}' not found.")

def edit_connection(name, arg_1=None, arg_2=None):
    """Edit an existing connection. Can handle full or partial edits."""
    config = load_connections()

    if name not in config:
        print(f"Connection '{name}' not found.")
        return

    if arg_1 == "origin":
        if arg_2:
            config[name]['origin'] = arg_2
            print(f"Origin path for '{name}' updated to '{arg_2}'.")
        else:
            print("No new origin path provided.")
            return
    elif arg_1 == "target":
        if arg_2:
            config[name]['target'] = arg_2
            print(f"Target path for '{name}' updated to '{arg_2}'.")
        else:
            print("No new target path provided.")
            return
    else:
        if arg_1 and arg_2:
            config[name]['origin'] = arg_1
            config[name]['target'] = arg_2
            print(f"Connection '{name}' fully updated.")
        else:
            print("For full edit, both origin and target paths must be provided.")
            return

    save_connection(config)

def remove_connection(name):
    """Remove a connection from the connections file."""
    config = load_connections()
    if name in config:
        del config[name]
        save_connection(config)
        print(f"Connection '{name}' removed successfully.")
    else:
        print(f"Connection '{name}' not found.")

def sync(name, direction):
    """Sync the content between origin and target based on direction."""
    config = load_connections()

    if name not in config:
        print(f"Connection '{name}' not found.")
        return

    origin = config[name]['origin']
    target = config[name]['target']

    if direction == "origin-to-target":
        copy_folder(origin, target)
        git_commit_and_push(target)
        print(f"Synced from '{origin}' to '{target}' and pushed changes.")
    elif direction == "target-to-origin":
        git_pull(target)
        copy_folder(target, origin)
        print(f"Pulled changes and synced from '{target}' to '{origin}'.")
    else:
        print("Invalid sync direction. Use 'origin-to-target' or 'target-to-origin'.")

