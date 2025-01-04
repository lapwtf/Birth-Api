from typing import Optional, List, Dict, Any
import discord
from discord.ext import commands

class MessageAPI:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def send_message(self, channel_id: int, content: str, embed: Optional[discord.Embed] = None) -> Optional[Dict[str, Any]]:
        channel = self.bot.get_channel(channel_id)
        if not channel:
            return None

        try:
            message = await channel.send(content=content, embed=embed)
            return {
                'id': message.id,
                'content': message.content,
                'created_at': message.created_at.isoformat()
            }
        except discord.Forbidden:
            return None

    async def edit_message(self, channel_id: int, message_id: int, new_content: str) -> bool:
        channel = self.bot.get_channel(channel_id)
        if not channel:
            return False

        try:
            message = await channel.fetch_message(message_id)
            if message.author != self.bot.user:
                return False
            await message.edit(content=new_content)
            return True
        except (discord.NotFound, discord.Forbidden):
            return False

    async def delete_messages(self, channel_id: int, message_ids: List[int]) -> int:
        channel = self.bot.get_channel(channel_id)
        if not channel or not isinstance(channel, discord.TextChannel):
            return 0

        try:
            messages = []
            for msg_id in message_ids:
                try:
                    message = await channel.fetch_message(msg_id)
                    messages.append(message)
                except discord.NotFound:
                    continue
            
            if len(messages) > 0:
                await channel.delete_messages(messages)
            return len(messages)
        except discord.Forbidden:
            return 0

    async def get_message_history(self, channel_id: int, limit: int = 100) -> List[Dict[str, Any]]:
        channel = self.bot.get_channel(channel_id)
        if not channel:
            return []

        try:
            messages = []
            async for message in channel.history(limit=limit):
                messages.append({
                    'id': message.id,
                    'content': message.content,
                    'author': {
                        'id': message.author.id,
                        'name': message.author.name
                    },
                    'created_at': message.created_at.isoformat()
                })
            return messages
        except discord.Forbidden:
            return []
