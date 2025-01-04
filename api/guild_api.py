from typing import Optional, List, Dict, Any
import discord
from discord.ext import commands

class GuildAPI:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def get_guild_info(self, guild_id: int) -> Optional[Dict[str, Any]]:
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return None

        return {
            'id': guild.id,
            'name': guild.name,
            'description': guild.description,
            'member_count': guild.member_count,
            'owner_id': guild.owner_id,
            'created_at': guild.created_at.isoformat(),
            'icon_url': str(guild.icon.url) if guild.icon else None
        }

    async def get_guild_channels(self, guild_id: int) -> List[Dict[str, Any]]:
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return []

        channels = []
        for channel in guild.channels:
            channel_info = {
                'id': channel.id,
                'name': channel.name,
                'type': str(channel.type),
                'position': channel.position
            }
            if isinstance(channel, discord.TextChannel):
                channel_info['topic'] = channel.topic
            channels.append(channel_info)
        return channels

    async def get_guild_roles(self, guild_id: int) -> List[Dict[str, Any]]:
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return []

        return [{
            'id': role.id,
            'name': role.name,
            'color': str(role.color),
            'permissions': role.permissions.value,
            'position': role.position,
            'mentionable': role.mentionable
        } for role in guild.roles]
