import os
import disnake
from disnake.ext import commands

with open(os.path.dirname(os.path.realpath(__file__)) + '/token.txt') as file:
    TOKEN = file.readline().strip()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("*"), help_command=None, intents=disnake.Intents.all(), test_guilds=[1026584709599338647])

@bot.command()
@commands.is_owner()
async def load(ctx, extencion):
    bot.load_extension(f"cogs.{extencion}")
    print(f"Расширение {extencion} было загружено.")
@bot.command()
@commands.is_owner()
async def unload(ctx, extencion):
    bot.unload_extension(f"cogs.{extencion}")
    print(f"Расширение {extencion} было отгружено.")
@bot.command()
@commands.is_owner()
async def reload(ctx, extencion):
    bot.reload_extension(f"cogs.{extencion}")
    print(f"Расширение {extencion} было перезагружено.")

print("Идёт загрузка расширений...")
for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"Расширение {filename[:-3]} было загружено.")

bot.run(TOKEN)
