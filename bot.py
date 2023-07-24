import os
import disnake
from disnake.ext import commands

with open(os.path.dirname(os.path.realpath(__file__)) + '/token.txt') as file:
    TOKEN = file.readline().strip()

bot = commands.Bot(command_prefix="^", help_command=None, intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f"Ботяра {bot.user} готов к р&р!")

@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    await channel.send(f"Вечер в хату, {member.name}!")

@bot.command()
@commands.has_permissions(administrator=True)
async def send_embed(channel = disnake.channel, msg = "", desc = "", colour = 0x7289da):
    embed = disnake.Embed(
        title=msg,
        description=desc,
        color=0x7289da
    )
    await channel.send(embed=embed)

bot.run(TOKEN)