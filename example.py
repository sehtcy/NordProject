#using discord API
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)

@client.command()
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)

@client.event
async def on_ready():
    print('The Bot is on.')

    general_channel = client.get_channel('insert channel ID #')
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('testing'))
    await general_channel.send('To get started, type .commands')

@client.command(name='commands')
async def commands(ctx):
    myEmbed = discord.Embed(title="Commands", description="clear", color=0xffd700)
    await ctx.message.channel.send(embed=myEmbed)

client.run('insert token here')
