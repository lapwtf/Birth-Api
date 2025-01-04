from typing import Optional, List, Dict, Any
import discord
from discord.ext import commands
""" NAME OF FILE IS SELF EXPLANATORY """
class UserAPI:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def get_user_info(self, user_id: int) -> Optional[Dict[str, Any]]:
        try:
            user = await self.bot.fetch_user(user_id)
            return {
                'id': user.id,
                'name': user.name,
                'discriminator': user.discriminator,
                'avatar_url': str(user.avatar.url) if user.avatar else None,
                'bot': user.bot,
                'created_at': user.created_at.isoformat()
            }
        except discord.NotFound:
            return None

    async def get_member_roles(self, guild_id: int, user_id: int) -> List[Dict[str, Any]]:
        guild = self.bot.get_guild(guild_id)
        if not guild:
            return []
        
        member = guild.get_member(user_id)
        if not member:
            return []

        return [{'id': role.id, 'name': role.name, 'color': str(role.color)} for role in member.roles]

    async def get_user_mutual_guilds(self, user_id: int) -> List[Dict[str, Any]]:
        user = await self.bot.fetch_user(user_id)
        mutual_guilds = []
        
        for guild in self.bot.guilds:
            member = guild.get_member(user_id)
            if member:
                mutual_guilds.append({
                    'id': guild.id,
                    'name': guild.name,
                    'member_count': guild.member_count,
                    'joined_at': member.joined_at.isoformat() if member.joined_at else None
                })
        
        return mutual_guilds
