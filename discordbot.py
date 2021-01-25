from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_message(message):
    if client.user in message.mentions:
        reply = f'{message.author.mention} 呼んだ？'
        await message.channel.send(reply)
        
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
