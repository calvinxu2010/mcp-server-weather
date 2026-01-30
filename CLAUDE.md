# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) server that provides weather information to AI assistants. It exposes a single tool `get_weather(city)` that fetches current weather from the wttr.in API.

## Commands

```bash
# Install dependencies
uv sync

# Run the server
uv run main.py

# Test with MCP Inspector (opens at http://localhost:5173)
mcp dev main.py
```

## Architecture

- **main.py**: The entire server implementation (~30 lines). Uses FastMCP to register an async `get_weather` tool that queries wttr.in with format parameters `%C` (condition) and `%t` (temperature).
- **main_commented.py**: Heavily annotated version of main.py for learning purposes.

The server uses stdio transport for communication with MCP clients.

## Adding New Tools

Register new tools using the `@mcp.tool()` decorator on async functions:

```python
@mcp.tool()
async def new_tool(param: str) -> str:
    """Docstring becomes the tool description."""
    # implementation
```

