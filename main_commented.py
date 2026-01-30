"""
MCP Weather Server

A Model Context Protocol server that exposes weather data via the wttr.in API.

MCP (Model Context Protocol) is a standard for connecting AI models to external
tools and data sources. This server implements a simple weather lookup tool
that can be used by MCP-compatible clients (e.g., Claude Desktop, Claude Code).
"""

# httpx: An async-capable HTTP client library, similar to requests but with
# native async/await support for better performance in concurrent scenarios
import httpx

# FastMCP: A high-level framework for building MCP servers with minimal boilerplate
# It provides decorators to easily expose Python functions as MCP tools
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server with the name "weather"
# This name is used to identify the server in client configurations
# and appears in tool listings when clients connect
mcp = FastMCP("weather")


# The @mcp.tool() decorator registers this function as an MCP tool
# MCP tools are functions that AI models can call to perform actions
# The function signature (parameters and return type) is automatically
# converted to the MCP tool schema for the client to understand
@mcp.tool()
async def get_weather(city: str) -> str:
    """
    Get current weather for a city.

    This tool queries the wttr.in service, a free weather API that supports
    plain-text responses. The city parameter can be a city name, airport code,
    or geographic coordinates.

    Args:
        city: The name of the city to get weather for (e.g., "London", "New York")

    Returns:
        A string containing the weather condition and temperature for the city,
        or an error message if the weather could not be fetched.
    """
    # Create an async HTTP client with a 30-second timeout
    # Using 'async with' ensures the client is properly closed after the request
    async with httpx.AsyncClient(timeout=30.0) as client:
        # Query wttr.in API with format parameters:
        # %C = weather condition text (e.g., "Partly cloudy", "Clear")
        # %t = temperature with unit (e.g., "+15°C", "-5°F")
        # The format parameter tells wttr.in to return plain text instead of ASCII art
        response = await client.get(
            f"https://wttr.in/{city}?format=%C+%t"
        )

        # Check if the request was successful (HTTP 200 OK)
        if response.status_code == 200:
            # Strip whitespace from the response and format it nicely
            return f"Weather in {city}: {response.text.strip()}"

        # Return an error message if the API request failed
        # This could happen if the city name is invalid or the service is down
        return f"Could not fetch weather for {city}"


# Entry point: This block runs when the script is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    # Start the MCP server using stdio transport (default)
    # stdio transport communicates via standard input/output streams,
    # which is the standard way for MCP clients to spawn and communicate
    # with MCP servers as subprocesses
    mcp.run()




  Analysis Summary:                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                    
  The file is an MCP (Model Context Protocol) weather server with these components:                                                                                                                                                                                                                                                                                                                                                                 
  ┌──────────────────────────┬──────────────────────────────────────────────────────────┐                                                                                                                                                                                                                                                                                                                                                           
  │        Component         │                         Purpose                          │                                                                                                                                                                                                                                                                                                                                                           
  ├──────────────────────────┼──────────────────────────────────────────────────────────┤                                                                                                                                                                                                                                                                                                                                                           
  │ httpx                    │ Async HTTP client for making API requests                │                                                                                                                                                                                                                                                                                                                                                           
  ├──────────────────────────┼──────────────────────────────────────────────────────────┤                                                                                                                                                                                                                                                                                                                                                           
  │ FastMCP                  │ Framework for building MCP servers with decorators       │                                                                                                                                                                                                                                                                                                                                                           
  ├──────────────────────────┼──────────────────────────────────────────────────────────┤                                                                                                                                                                                                                                                                                                                                                           
  │ mcp = FastMCP("weather") │ Server instance named "weather"                          │                                                                                                                                                                                                                                                                                                                                                           
  ├──────────────────────────┼──────────────────────────────────────────────────────────┤                                                                                                                                                                                                                                                                                                                                                           
  │ @mcp.tool()              │ Decorator that exposes the function as an MCP tool       │                                                                                                                                                                                                                                                                                                                                                           
  ├──────────────────────────┼──────────────────────────────────────────────────────────┤                                                                                                                                                                                                                                                                                                                                                           
  │ get_weather(city)        │ Async function that queries wttr.in API for weather data │                                                                                                                                                                                                                                                                                                                                                           
  ├──────────────────────────┼──────────────────────────────────────────────────────────┤                                                                                                                                                                                                                                                                                                                                                           
  │ mcp.run()                │ Starts the server using stdio transport                  │                                                                                                                                                                                                                                                                                                                                                           
  └──────────────────────────┴──────────────────────────────────────────────────────────┘                                                                                                                                                                                                                                                                                                                                                           
  Key details added in comments:                                                                                                                                                                                                                                                                                                                                                                                                                    
  - Explanation of MCP and its purpose                                                                                                                                                                                                                                                                                                                                                                                                              
  - What httpx and FastMCP do                                                                                                                                                                                                                                                                                                                                                                                                                       
  - How the @mcp.tool() decorator works                                                                                                                                                                                                                                                                                                                                                                                                             
  - The wttr.in API format parameters (%C for condition, %t for temperature)                                                                                                                                                                                                                                                                                                                                                                        
  - Error handling logic                                                                                                                                                                                                                                                                                                                                                                                                                            
  - How stdio transport works for MCP communication 
  