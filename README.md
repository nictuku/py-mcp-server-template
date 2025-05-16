# py-mcp-server-template

This repository is a template to help you create your own MCP (Multi-Capability Provider) servers in Python. Fork this repository to get started.

## Setup with uv

This project uses `uv` for Python packaging and virtual environment management. If you don't have `uv` installed, please refer to the [official uv installation guide](https://github.com/astral-sh/uv#installation).

1.  **Clone your forked repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create and activate the virtual environment:**
    `uv` typically creates a `.venv` directory in your project root.
    ```bash
    uv venv
    source .venv/bin/activate  # On macOS/Linux
    # .venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**
    This project uses `pyproject.toml` to manage dependencies.
    ```bash
    uv pip install .
    ```
    If you add new dependencies, define them in your `pyproject.toml` file and run this command again. If you are using a `requirements.txt` file for some reason, you can install it with `uv pip install -r requirements.txt`.

## Running the Server

The `mcp_server.py` script starts the MCP server.

To run the server directly:
```bash
uv run python mcp_server.py
```

## Integrating with Claude Desktop or Cursor

To use this MCP server with an application like Claude Desktop or Cursor, you'll need to configure it in the application's settings. The configuration will typically involve specifying the command to run your server.

Here's an example configuration snippet. You'll need to replace `/ABSOLUTE/PATH/TO/PARENT/FOLDER/YOUR_REPOSITORY_NAME` with the actual absolute path to your project directory on your system.

```json
{
    "mcpServers": {
        "my-custom-python-server": {
            "command": "uv",
            "args": [
                "run",
                "--python",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/YOUR_REPOSITORY_NAME/.venv/bin/python",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/YOUR_REPOSITORY_NAME/mcp_server.py"
            ],
            "workingDirectory": "/ABSOLUTE/PATH/TO/PARENT/FOLDER/YOUR_REPOSITORY_NAME"
        }
    }
}
```

**Explanation of the configuration:**

*   `"my-custom-python-server"`: This is a name you give to your server configuration.
*   `"command": "uv"`: Specifies `uv` as the command to execute.
*   `"args"`: A list of arguments for the `uv` command:
    *   `"run"`: Tells `uv` to execute a command within its managed environment.
    *   `"--python"`: Specifies the Python interpreter to use. It's important to point this to the Python interpreter inside your `uv` virtual environment (`.venv/bin/python`).
    *   `"/ABSOLUTE/PATH/TO/PARENT/FOLDER/YOUR_REPOSITORY_NAME/mcp_server.py"`: The absolute path to your server script.
*   `"workingDirectory"`: Specifies the working directory for the server process, which should be your project's root directory.

**Important:**
*   Ensure the paths in the `args` and `workingDirectory` are correct for your system.
*   If the application cannot locate `uv`, you might need to specify its full path in the `"command"` field. You can typically find this path by running `which uv` in your terminal on macOS or Linux, or `where uv` on Windows.
*   The server listens on `stdio` by default as configured in `mcp_server.py` (`mcp.run(transport='stdio')`), which is typically what applications like Cursor expect.

After configuring, the application should be able to communicate with your Python MCP server.
