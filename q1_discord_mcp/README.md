# Discord MCP Server

A FastMCP server for Discord integrations with authentication and logging.

## Features

- Discord API integration for sending/receiving messages
- Channel information retrieval
- Message search functionality
- Content moderation tools
- API key authentication
- Logging and rate limiting

## Setup

1. Install dependencies:
   ```bash
   pip install -e .
   ```

2. Create a `.env` file:
   ```
   DISCORD_BOT_TOKEN=your_discord_bot_token
   MCP_API_KEY=your_api_key_for_authentication
   ```

## Running the Server

```bash
uvicorn main:mcp.app --host 0.0.0.0 --port 8000 --reload
```

Or:

```bash
fastmcp run main.py
```

## API Tools

- `send_message`: Send a message to a channel
- `get_messages`: Retrieve channel message history
- `get_channel_info`: Get channel metadata
- `search_messages`: Search messages by content
- `moderate_content`: Perform moderation actions

## Authentication

Include your API key in the Authorization header:
```
Authorization: Bearer your_api_key
```

## Example Usage

```python
from fastmcp.client import FastMCPClient

client = FastMCPClient(
    base_url="http://localhost:8000",
    auth_token="your_api_key"
)

# Send a message
response = await client.call_tool(
    "send_message",
    {
        "channel_id": "your_channel_id",
        "message_content": "Hello from FastMCP!"
    }
)
```
