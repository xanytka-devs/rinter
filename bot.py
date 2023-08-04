import os
import disnake
from disnake.ext import commands
import cogs_manager
from cogs.tickets_ui import TicketInteractionUI

with open(os.path.dirname(os.path.realpath(__file__)) + '/token.txt') as file:
    TOKEN = file.readline().strip()
    DBNAME = file.readline().strip()
    DBLINK = file.readline().strip()
    DBUNAME = file.readline().strip()
    DBUPASS = file.readline().strip()

class BaseBot(commands.Bot):
    intents = disnake.Intents.all()
    def __init__(self):
        super().__init__()
        self.command_prefix=commands.when_mentioned_or("*")
        self.test_guilds=[1026584709599338647]
        self.persistent_views_added=False

    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(TicketInteractionUI())
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

cogs_manager.Manager.loadCogs(bot)

if __name__ == "__main__":
    bot.run(TOKEN)
