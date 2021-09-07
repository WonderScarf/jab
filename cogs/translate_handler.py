import discord
from discord.ext import commands

from googletrans import Translator, LANGCODES

class Translate(commands.Cog):
    'Cog to translates languages'

    def __init__ (self, bot):
        self.bot = bot
        self.trans = Translator()
    
    @commands.command(pass_context=True)
    async def translate(self, ctx, language:str, *, message:str):
        
        if language not in LANGCODES:
            await ctx.send("The language you input does not exist as a known language.")
            return
        translatedMessage = self.trans.translate(text=message, dest=language)
        await ctx.send(translatedMessage.text)
        
