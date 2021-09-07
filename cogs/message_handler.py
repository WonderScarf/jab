import discord
from discord.ext import commands


class Message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context = True, description="Deletes messages from the most recent. The number set after the command is the amount of messages to be delete (not including the command).")
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, amount=1):
        amount += 1
        await ctx.channel.purge(limit=amount)

    @commands.command(pass_context = True)
    @commands.has_permissions(manage_messages=True)
    async def dm(self, ctx, target: discord.Member, *, message=None):
        await ctx.channel.purge(limit=1)
        await target.send(message)
        print("Jab+ has sent dm properly.")
        

    @commands.command(pass_context = True, description="I will repeat anything you say after the command.")
    @commands.has_permissions(manage_messages=True)
    async def mimic(self, ctx, *, message):
        await ctx.channel.purge(limit=1)
        await ctx.send(message)
    
    @commands.command(pass_context=True)
    async def poll(self,ctx, *, question:str):
        await ctx.message.add_reaction('👍')
        await ctx.message.add_reaction('👎')
    
    