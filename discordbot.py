from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_message(message):
    if message.content == "!ping":
        await message.channel.send("pong!")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
