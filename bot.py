import discord
from discord.ext import commands

from cogs.role_handler import Role
from cogs.error_handler import CommandErrorHandler
from cogs.games_handler import Games
from cogs.message_handler import Message
from cogs.moderation_handler import Ban,Kick
from cogs.translate_handler import Translate

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OWNER_ID = os.getenv('OWNER_ID')

bot = commands.Bot(command_prefix='?')
@bot.event
async def on_ready():
    #General information about the bot and owner status
    print("Jab has connected to discord!")
    print("Username: " + str(bot.user.name))
    print("Bot ID: " + str(bot.user.id))
    print("Owner ID: " + str(OWNER_ID))

    #sets the bot's rolet to 'playing: ...'    
    await bot.change_presence(activity=discord.Game(name="Disco Elysium"))

@bot.event
async def on_disconnect():
    print("Jab+ has disconeceted from discord.")

bot.add_cog(CommandErrorHandler(bot))
bot.add_cog(Message(bot)) 
bot.add_cog(Role(bot))
bot.add_cog(Games(bot))

bot.add_cog(Ban(bot))
bot.add_cog(Kick(bot))
bot.add_cog(Translate(bot))

bot.run(TOKEN)