import discord
import random
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hai! Saya adalah bot {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def justin(ctx):
    await ctx.send("Hi my name is Justin, nice to meet you !")

@bot.command()
async def holla(ctx, count_number=10):
    await ctx.send("hi" * count_number)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

bot.run("")
