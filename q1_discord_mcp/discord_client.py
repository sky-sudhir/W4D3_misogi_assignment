import aiohttp
from typing import Dict, List, Any, Optional

class DiscordClient:
    """Discord API client for interacting with Discord's REST API."""
    
    BASE_URL = "https://discord.com/api/v10"
    
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Authorization": f"Bot {token}",
            "Content-Type": "application/json"
        }
    
    async def send_message(self, channel_id: str, content: str) -> Dict[str, Any]:
        """Send a message to a Discord channel."""
        async with aiohttp.ClientSession() as session:
            url = f"{self.BASE_URL}/channels/{channel_id}/messages"
            payload = {"content": content}
            
            async with session.post(url, headers=self.headers, json=payload) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"Failed to send message: {response.status} - {error_text}")
    
    async def get_channel_messages(self, channel_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Get messages from a Discord channel."""
        async with aiohttp.ClientSession() as session:
            url = f"{self.BASE_URL}/channels/{channel_id}/messages?limit={limit}"
            
            async with session.get(url, headers=self.headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"Failed to get messages: {response.status} - {error_text}")
    
    async def get_channel(self, channel_id: str) -> Dict[str, Any]:
        """Get information about a Discord channel."""
        async with aiohttp.ClientSession() as session:
            url = f"{self.BASE_URL}/channels/{channel_id}"
            
            async with session.get(url, headers=self.headers) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"Failed to get channel: {response.status} - {error_text}")
    
    async def delete_message(self, channel_id: str, message_id: str) -> bool:
        """Delete a message from a Discord channel."""
        async with aiohttp.ClientSession() as session:
            url = f"{self.BASE_URL}/channels/{channel_id}/messages/{message_id}"
            
            async with session.delete(url, headers=self.headers) as response:
                return response.status == 204
    
    async def kick_user(self, guild_id: str, user_id: str, reason: Optional[str] = None) -> bool:
        """Kick a user from a Discord guild."""
        async with aiohttp.ClientSession() as session:
            url = f"{self.BASE_URL}/guilds/{guild_id}/members/{user_id}"
            headers = self.headers.copy()
            if reason:
                headers["X-Audit-Log-Reason"] = reason
            
            async with session.delete(url, headers=headers) as response:
                return response.status == 204
    
    async def ban_user(self, guild_id: str, user_id: str, reason: Optional[str] = None) -> bool:
        """Ban a user from a Discord guild."""
        async with aiohttp.ClientSession() as session:
            url = f"{self.BASE_URL}/guilds/{guild_id}/bans/{user_id}"
            headers = self.headers.copy()
            if reason:
                headers["X-Audit-Log-Reason"] = reason
            
            async with session.put(url, headers=headers) as response:
                return response.status == 204
