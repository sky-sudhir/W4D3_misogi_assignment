from typing import Optional
from pydantic import BaseModel, Field


class SendMessageInput(BaseModel):
    """Input for sending a message."""
    channel_id: str = Field(..., description="The ID of the Discord channel.")
    message_content: str = Field(..., description="The content of the message to send.")

class Message(BaseModel):
    """Represents a Discord message."""
    id: str
    channel_id: str
    author_id: str
    content: str
    timestamp: str

class ChannelInfo(BaseModel):
    """Represents Discord channel metadata."""
    id: str
    name: str
    type: str
    guild_id: Optional[str] = None

class SearchMessagesInput(BaseModel):
    """Input for searching messages."""
    channel_id: Optional[str] = Field(None, description="Optional channel ID to filter by.")
    query: str = Field(..., description="The search query string.")
    limit: int = Field(10, description="Maximum number of messages to return.", ge=1, le=100)

class ModerateContentInput(BaseModel):
    """Input for content moderation actions."""
    action: str = Field(..., description="The moderation action (e.g., 'delete_message', 'kick_user', 'ban_user').")
    target_id: str = Field(..., description="The ID of the message or user to moderate.")
    reason: Optional[str] = Field(None, description="The reason for the moderation action.")