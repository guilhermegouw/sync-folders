import sys
from commands import add_connection, show_connection, list_connections, edit_connection, remove_connection, sync


commands = ['add_connection', 'show_connection', 'list_connections', 'edit_connection', 'remove_connection', 'sync']


def main():
    command = sys.argv[1]

    if command not in commands:
        print(f"{command} is not a valid command.\n")
        print("Valid commands are:")
        [print(f"  - {cmd}") for cmd in commands]
        print()
        return

    if command == "add_connection":
        if len(sys.argv) != 5:
            print("Usage: python main.py add_connection <connection_name> <path_to_origin_folder> <path_to_target_folder>")
            return
        name = sys.argv[2]
        origin = sys.argv[3]
        target = sys.argv[4]
        add_connection(name, origin, target)
    elif command == "show_connection":
        if len(sys.argv) != 3:
            print("Usage: python main.py show_connection <connection_name>")
            return
        name = sys.argv[2]
        show_connection(name)
    elif command == "list_connections":
        list_connections()
    elif command == "edit_connection":
        if len(sys.argv) == 5:
            # Full edit
            name = sys.argv[2]
            arg_1 = sys.argv[3]
            arg_2 = sys.argv[4]
            edit_connection(name, arg_1, arg_2)
        elif len(sys.argv) == 4:
            # Partial edit
            name = sys.argv[2]
            arg_1 = sys.argv[3]
            arg_2 = sys.argv[4]
            edit_connection(name, arg_1, arg_2)
        else:
            print("Usage for full edit: python main.py edit_connection <connection_name> <new_origin_path> <new_target_path>")
            print("Usage for partial edit: python main.py edit_connection <connection_name> origin <new_origin_path>")
            print("Usage for partial edit: python main.py edit_connection <connection_name> target <new_target_path>")
            return
    elif command == "remove_connection":
        if len(sys.argv) != 3:
            print("Usage: python main.py remove_connection <connection_name>")
            return
        name = sys.argv[2]
        remove_connection(name)
    elif command == "sync":
        if len(sys.argv) != 4:
            print("Usage: python main.py sync <connection_name> <direction>")
            print("Direction options: origin-to-target, target-to-origin")
            return
        name = sys.argv[2]
        direction = sys.argv[3]
        sync(name, direction)

if __name__ == "__main__":
    main()
