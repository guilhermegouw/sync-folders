That's a terminal application with the purpose of sync 2 folders in a simple and easy manner.

### Installation:

1. Clone the project with:
 ```
 cd ~/
 git clone git@github.com:guilhermegouw/sync-folders.git
 ```
2. Edit you .bashrc (or equivalent), add a alias to make the usage easier.
```
code ~/.bashrc
# inside the file add the following line:
alias sync-folders="python3 ~/sync-folders/main.py"
```
Now you are all set!

### Usage:
The application has 2 basic features:
- Connections: Are connections between 2 folders.
  - **origin**: Is your obsidian vault folder.
  - **target**: Is the folder that contains the git repository that the users wants to be synced with.
- Sync: Is the action of syncing per say.
Each feature has a set of arguments that specifies the desired action.

Let's explore those arguments.
#### Connections:
- **add_connection**
  command:
  ```
  sync-folders add_connection connection_name path_to_origin_folder path_to_target_folder
  ```
- What it does?
  Creates a connection between "origin" and "target", that connection will have a name that will be used to reference the connection when running other connections.
- Example: 
    - You have 2 folders:
        - origin: ~/origin
    		- target: ~/target
	  - You want to create a connection between those folders and, name it "test_connection"
	  - you will run:
    ```
    sync-folders add_connection test_connection ~/origin ~/target
    ```

- list_connections
    command:
    ```
    sync-folders list_connections
    ```
    - What it does?
	    Lists all connections available.
  	- Example:
	    - Let's say you created the connection of the add_connection example. The output will be something like this:
		```
	    sync-folders list_connections
	    Stored connections:
        - test_connection: /Users/your-home-folder/origin ->               /Users/your-home-folder/target
    ```

- edit_connection:
    - What it does?
        Here you have to options:
    - Full: Edits both origin_path and target_path.
 	  command:
    ```
    sync-folders connection_name origin_path target_path
    ```
    - Partial: Edits origin_path or target_path.
			- origin:
			command:
      ```
      sync-folders connection_name origin new_origin_path
      ```

      - target:
			command:
      ```
      sync-folders connection_name target new_target_path
      ```

- remove_connection:
    command:
    ```
    sync-folders remove_connection connection_name
  	```
	- What it does?
	    It removes the connection that you passed as argument.
	- Example:
	    - To remove the connection named "test_connection"
		```
		sync-folders remove_connection test_connection
		```

#### Sync:
```
sync-folders connection_name direction
```

Here you have 2 directions to sync your folders:
- origin-to-target: sync the origin content to target folder.
- target-to-origin: sync the target content to origin folder.
Examples:
```
sync-folders test_connection origin-to-target
```
or
```
sync-folders test_connection target-to-origin
```

Suggestions, doubts or comments: guilherme.gouw@gmail.com
