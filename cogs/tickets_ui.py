from datetime import datetime
import disnake
from disnake.ext import commands

ticketCategory = "1137130340830416917"

class TicketInteractionUI(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Закрыть", style=disnake.ButtonStyle.gray, emoji="🔒", custom_id="ticket_interaction:close")
    async def close(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        overwrites = {
            inter.guild.default_role: disnake.PermissionOverwrite(view_channel=False),
            inter.guild.me: disnake.PermissionOverwrite(view_channel=True),
            inter.author: disnake.PermissionOverwrite(send_messages=False)
        }
        await inter.channel.edit(overwrites=overwrites)
        await inter.channel.send("Вы уверены?", view=TicketCloseUI())

class TicketAdminInteractionUI(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Открыть", style=disnake.ButtonStyle.gray, emoji="🔓", custom_id="ticket_admin:open")
    async def open(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        overwrites = {
            inter.guild.default_role: disnake.PermissionOverwrite(view_channel=False),
            inter.guild.me: disnake.PermissionOverwrite(view_channel=True),
            inter.bot.get_user(int(inter.channel.topic)): disnake.PermissionOverwrite(view_channel=True)
        }
        await inter.channel.edit(overwrites=overwrites)
        await inter.channel.delete_messages([inter.bot.get_message(inter.channel.last_message_id)])
        await inter.channel.send(f"Тикет был открыт **<@{inter.author.id}>**")
        self.stop()
    
    @disnake.ui.button(label="Удалить", style=disnake.ButtonStyle.gray, emoji="🛑", custom_id="ticket_admin:delete")
    async def delete(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        await inter.channel.delete()
        self.stop()

class TicketCloseUI(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Закрыть", style=disnake.ButtonStyle.red, custom_id="ticket_close:close")
    async def close(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        overwrites = {
            inter.guild.default_role: disnake.PermissionOverwrite(view_channel=False),
            inter.guild.me: disnake.PermissionOverwrite(view_channel=True),
            inter.author: disnake.PermissionOverwrite(view_channel=False, send_messages=True)
        }
        await inter.channel.edit(overwrites=overwrites)
        await inter.channel.delete_messages([inter.bot.get_message(inter.channel.last_message_id)])
        await inter.channel.send(f"Тикет был закрыт **<@{inter.author.id}>**")
        embed = disnake.Embed(color=int(hex(int('0x388E3C',16)),0))
        embed.title = "Панель администрирования тикета"
        embed.description = "Что дальше делать с тикетом?"
        await inter.channel.send(embed=embed, view=TicketAdminInteractionUI())
        self.stop()
    
    @disnake.ui.button(label="Отмена", style=disnake.ButtonStyle.gray, custom_id="ticket_close:cancel")
    async def cancel(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        overwrites = {
            inter.guild.default_role: disnake.PermissionOverwrite(view_channel=False),
            inter.guild.me: disnake.PermissionOverwrite(view_channel=True),
            inter.author: disnake.PermissionOverwrite(send_messages=True)
        }
        await inter.channel.edit(overwrites=overwrites)
        await inter.channel.delete_messages([inter.bot.get_message(inter.channel.last_message_id)])
        self.stop()

class TicketCreationUI(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Создать тикет", style=disnake.ButtonStyle.green, emoji="📩", custom_id="ticket_interaction:create")
    async def confirm(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):
        chName = inter.author.name + "-" + datetime.utcnow().strftime('%d.%m.%Y.%H:%M')
        overwrites = {
            inter.guild.default_role: disnake.PermissionOverwrite(view_channel=False),
            inter.guild.me: disnake.PermissionOverwrite(view_channel=True),
            inter.author: disnake.PermissionOverwrite(view_channel=True)
        }
        channel = await inter.guild.create_text_channel(chName, category=inter.guild.get_channel(ticketCategory),
                                                        overwrites=overwrites, topic=inter.author.id)
        spEmb = disnake.Embed(color=int(hex(int('0x388E3C',16)),0))
        spEmb.title="Поддержка скоро прибудет"
        spEmb.description="Управление тикетом"
        await channel.send(f"Привет, **<@{inter.author.id}>**!", embed=spEmb, view=TicketInteractionUI())


class TicketsUICMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(name="новоеТаблоТикетов", description="Создаёт новое табло тикетов.")
    async def новоеТаблоТикетов(self, ctx, name="Новое табло тикетов", desc="Для создания обращения нажмите на 📩"):
        embed = disnake.Embed(color=int(hex(int('0x388E3C',16)),0))
        embed.title = name
        embed.description = desc
        await ctx.send(embed=embed, view=TicketCreationUI())


def setup(bot):
    bot.add_cog(TicketsUICMD(bot))
