import discord
from discord.ext import commands
import time
import pathlib

bot = commands.Bot("")

YOUR_GUILD_ID = 0
YOUR_CHANNEL_ID = 0
YOUR_BOT_TOKEN = ""
PATH_OF_DIRSONGS = "./songs"

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds,id=YOUR_GUILD_ID)

    voice_channel:discord.VoiceChannel = discord.utils.get(guild.voice_channels, id=YOUR_CHANNEL_ID)

    class Queue(list):
        def __init__(self,names,voice):
            super(Queue,self).__init__(names)
            self.voice = voice
            self.pos = 0
            self.max = len(names) - 1

        def play(self):
            self.voice.play(discord.FFmpegPCMAudio(source=self[self.pos]),after=self.manager)
            now = time.localtime(time.time())
            print(f"({now.tm_hour:02}:{now.tm_min:02}:{now.tm_sec:02})","Piste n°"+str(self.pos),"est lancée sans aucun problème !")
        def manager(self,err=None):
            if err:
                print(err)
            if self.pos == self.max:
                self.pos = 0
            else:
                self.pos += 1
            
            self.play()



    async def main():
        if voice_channel != None:
            vc:discord.VoiceClient = await voice_channel.connect()

            queue = []

            for file in pathlib.Path(PATH_OF_DIRSONGS).iterdir():
                queue.append(file)

            _Queue = Queue(queue,vc)

            _Queue.play()

        else:
            await print("Error!")
    await main()
    print("Le bot est lancé la musique va démarer !")

bot.run(YOUR_BOT_TOKEN)
