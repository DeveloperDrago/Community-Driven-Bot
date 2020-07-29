import discord
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def yeet(self, ctx, user: discord.Member):
        await delmsg(ctx)
        author = ctx.author
        embed = discord.Embed(
            color=discord.Color(0xff56c5),
            description=f'{author.mention} has yeeted {user.mention}!'
        )
        embed.set_image(url='https://cdn.discordapp.com/attachments/443829372479209485/705171706293256253/tenor_2.gif')
        await ctx.send(embed=embed)


# Message deletion System
async def delmsg(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        return
    else:
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return


def setup(bot):
    bot.add_cog(Fun(bot))
