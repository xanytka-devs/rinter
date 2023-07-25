from datetime import datetime
import disnake
from disnake.ext import commands

class CMDBase(commands.Cog):

    launched_at = None

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        if self.launched_at is None:
            self.launched_at = datetime.utcnow()
        print(f"Ботяра {self.bot.user} готов к р&р!")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.reply(f"**<@{ctx.message.author.id}>**, у вас не доcтаточно прав для использование данной комманды.", delete_after=10.0)
        elif isinstance(error, commands.UserInputError):
            await ctx.message.reply(f"**<@{ctx.message.author.id}>**, правильное использование команды '\{ctx.prefix}{ctx.command.name}': ({ctx.command.brief})\nПример: \{ctx.prefix}{ctx.command.usage}", delete_after=10.0)
        elif isinstance(error, commands.CommandNotFound):
            await ctx.message.reply(f"Команда '\{ctx.prefix}{ctx.message.content}' не существует.")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.message.reply(f"Команда '\{ctx.prefix}{ctx.command.name}' не доступна.")
        elif isinstance(error, commands.TooManyArguments):
            await ctx.message.reply(f"**<@{ctx.message.author.id}>**, ваша команда '\{ctx.prefix}{ctx.command.name}' имеет слишком много аргументов."
                           + f"Правильное использование данной команды: ({ctx.command.brief})\nПример: \{ctx.prefix}{ctx.command.usage}", delete_after=10.0)
        elif isinstance(error, commands.TooManyArguments):
            await ctx.message.reply(f"**<@{ctx.message.author.id}>**, команда '\{ctx.prefix}{ctx.command.name}' имеет ограничение в частоте использования.", delete_after=10.0)
    
    @commands.slash_command(name="данные", description="Выдаёт текущие данные о боте.")
    async def info(self, ctx):
        embed = disnake.Embed(color=ctx.guild.me.color)
        uptime = datetime.utcnow() - self.launched_at
        embed.set_thumbnail(url=ctx.bot.user.avatar.url)
        embed.title = self.bot.user.name
        embed.add_field(name="Сервера", value=str(len(ctx.bot.guilds)))
        embed.add_field(name="Задержка", value=f"{round(ctx.bot.latency * 1000, 2)} ms")
        embed.add_field(name="Держится на плаву", value=str(uptime))
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(CMDBase(bot))