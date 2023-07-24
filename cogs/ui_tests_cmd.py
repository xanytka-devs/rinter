from typing import Optional
import disnake
from disnake.ext import commands

class Confirm(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=10.0)
        self.value = Optional[bool]
    
    @disnake.ui.button(label="Го", style=disnake.ButtonStyle.green, emoji="🤣")
    async def confirm(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.response.send_message("Брух 💀", ephemeral=True)
        self.value = True
        self.stop()
    
    @disnake.ui.button(label="Ратио", style=disnake.ButtonStyle.red, emoji="🥱")
    async def cancel(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):
        await inter.response.send_message("Адьос 🙂", ephemeral=True)
        self.value = False
        self.stop()

class Dropdown(disnake.ui.StringSelect):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Красный", description="Активный как огонь.", emoji="🔴"),
            disnake.SelectOption(label="Жёлтый", description="Уравновешенный как земля.", emoji="🟡"),
            disnake.SelectOption(label="Зелёный", description="Спокойный как природа.", emoji="🟢"),
            disnake.SelectOption(label="Синий", description="Общительный как вода.", emoji="🔵"),
            disnake.SelectOption(label="Фиолетовый", description="Внезапный как молния.", emoji="🟣")
        ]

        super().__init__(
            placeholder="Цвет",
            min_values=1,
            max_values=1,
            options=options
        )
    async def callback(self, inter: disnake.MessageInteraction):
        await inter.response.send_message(f"Ваш элемент тепрь {self.values[0]}", ephemeral=True)

class DropdownView(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())

class UITestsCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Элемент")
    async def changeElement(self, ctx):
        await ctx.send("Выберите цвет вашего элемента:", view=DropdownView())

    @commands.command(name="Играть")
    async def ask_play(self, ctx):
        view = Confirm()
        await ctx.send("Бро, го играть до 3:33?", view=view)
        await view.wait()
        if view.value is not None:
            await ctx.send("Оке, игнорщик, я сам пошёл.")
    
def setup(bot):
    bot.add_cog(UITestsCMD(bot))