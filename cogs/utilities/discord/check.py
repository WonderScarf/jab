import discord

from discord.ext import commands

class Check:

    def if_in_channel(self, ctx, reservedChannelId:int):
        return ctx.TextChannel.id == reservedChannelId
    
    
    


    
        
    
