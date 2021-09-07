import discord

from cogs.utilities.games_of_chance import Chance
from discord.ext import commands


class Games(commands.Cog):

    def __init__ (self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def dice(self, ctx, sides:int):
        'Gets a number of dice sides and generates and returns a random number in that range'
        
        result = Chance.diceRoll(sides)
        if result == -1:
            retort = 'There was an error, make sure the number of sides is a number greater than 1'
        else:
            retort = 'The result of the dice roll is a ' + str(result) + '.'
        await ctx.send(retort)