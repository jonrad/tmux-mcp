from mcp.server.fastmcp import FastMCP
import libtmux
import logging
import os

# Create an MCP server
mcp = FastMCP("tmux", settings={"log_level": "DEBUG"})

# FastMCP sets its own logging, which we may want to override
log_file = os.getenv("LOG_FILE")
if log_file:
    file_handler = logging.FileHandler(log_file)
    logging.root.handlers.append(file_handler)
logger = logging.getLogger(__name__)

# Connect to the tmux server
server = libtmux.Server()

def main():
    logger.info("Starting tmux MCP server")
    mcp.run()

@mcp.tool(description="Run a generic command in tmux. This is the equivalent of running `tmux <command> <args>` in your shell.")
def run_tmux_command(command: str, args: list[str]) -> str:
    if command == 'tmux':
        command = args.pop(0)

    logger.info(f"Run command: {command} {args}")
    result = server.cmd(command, *args)
    formatted = "\n".join(result.stdout)
    logger.info(f"Result: {formatted}")
    return result.stdout

if __name__ == "__main__":
    main()