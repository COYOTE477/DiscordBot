import discord
from discord.ext import commands
import youtube_dl
from discord_slash import cog_ext
import time
with open('log.txt', 'w') as f:
    f.write('readme')
class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @cog_ext.cog_slash(name='sex', description='sex')
    async def sex(self,ctx):
      await ctx.send('https://cdn.discordapp.com/attachments/891906925896273990/919865500924784650/1639200807906.jpg')
    
    @cog_ext.cog_slash(name='play', description='fart')
    async def play(self,ctx,url):
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': "-vn"}
      YDL_OPTIONS = {'format':"bestaudio"}
      vc = ctx.voice_client

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(url, download=False)
          url2 = info['formats'][0]['url']
          source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
          await ctx.send('Now playing: `FORTNITE SONG „Skybase“ Standart Skill feat. Ayana (Official Music Video)`')
          vc.play(source)
          time.sleep(5)
          await ctx.send('oops i meant ' + str(url))
          
    
    @cog_ext.cog_slash(name='join', description='balls')
    async def join(self,ctx):
        if ctx.author.voice is None:
          await ctx.send("shit you are not in vioce canal! fuck you")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
          await ctx.send("epic")
          await voice_channel.connect()
        else:
          await ctx.voice_client.move_to(voice_channel)
    @cog_ext.cog_slash(name='leave', description='you should leave the call now!!!!!!!!')
    async def leave(self,ctx):
      await ctx.voice_client.move_to(None)
      await ctx.send("die")
    
    @cog_ext.cog_slash(name='say', description='die')
    async def say(self,ctx,msg):
      await ctx.send('i am racist')

          
def setup(client):
    client.add_cog(music(client))