# MCP Weather Server

A Model Context Protocol (MCP) server that provides weather information for cities using the [wttr.in](https://wttr.in) API.

## Features

- **get_weather**: Fetches current weather conditions and temperature for any city

## Requirements

- Python 3.10+

## Installation

```bash
# Using uv
uv sync

# Or using pip
pip install -e .
```

## Usage

### Running the server

```bash
# Using uv
uv run main.py

# Or directly with Python
python main.py
```

### Configuring with Claude Desktop

Add the following to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": ["--directory", "/path/to/mcp-server-weather", "run", "main.py"]
    }
  }
}
```

### Available Tools

#### `get_weather`

Get current weather for a city.

**Parameters:**
- `city` (string, required): The name of the city

**Example response:**
```
Weather in London: Partly cloudy +15°C
```

## Dependencies

- [httpx](https://www.python-httpx.org/) - Async HTTP client
- [mcp](https://github.com/modelcontextprotocol/python-sdk) - Model Context Protocol SDK

## License

MIT

## Original Source

LinkedIn Learning

https://www.linkedin.com/learning/model-context-protocol-mcp-hands-on-with-agentic-ai/articles/creating-an-mcp-server-using-python?resume=false&u=2164418

## Installing uv

**macOS via Homebrew:**
```bash
brew install uv
```

**Windows via WinGet:**
```bash
winget install --id=astral-sh.uv -e
```

## Setting Up the Project

To set up your project, open your code editor to the folder you want to add your project. Then follow these steps:

1. Create a new folder called `mcp-server-weather` using the editor tools or terminal:
   ```bash
   mkdir mcp-server-weather
   ```

2. Navigate to the folder in terminal:
   ```bash
   cd mcp-server-weather
   ```

3. Initiate a new uv project:
   ```bash
   uv init
   ```

4. Create a virtual environment using uv:
   ```bash
   uv venv
   ```

5. Start the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
   > **Note:** To stop the virtual environment, run `deactivate` in terminal.

6. Install the Python MCP SDK with the CLI extension and additional Python dependencies in the virtual environment:
   ```bash
   uv add "mcp[cli]" httpx
   ```

## Testing and Running the MCP Server

The MCP server is now fully functional and ready to test using the MCP Inspector.

1. In terminal, start your MCP server in developer mode by running:
   ```bash
   mcp dev main.py
   ```

2. The MCP Inspector is now available at http://localhost:5173; open the URL in your browser

3. Select the "Connect" button

4. Select the "Tools" tab

5. Select the "List Tools" button

6. Select the `get_weather` tool

7. In the `get_weather` panel, enter a city name (e.g., "London")

8. Under "Tool Result" you'll see the weather data

9. Press `Ctrl+C` in terminal to exit the MCP Inspector
