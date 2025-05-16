from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("py-mcp-server")

@mcp.tool()
async def get_ping(message: str) -> str:
    return "pong"

@mcp.tool()
async def get_joke() -> str:
    response = httpx.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()
    return joke_data["setup"] + "\n" + joke_data["punchline"]

@mcp.tool()
async def get_weather(city: str) -> str:
    response = httpx.get(f"https://wttr.in/{city}?format=3")
    return response.text

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')