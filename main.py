import discord
from discord.ext import commands
import os, random
from get_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            nama_file = file.filename
            url_file = file.url
            await file.save(f'./{nama_file}')
            await ctx.send(f'File telah disimpan dengan nama {nama_file}')

            nama, skor = get_class(image='name_file', model='keras_model.h5', label='label.txt')

            #inferensi
            if nama == 'jadul\n' and skor >= 0.65:
                await ctx.send('Mobil ini adalah mobil jadul')
                await ctx.send('Mobil seperti ini sudah langka ditemukan yang membuat harganya lebih mahal')
                await ctx.send('Mobil jadul termahal pada saat ini adalah Mercedes-Benz 300 SLR Uhlenhaut Coupe dengan harga Rp2.2 triliun')
            elif nama == 'modern\n' and skor >= 0.65:
                await ctx.send('Mobil ini adalah mobil modern')
                await ctx.send('Mobil seperti ini ada banyak di jaman sekarang')
                await ctx.send('Salah satu mobil modern termahal saat ini adalah Rolls-Royce Boat Tail dengan harga Rp435 miliar ')   
            else:
                await ctx.send('Foto tersebut tidak dapat diidentifikasian sebagai mobil')

    else:
        await ctx.send('Tidak ada file yang dikirim')

bot.run("enter ur token")

