import discord

from cogs.utilities.file_management import Txt

from discord.ext import commands
# * means do not say the name of the role

class Role(commands.Cog):
    'Cog that includes ways to manage roles and their permisions.'

    def __init__ (self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def newrole(self, ctx, roleName:str, red:int, green:int, blue:int, roleType:int=3, shownSeparately:bool=False): #0=admin,1=highmod,2=lowmod,3=standard
        'Adds a new role to the current guild. Takes in a unique name, 3 values up to 255 representing red, green and blue values respectively, a permision type from 0 to 3 (0 = admin, 1 = highmod, 2 = lowmod, 3 = standard user) and a bool to check if the user is shown separately to the other roles.'
        
        rgbMax = 255 #rgb values must be from 0 to 255

        #Checks the current guild to see if the name chosen is already existing exiting if thats the case 
        for role in ctx.guild.roles:
            if role.name == roleName:
                await ctx.send("I'm unable to create that role as there is already a role with that name.")
                return
        
        for colorValue in [red, green, blue]:
            if colorValue > rgbMax or colorValue < 0:
                await ctx.send("I'm sorry but a rgb value must be in the range of 0 to {0}.".format(rgbMax))
                return

        roleTypeData = Txt.read(r'cogs\utilities\txtFiles\roles.txt') #reads the data in the roles file
        
        #Checks to see if the roleType is a type that is within the range of scope in the files
        if len(roleTypeData) <= roleType or roleType < 0:
            await ctx.send("The role type you have input doesn't exist. The possible types range from 0 to {0}.".format(len(roleTypeData) - 1))
            return

        
        rolePerms = roleTypeData[roleType].split('|') #splits the specified line (representing a role type) by '|' which stand for true or false for that role and put it into a new list.
        
        perms = discord.Permissions(administrator=bool(rolePerms[0]), manage_guild=bool(rolePerms[1]), manage_channels=bool(rolePerms[2]), ban_members=bool(rolePerms[3]), kick_members=bool(rolePerms[4])) #each of the 5 sections in the rolePerms (as there are 5 perms to manage) is converted to a bool and used to make a Permisions object.

        await ctx.guild.create_role(name=roleName, color=discord.Color.from_rgb(red,green,blue), permissions=perms, hoist=shownSeparately)
        await ctx.send("The role of '{0}' has been added sucessfully.".format(roleName))
    
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def equiprole(self, ctx, target: discord.Member, roleName: discord.Role):
        await target.add_roles(roleName, atomic=True)
        await ctx.send("The role of '{0}' has been equiped to '{1}' sucessfully.".format(roleName,target.display_name))
    
    @commands.command(pass_context=True)
    async def displayroles(self, ctx):
        currentRole = 0
        roleEmbed = discord.Embed(
            title = 'Roles',
            color = discord.Color.from_rgb(0,204,204)
        )

        while currentRole < len(ctx.guild.roles):
            roleEmbed.add_field(name= ctx.guild.roles[currentRole].name, value=ctx.guild.roles[currentRole].permissions, inline=True)
            currentRole += 1
        await ctx.send(embed=roleEmbed)