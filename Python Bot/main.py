import discord
from discord.ext import commands
import datetime
import json
import os


with open("./jsons/config.json") as f:
    cfg = json.load(f)
token = cfg["token"]


client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot is online.\n")
    await client.change_presence(activity=discord.Game(name="with a Community to develop me"), status=discord.Status.online)


# Ignore any other bot
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel

    if author.bot:
        return
    elif content == client.user.mention:
        await channel.send(f"My prefix is `!`! Type `!help` for more commands!")

    await client.process_commands(message)


# Ping command
@client.command()
async def ping(ctx):
    embed = discord.Embed(
        color=discord.Color(0xff56c5),
        timestamp=datetime.datetime.utcnow()
        )

    embed.add_field(
        name=f'Ping!',
        value=f'{round(client.latency * 1000)}ms'
    )

    await ctx.send(embed=embed)


# Reload command
@client.command(aliases=['rl'], description='Reload a cog.')
@commands.is_owner()
async def reload(ctx, extension):
    await delmsg(ctx)
    try:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Cog ``{extension}`` reloaded.')
    except commands.ExtensionNotLoaded:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Cog ``{extension}`` reloaded.')


# Unload Cog
@client.command(description='Unload a cog.')
@commands.is_owner()
async def unload(ctx, extension):
    await delmsg(ctx)
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Cog ``{extension}`` unloaded.')
    print(f'main.py: Cog {extension} unloaded')


# Load cog
@client.command(description='Load a cog.')
@commands.is_owner()
async def load(ctx, extension):
    await delmsg(ctx)
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Cog ``{extension}`` loaded.')
    print(f'main.py: Cog {extension} loaded.')


# Cog loader
for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')


# Message deletion System
async def delmsg(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        return
    else:
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            return


client.run(token)
