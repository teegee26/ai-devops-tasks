```bash
#!/bin/bash

if ! systemctl is-active --quiet docker; then
    echo "Docker is not running. Starting Docker..."
    sudo systemctl start docker
else
    echo "Docker is already running."
fi
```
### Script Explanation

Let's go through the script line by line:

1. <br> <code>#!/bin/bash</code>  
    This is called a "shebang." It tells the system to use the Bash shell to run this script.

2. <br> <code>if ! systemctl is-active --quiet docker; then</code>  
    This line checks if the Docker service is **not** running.  
    - `systemctl is-active --quiet docker` checks if Docker is active, but doesn't print anything.
    - The `!` means "not", so the condition is true if Docker is **not** running.

3. <br> <code>echo "Docker is not running. Starting Docker..."</code>  
    If Docker is not running, this line prints a message to let you know.

4. <br> <code>sudo systemctl start docker</code>  
    This command starts the Docker service using `sudo` (which runs the command as an administrator).

5. <br> <code>else</code>  
    If Docker **is** running, the script will do the next step instead.

6. <br> <code>echo "Docker is already running."</code>  
    This prints a message saying Docker is already running.

7. <br> <code>fi</code>  
    This ends the `if` statement.

**Summary:**  
This script checks if Docker is running. If not, it starts Docker; if it is, it tells you so.
