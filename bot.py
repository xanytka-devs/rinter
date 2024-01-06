if __name__ == "__main__":
    import os
    import disnake
    from disnake.ext import commands
    import cogs_manager
    from cogs.tickets_ui import *

    with open(os.path.dirname(os.path.realpath(__file__)) + '/token.txt') as file:
        TOKEN = file.readline().strip()
        DBNAME = file.readline().strip()
        DBLINK = file.readline().strip()
        DBUNAME = file.readline().strip()
        DBUPASS = file.readline().strip()

    class BaseBot(commands.Bot):
        intents = disnake.Intents.all()
        def __init__(self):
            super().__init__(command_prefix=commands.when_mentioned)
            self.command_prefix=commands.when_mentioned
            self.test_guilds=[1026584709599338647]
            self.persistent_views_added=False

        async def on_ready(self):
            if not self.persistent_views_added:
                self.add_view(TicketCreationUI(None))
                self.add_view(TicketInteractionUI())
                self.add_view(TicketCloseUI())
                self.add_view(TicketAdminInteractionUI())
                self.persistent_views_added = True

    bot = BaseBot()

    @bot.command()
    @commands.is_owner()
    async def load(ctx, extencion):
        bot.load_extension(f"cogs.{extencion}")
        print(f"Расширение '{extencion}' было загружено.")

    @bot.command()
    @commands.is_owner()
    async def unload(ctx, extencion):
        bot.unload_extension(f"cogs.{extencion}")
        print(f"Расширение '{extencion}' было отгружено.")

    @bot.command()
    @commands.is_owner()
    async def reload(ctx, extencion):
        bot.reload_extension(f"cogs.{extencion}")
        print(f"Расширение '{extencion}' было перезагружено.")

    @bot.event
    async def on_command_error(ctx, error):
        print(error)
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply(f"У вас не доcтаточно прав для использование данной комманды.")
        if isinstance(error, commands.UserInputError):
            await ctx.reply(f"Правильное использование команды '{ctx.prefix}{ctx.command.name}': ({ctx.command.brief})\nПример: {ctx.prefix}{ctx.command.usage}")
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply(f"Команда '{ctx.message.content}' не существует.")
        if isinstance(error, commands.DisabledCommand):
            await ctx.reply(f"Команда '{ctx.prefix}{ctx.command.name}' не доступна.")
        if isinstance(error, commands.TooManyArguments):
            await ctx.reply(f"Ваша команда '{ctx.prefix}{ctx.command.name}' имеет слишком много аргументов."
                           + f"Правильное использование данной команды: ({ctx.command.brief})\nПример: {ctx.prefix}{ctx.command.usage}", )
        if isinstance(error, commands.TooManyArguments):
            await ctx.reply(f"Команда '{ctx.prefix}{ctx.command.name}' имеет ограничение в частоте использования.")

    cogs_manager.Manager.loadCogs(bot)
    bot.run(TOKEN)
