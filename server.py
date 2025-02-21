from mcp.server.fastmcp import FastMCP
import libtmux
import logging
import os

def main():
    # Create an MCP server
    mcp = FastMCP("tmux", settings={"log_level": "DEBUG"})

    # FastMCP sets its own logging, which we may want to override
    log_file = os.getenv("LOG_FILE", "default.log")
    if log_file:
        file_handler = logging.FileHandler(log_file)
        logging.root.handlers.append(file_handler)
    logger = logging.getLogger(__name__)

    # Connect to the tmux server
    server = libtmux.Server()

    logger.info("Starting tmux MCP server")

    @mcp.tool(description="Run a generic command in tmux")
    def run_tmux_command(command: str, args: list[str]) -> str:
        if command == 'tmux':
            command = args.pop(0)

        logger.info(f"Run command: {command} {args}")
        result = server.cmd(command, *args)
        formatted = "\n".join(result.stdout)
        logger.info(f"Result: {formatted}")
        return result.stdout

    #@mcp.resource("tmux://pane/current", description="Gets the content of the current pane")
    @mcp.tool(description="Gets the content of the current pane")
    def get_current_pane_contents() -> str:
        return server.panes[0].capture_pane(end="-10")

    mcp.run()