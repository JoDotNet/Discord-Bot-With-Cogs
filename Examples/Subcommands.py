import nextcord
from nextcord.ext import commands
from nextcord import Interaction



class Subcommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # Example using Fruit as main command and adding subcommands with different fruit names
    @nextcord.slash_command(name = "fruit")
    async def fruit(self):
        pass # We have to add pass, because we will not be running the command.


    # Adding subcommand to Fruit that will send Apple
    @fruit.subcommand(name = "apple")
    async def apple(self, ctx: Interaction):

        await ctx.send("Apple")



def setup(bot):
    bot.add_cog(Subcommands(bot))