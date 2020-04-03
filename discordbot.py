from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token1 = os.environ['DISCORD_BOT_TOKEN1']
token2 = os.environ['DISCORD_BOT_TOKEN2']
token3 = os.environ['DISCORD_BOT_TOKEN3']
token4 = os.environ['DISCORD_BOT_TOKEN4']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
