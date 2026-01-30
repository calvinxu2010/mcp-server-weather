"""
MCP Weather Server

A Model Context Protocol server that exposes weather data via the wttr.in API.
"""

import httpx
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server with the name "weather"
# This name is used to identify the server in client configurations
mcp = FastMCP("weather")


@mcp.tool()
async def get_weather(city: str) -> str:
    """Get current weather for a city."""
    # Create an async HTTP client with a 30-second timeout
    async with httpx.AsyncClient(timeout=30.0) as client:
        # Query wttr.in API with format parameters:
        # %C = weather condition (e.g., "Partly cloudy")
        # %t = temperature (e.g., "+15°C")
        response = await client.get(
            f"https://wttr.in/{city}?format=%C+%t"
        )
        if response.status_code == 200:
            return f"Weather in {city}: {response.text.strip()}"
        return f"Could not fetch weather for {city}"


if __name__ == "__main__":
    # Start the MCP server using stdio transport (default)
    mcp.run()
