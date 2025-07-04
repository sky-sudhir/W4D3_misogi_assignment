# server.py
import os
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from fastmcp import FastMCP, Context
from pydantic import Field
from models import SendMessageInput, Message, ChannelInfo, SearchMessagesInput, ModerateContentInput
from discord_client import DiscordClient

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
MCP_API_KEY = os.getenv("MCP_API_KEY")

if not DISCORD_BOT_TOKEN:
    print("WARNING: DISCORD_BOT_TOKEN not set. Discord tools will not function correctly.")


mcp = FastMCP(name="DiscordMCP")


@mcp.tool
async def send_message(
    input: SendMessageInput,
    ctx: Context
) -> Dict[str, Any]:
    """
    Sends a message to a specified Discord channel. 
    """
    if not DISCORD_BOT_TOKEN:
        await ctx.error("Discord bot token not configured. Cannot send message.")
        return {"status": "error", "message": "Discord bot token missing."}

    await ctx.info(f"Attempting to send message to channel {input.channel_id}")
    
    try:
        discord_client = DiscordClient(DISCORD_BOT_TOKEN)
        response = await discord_client.send_message(input.channel_id, input.message_content)
        await ctx.info(f"Message sent successfully to channel {input.channel_id}")
        return {"status": "success", "message_id": response["id"]}
    except Exception as e:
        await ctx.error(f"Failed to send message: {e}")
        return {"status": "error", "message": str(e)}

@mcp.tool
async def get_messages(
    ctx: Context,
    channel_id: str = Field(..., description="The ID of the Discord channel."),
    limit: int = Field(10, description="Maximum number of messages to retrieve.", ge=1, le=100),
) -> List[Message]:
    """
    Retrieves message history from a specified Discord channel.
    """
    if not DISCORD_BOT_TOKEN:
        await ctx.error("Discord bot token not configured. Cannot retrieve messages.")
        return []

    await ctx.info(f"Retrieving {limit} messages from channel {channel_id}")
    
    try:
        discord_client = DiscordClient(DISCORD_BOT_TOKEN)
        messages_data = await discord_client.get_channel_messages(channel_id, limit)
        
        result = []
        for msg in messages_data:
            result.append(Message(
                id=msg["id"],
                channel_id=channel_id,
                author_id=msg["author"]["id"],
                content=msg["content"],
                timestamp=msg["timestamp"]
            ))
        
        await ctx.info(f"Successfully retrieved {len(result)} messages")
        return result
    except Exception as e:
        await ctx.error(f"Failed to retrieve messages: {e}")
        return []

@mcp.tool
async def get_channel_info(
    ctx: Context,
    channel_id: str = Field(..., description="The ID of the Discord channel."),
) -> Optional[ChannelInfo]:
    """
    Fetches metadata for a specified Discord channel.
    """
    if not DISCORD_BOT_TOKEN:
        await ctx.error("Discord bot token not configured. Cannot get channel info.")
        return None

    await ctx.info(f"Fetching info for channel {channel_id}")
    
    try:
        discord_client = DiscordClient(DISCORD_BOT_TOKEN)
        channel_data = await discord_client.get_channel(channel_id)
        
        return ChannelInfo(
            id=channel_data["id"],
            name=channel_data["name"],
            type=channel_data["type"],
            guild_id=channel_data.get("guild_id", "")
        )
    except Exception as e:
        await ctx.error(f"Failed to get channel info: {e}")
        return None

@mcp.tool
async def search_messages(
    input: SearchMessagesInput,
    ctx: Context
) -> List[Message]:
    """
    Searches Discord message history with filters.
    """
    if not DISCORD_BOT_TOKEN:
        await ctx.error("Discord bot token not configured. Cannot search messages.")
        return []

    await ctx.info(f"Searching for '{input.query}' in channel {input.channel_id or 'all'} (limit: {input.limit})")
    
    try:
        discord_client = DiscordClient(DISCORD_BOT_TOKEN)
        
        # Discord API doesn't have a direct search endpoint for bots
        # We'll fetch messages and filter them client-side
        if input.channel_id:
            # If channel_id is provided, search only in that channel
            messages_data = await discord_client.get_channel_messages(input.channel_id, 100)  # Get more messages to filter
            
            result = []
            for msg in messages_data:
                if input.query.lower() in msg["content"].lower():
                    result.append(Message(
                        id=msg["id"],
                        channel_id=input.channel_id,
                        author_id=msg["author"]["id"],
                        content=msg["content"],
                        timestamp=msg["timestamp"]
                    ))
                    if len(result) >= input.limit:
                        break
            
            await ctx.info(f"Found {len(result)} messages matching query")
            return result
        else:
            # If no channel_id, we can't search across all channels efficiently
            # This would require knowledge of all accessible channels
            await ctx.warning("Searching across all channels is not supported")
            return []
    except Exception as e:
        await ctx.error(f"Failed to search messages: {e}")
        return []

