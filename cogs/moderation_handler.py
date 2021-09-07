import discord
from discord.ext import commands

class Kick(commands.Cog):
    'Cog that contains comands involving kicking users from a guild.'

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, target:discord.Member, *, kickReason:str="none"):
        'Kicks a member of current guild. 1st takes the member, then the reason for the kick.'

        await ctx.guild.ban(user=target, reason=kickReason)
        await ctx.send('{0} has been kicked from {1} with the reason of: {2}.'.format(target, ctx.guild.name, kickReason))

class Ban(commands.Cog):
    'Cog that contains comands involving banning and unbanning users from a guild.'

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, target:discord.Member, *, banReason:str="none"):
        'Bans a member of current guild. 1st takes the member, then the reason for the ban.'

        await ctx.guild.ban(user=target, reason=banReason)
        await ctx.send('{0} has been banned from {1} with the reason of: {2}.'.format(target, ctx.guild.name, banReason))

    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, target:discord.Member,*, unbanReason:str="None"):
        'Unbans a previous member of current guild. 1st takes the member, then the reason for the unban.'

        await ctx.guild.unban(user=target, reason=unbanReason)
        await ctx.send('{0} has been banned from {1} with the reason of: {2}.'.format(target, ctx.guild.name, unbanReason))

