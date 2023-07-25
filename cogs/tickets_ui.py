import disnake
from disnake.ext import commands

class TicketInteractionUI(disnake.ui.View):
    def __init__(self):
        super().__init__()
    
    @disnake.ui.button(label="Создать тикет", style=disnake.ButtonStyle.green, emoji="📩")
    async def confirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.send("Бро, привет!")
        self.stop()

class TicketsUICMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.has_permissions(administrator=True)
    @commands.command(name="новоеТаблоТикетов", brief="Создаёт новое табло тикетов.", usage="новоеТаблоТикетов \"<name>\" \"<description>\"")
    async def создатьТаблоТикетов(self, ctx, name="Новое табло тикетов", desc="Для создания обращения нажмите на 📩"):
        embed = disnake.Embed(color=ctx.guild.me.color)
        embed.title=name
        embed.description=desc
        await ctx.send(embed=embed, view=TicketInteractionUI())

def setup(bot):
    bot.add_cog(TicketsUICMD(bot))