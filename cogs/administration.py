import disnake
from disnake.ext import commands

class AdministrationCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="вложение", description="Заменяет данный текст на вложение.")
    @commands.has_permissions(attach_files=True)
    async def вложение(self, ctx, заголовок="Новое вложение", описание=" "):
        embed = disnake.Embed()
        await self.bot.fetch_user(ctx.author.id)
        embed.color=ctx.author.accent_color
        embed.title=заголовок
        if not описание.isspace():
            embed.description=описание
        embed.set_author(
            name=ctx.author.name,
            icon_url=ctx.author.avatar
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AdministrationCMD(bot))