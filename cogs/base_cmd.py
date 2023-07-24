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
            await ctx.reply(f"**<@{ctx.member.id}>**, у вас не домтаточно прав для использование данной комманды.", ephemeral=True)
        elif isinstance(error, commands.UserInputError):
            await ctx.reply(f"Правильное использование команды '{ctx.prefix}{ctx.command.name}': ({ctx.command.brief})\nПример: {ctx.prefix}{ctx.command.usage}", ephemeral=True)
        elif isinstance(error, commands.CommandNotFound):
            await ctx.reply(f"Команда '{ctx.prefix}{ctx.message.content}' не существует. Проверьте словарь.")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.reply(f"Команда '{ctx.prefix}{ctx.command.name}' не доступна.")
        elif isinstance(error, commands.TooManyArguments):
            await ctx.reply(f"Ваша команда '{ctx.prefix}{ctx.command.name}' имеет слишком много аргументов."
                           + f"Правильное использование данной команды: ({ctx.command.brief})\nПример: {ctx.prefix}{ctx.command.usage}", ephemeral=True)
        elif isinstance(error, commands.TooManyArguments):
            await ctx.reply(f"Команда '{ctx.prefix}{ctx.command.name}' имеет ограничение в частоте использования.", ephemeral=True)
    
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