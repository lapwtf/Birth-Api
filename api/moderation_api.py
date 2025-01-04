from typing import Optional, List, Dict, Any
import discord
from discord.ext import commands
from datetime import datetime, timedelta

class ModerationAPI:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def ban_user(self, guild_id: int, user_id: int, reason: Optional[str] = None, delete_message_days: int = 0) -> bool:
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return False

        try:
            await guild.ban(discord.Object(id=user_id), reason=reason, delete_message_days=delete_message_days)
            return True
        except discord.Forbidden:
            return False

    async def kick_user(self, guild_id: int, user_id: int, reason: Optional[str] = None) -> bool:
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return False

        member = guild.get_member(user_id)
        if not member:
            return False

        try:
            await member.kick(reason=reason)
            return True
        except discord.Forbidden:
            return False

    async def timeout_user(self, guild_id: int, user_id: int, duration: int, reason: Optional[str] = None) -> bool:
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return False

        member = guild.get_member(user_id)
        if not member:
            return False

        try:
            timeout = datetime.utcnow() + timedelta(minutes=duration)
            await member.timeout(timeout, reason=reason)
            return True
        except discord.Forbidden:
            return False

    async def get_ban_list(self, guild_id: int) -> List[Dict[str, Any]]:
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return []

        try:
            bans = await guild.bans()
            return [{
                'user_id': ban.user.id,
                'user_name': ban.user.name,
                'reason': ban.reason
            } for ban in bans]
        except discord.Forbidden:
            return []
