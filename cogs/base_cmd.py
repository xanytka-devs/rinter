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