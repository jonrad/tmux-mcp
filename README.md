# Tmux MCP Server

A POC [MCP (Model Context Protocol) Server](https://modelcontextprotocol.io/introduction) implementation that provides programmatic control over tmux sessions

## Warning

This is a proof of concept and should not be used in production. Using this, you can run arbitrary tmux commands, including reading pane contents and sending keys. 

## Features

- Run arbitrary tmux commands

## Usage

### In your MCP client configuration:

```json
"mcpServers": {
    "tmux": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/jonrad/tmux-mcp", "tmux-mcp"]
    },
}
```