@mcp.tool
async def moderate_content(
    input: ModerateContentInput,
    ctx: Context
) -> Dict[str, Any]:
    """
    Performs content moderation actions (delete messages, manage users).
    """
    if not DISCORD_BOT_TOKEN:
        await ctx.error("Discord bot token not configured. Cannot moderate content.")
        return {"status": "error", "message": "Discord bot token missing."}

    await ctx.info(f"Attempting to perform moderation action '{input.action}' on '{input.target_id}' (Reason: {input.reason or 'N/A'})")
    
    try:
        discord_client = DiscordClient(DISCORD_BOT_TOKEN)
        
        if input.action == "delete_message":
            # For delete_message, target_id should be in format "channel_id:message_id"
            if ":" not in input.target_id:
                await ctx.error("Invalid target_id format for delete_message. Expected 'channel_id:message_id'")
                return {"status": "error", "message": "Invalid target_id format"}
            
            channel_id, message_id = input.target_id.split(":", 1)
            success = await discord_client.delete_message(channel_id, message_id)
            
            if success:
                await ctx.info(f"Successfully deleted message {message_id}")
                return {"status": "success", "message": f"Message {message_id} deleted"}
            else:
                await ctx.error(f"Failed to delete message {message_id}")
                return {"status": "error", "message": "Failed to delete message"}
                
        elif input.action == "kick_user":
            # For kick_user, target_id should be in format "guild_id:user_id"
            if ":" not in input.target_id:
                await ctx.error("Invalid target_id format for kick_user. Expected 'guild_id:user_id'")
                return {"status": "error", "message": "Invalid target_id format"}
            
            guild_id, user_id = input.target_id.split(":", 1)
            success = await discord_client.kick_user(guild_id, user_id, input.reason)
            
            if success:
                await ctx.info(f"Successfully kicked user {user_id}")
                return {"status": "success", "message": f"User {user_id} kicked"}
            else:
                await ctx.error(f"Failed to kick user {user_id}")
                return {"status": "error", "message": "Failed to kick user"}
                
        elif input.action == "ban_user":
            # For ban_user, target_id should be in format "guild_id:user_id"
            if ":" not in input.target_id:
                await ctx.error("Invalid target_id format for ban_user. Expected 'guild_id:user_id'")
                return {"status": "error", "message": "Invalid target_id format"}
            
            guild_id, user_id = input.target_id.split(":", 1)
            success = await discord_client.ban_user(guild_id, user_id, input.reason)
            
            if success:
                await ctx.info(f"Successfully banned user {user_id}")
                return {"status": "success", "message": f"User {user_id} banned"}
            else:
                await ctx.error(f"Failed to ban user {user_id}")
                return {"status": "error", "message": "Failed to ban user"}
        else:
            await ctx.warning(f"Unknown moderation action: {input.action}")
            return {"status": "error", "message": "Unknown moderation action"}
    except Exception as e:
        await ctx.error(f"Failed to perform moderation action: {e}")
        return {"status": "error", "message": str(e)}


# --- Authentication Layer ---
# FastMCP uses `AuthProviders` for server protection.
# We'll use a simple in-memory API key provider for demonstration.
# For multi-tenancy, you would typically have a more complex provider
# that maps API keys to Discord bot tokens and permissions.



# Add the middleware to the FastMCP server
# mcp.add_middleware(AuditLoggingMiddleware)

# --- Rate Limiting (Conceptual) ---
# FastMCP has built-in rate limiting middleware.
# You would configure it based on your needs (e.g., per IP, per API key).
# from fastmcp.server.middleware.rate_limiting import RateLimitingMiddleware

# Example: 100 requests per minute
# In a real app, you'd use a more persistent store than in-memory for production.
# mcp.add_middleware(RateLimitingMiddleware(100, 60))


# --- Main execution block ---
if __name__ == "__main__":
    print(f"FastMCP Server '{mcp.name}' starting...")
    mcp.run()
