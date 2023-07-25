import disnake
from disnake.ext import commands

class AdministrationCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="вложение", description="Заменяет данный текст на вложение.")
    @commands.has_permissions(attach_files=True)
    async def вложение(self, ctx, title="Новое вложение", description="Описание"):
        embed = disnake.Embed(color=ctx.guild.me.color)
        embed.title=title
        embed.description=description
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AdministrationCMD(bot))