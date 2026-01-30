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

Original source

Linkedin Learning

https://www.linkedin.com/learning/model-context-protocol-mcp-hands-on-with-agentic-ai/articles/creating-an-mcp-server-using-python?resume=false&u=2164418


macOS via Homebrew:  

brew install uv

Windows via WinGet:  

winget install --id=astral-sh.uv  -e


Setting up the project
To set up your project, open your code editor to the folder you want to add your project. Then follow these steps to set up your project:

Create a new folder called mcp-server-weather using the editor tools or terminal:
mkdir mcp-server-weather
Navigate to the folder in terminal:
cd mcp-server-weather
Initiate a new uv project:
uv init
Create a virtual environment using uv:
uv venv
Start the virtual environment:
source .venv/bin/activate
Note: To stop the virtual environment, run deactivate in terminal.
Install the Python MCP SDK with the CLI extension and additional Python dependencies in the virtual environment:
uv add "mcp[cli]" httpx

Building the weather MCP server

Testing and running the MCP server
The MCP server is now fully functional and ready to test using the MCP Inspector. You'll learn more about the inspector in the next video, but here's a preview:

In terminal, start your MCP server in developer mode by running:
mcp dev main.py

The MCP Inspector is now available at http://localhost:5173; open the URL in your browser
Select the "Connect" button
Select the "Tools" tab
Select the "List Tools" button
Select the get_current_weather tool
In the get_current_weather panel, enter a latitude and longitude, eg 63.4463991, 10.8127596
Under "Tool Result" you'll see a JSON object with weather data
Press Ctrl+C in terminal to crash out of the MCP Inspector.