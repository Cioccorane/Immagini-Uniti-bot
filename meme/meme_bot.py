import discord
import random
import os
from discord.ext import commands


# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')


@bot.command()
async def ciao(ctx, nome):
    await ctx.send(f'Ciao {nome}!')


@bot.command()
async def meme(ctx):
    lista_file = os.listdir('img')
    random_file = random.choice(lista_file)
    
    with open(f'img/{random_file}', 'rb') as f:
        discord_file = discord.File(f)
        await ctx.send(file=discord_file)

@bot.command()
async def memeanimali(ctx):
    lista_file = os.listdir('meme_animali')
    random_file = random.choice(lista_file)
    
    with open(f'meme_animali/{random_file}', 'rb') as f:
        discord_file = discord.File(f)
        await ctx.send(file=discord_file)
        
@bot.command()
async def memeharry(ctx):
    lista_file = os.listdir('meme_harry_potter')
    random_file = random.choice(lista_file)
    
    with open(f'meme_harry_potter/{random_file}', 'rb') as f:
        discord_file = discord.File(f)
        await ctx.send(file=discord_file)
        


bot.run("")