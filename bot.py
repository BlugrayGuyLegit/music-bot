import discord
from discord.ext import commands
import youtube_dl

# Initialisation du bot
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

@bot.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    if voice_channel is None:
        await ctx.send("Vous devez être dans un salon vocal pour utiliser cette commande.")
    else:
        await voice_channel.connect()
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }
        YDL_OPTIONS = {'format': 'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

@bot.command()
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

bot.run('DISCORD_BOT_TOKEN')
