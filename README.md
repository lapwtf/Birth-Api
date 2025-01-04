# Discord Bot API Collection

This folder contains a collection of API classes that provide easy-to-use interfaces for common Discord bot operations.

## Available APIs

### UserAPI
Handles user-related operations:
- Get user information
- Get member roles
- Get mutual guilds

### GuildAPI
Manages guild (server) operations:
- Get guild information
- Get guild channels
- Get guild roles

### ModerationAPI
Provides moderation functionality:
- Ban users
- Kick users
- Timeout users
- Get ban list

### MessageAPI
Handles message operations:
- Send messages
- Edit messages
- Delete messages
- Get message history

## Usage Example

```python
from api import UserAPI, GuildAPI, ModerationAPI, MessageAPI

# Initialize the APIs with your bot instance >.<
user_api = UserAPI(bot)
guild_api = GuildAPI(bot)
mod_api = ModerationAPI(bot)
message_api = MessageAPI(bot)

# example: get user information lol
async def get_user(user_id: int):
    user_info = await user_api.get_user_info(user_id)
    if user_info:
        print(f"Found user: {user_info['name']}")
```

## Requirements
- discord.py==1.7.3
- Python 3.8+

## Note
Make sure your bot has the necessary permissions to perform these operations in the guild.
