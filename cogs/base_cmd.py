import disnake
from disnake.ext import commands

class CMDBase(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Ботяра {self.bot.user} готов к р&р!")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f"**<@{ctx.member.id}>**, у вас не домтаточно прав для использование данной комманды.")
        elif isinstance(error, commands.UserInputError):
            await ctx.send(f"Правильное использование данной команды: '{ctx.prefix}{ctx.command.name}' ({ctx.command.brief})\nПример: {ctx.prefix}{ctx.command.usage}")
    
def setup(bot):
    bot.add_cog(CMDBase(bot))