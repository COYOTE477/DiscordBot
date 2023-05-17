import discord
from discord.ext import commands
import youtube_dl
from discord_slash import cog_ext

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

#    @commands.command()
#    async def join(self,ctx):
#        if ctx.author.voice is None:
#          await ctx.send("shit you are not in vioce canal! fuck you")
#        voice_channel = ctx.author.voice.channel
#        if ctx.voice_client is None:
#          await voice_channel.connect()
#        else:
#          await ctx.voice_client.move_to(voice_channel)
#
#    @commands.command()
#    async def leave(self,ctx):
#      await ctx.voice_client.move_to(None)
#      
#    @commands.command()
#    async def play(self,ctx,url):
#      ctx.voice_client.stop
#      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': "-vn"}
#      YDL_OPTIONS = {'format':"bestaudio"}
#      vc = ctx.voice_client
#
#      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
#          info = ydl.extract_info(url, download=False)
#          url2 = info['formats'][0]['url']
#          source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
#          await ctx.send('Now playing: `FORTNITE SONG „Skybase“ Standart Skill feat. Ayana (Official Music Video)`')
#          vc.play(source)
    
#    @commands.command()
#    async def pause(self,ctx):
#      await ctx.send("paused le music")
#      await ctx.voice_client.pause()
#    
#    @commands.command()
#    async def resume(self,ctx):
#      await ctx.send("resumed le music")
#      await ctx.voice_client.resume()
#    
#    @commands.command()
#    async def gustavo(self,ctx):
#      await ctx.send('<:fring:887710632449810492>')
#    
#    @commands.command()
#    async def ping(self,ctx):
#      await ctx.send("pong")
#    
#    @commands.command()
#    async def say(self,ctx,msg):
#      await ctx.send(msg)
    
    @cog_ext.cog_slash(name='sex', description='sex')
    async def sex(self,ctx):
      await ctx.send('https://cdn.discordapp.com/attachments/891906925896273990/919865500924784650/1639200807906.jpg')
    
    @cog_ext.cog_slash(name='play', description='fart')
    async def play(self,ctx,url):
      ctx.voice_client.stop
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': "-vn"}
      YDL_OPTIONS = {'format':"bestaudio"}
      vc = ctx.voice_client

      with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
          info = ydl.extract_info(url, download=False)
          url2 = info['formats'][0]['url']
          source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
          await ctx.send('Now playing: `FORTNITE SONG „Skybase“ Standart Skill feat. Ayana (Official Music Video)`')
          vc.play(source)
    
    @cog_ext.cog_slash(name='join', description='balls')
    async def join(self,ctx):
        if ctx.author.voice is None:
          await ctx.send("shit you are not in vioce canal! fuck you")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
          await voice_channel.connect()
        else:
          await ctx.voice_client.move_to(voice_channel)
  

#    @commands.command()
#    async def ball(self,ctx):
#      await ctx.send(':red_circle:')
#    
#    @commands.command()
#    async def balls(self,ctx):
#      await ctx.send(':black_circle: :white_circle: :brown_circle: :red_circle: :blue_circle: :green_circle: :orange_circle: #:yellow_circle: :purple_circle:')
#    @commands.command()
#    async def donate(self,ctx):
#        embed=discord.Embed(title="BUY THIS", url="https://www.amazon.com/Bulex-Action-Figure-Desktop-Decoration/dp/B08DRKR89Z/#ref=sr_1_2?crid=3HBRUHHGQTC4B&keywords=white+people+be+like", description="PLEASE", color=0x0d49ab)
#        embed.add_field(name="buy pleasE", value="ITS ONLY", inline=True)
#        embed.add_field(name="pease bro PLASE", value="20 DOLLARS", inline=True)
#        embed.set_footer(text="please")
#        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(music(client))