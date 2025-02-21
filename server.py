# server.py
from mcp.server.fastmcp import FastMCP
import libtmux
import typing as t
from datetime import datetime

# Create an MCP server
mcp = FastMCP("Tmux", settings={"log_level": "DEBUG"})
server = libtmux.Server()
log_file = "tmux-mcp.log"

def log(message: str) -> None:
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()}: {message}\n")

#@mcp.tool()
#def display_message(message: str) -> str:
#    """Display message in tmux status bar"""
#    log(f"Display message: {message}")
#    server.cmd("display-message", message)
#    return "Message displayed in tmux"

@mcp.tool()
def run_tmux_command(command: str, args: list[str]) -> str:
    """run a generic command in tmux"""
    if command == 'tmux':
        command = args.pop(0)
    
    log(f"Run command: {command} {args}")
    result = server.cmd(command, *args)
    formatted = "\n".join(result.stdout)
    log(f"Result: {formatted}")
    return formatted

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

#print(run_command("list-buffers", []))
mcp.run()