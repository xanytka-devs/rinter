import os
import disnake
from disnake.ext import commands

with open(os.path.dirname(os.path.realpath(__file__)) + '/token.txt') as file:
    TOKEN = file.readline().strip()
    DBNAME = file.readline().strip()
    DBLINK = file.readline().strip()
    DBUNAME = file.readline().strip()
    DBUPASS = file.readline().strip()

class BaseBot(commands.Bot):
    intents=disnake.Intents.all()
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned)
        self.test_guilds=[1026584709599338647]
        self.command_prefix=commands.when_mentioned_or("*")
        self.persistent_views_added = False
        self.help_command=None

    async def on_ready(self):
        if not self.persistent_views_added:
            #self.add_view(())
            self.persistent_views_added = True

bot = BaseBot()

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

if __name__ == "__main__":
    bot.run(TOKEN)
