import os
import disnake
from disnake.ext import commands

class Manager:
    def loadCogs(bot):
        print("Идёт загрузка расширений...")
        # Check for ignored cogs.
        isWhitelist = False
        loadItems = []
        with open(os.path.dirname(os.path.realpath(__file__)) + '/token.txt', 'r') as file:
            for line in file:
                if line.startswith('#') or line == '\n' or line == '\n'or line == ')':
                    continue
                if line == "only=(":
                    isWhitelist = True
                loadItems.append(line.strip(',').strip())
        # Load cogs.
        loadedExt = False
        for filename in os.listdir("cogs"):
            if filename.endswith(".py"):
                loadedExt = False
                for item in loadItems:
                    if loadedExt: break
                    if isWhitelist and filename == item:
                        bot.load_extension(f"cogs.{filename[:-3]}")
                        print(f"Расширение {filename[:-3]} было загружено.")
                        loadedExt = True
                    elif not isWhitelist and filename != item:
                        bot.load_extension(f"cogs.{filename[:-3]}")
                        print(f"Расширение {filename[:-3]} было загружено.")
                        loadedExt = True