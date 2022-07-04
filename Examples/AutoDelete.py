import nextcord
from nextcord.ext import commands
from nextcord import Interaction



class AutoDelete(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    # Delete a sent message after a certain amount of time
    @nextcord.slash_command(name = "hello", description = "Says hello to you")
    async def hello(self, ctx: Interaction):
        
        await ctx.send("Hi", delete_after = 10) # delete_after = 10 will delete the sent message after 10 seconds




def setup(bot):
    bot.add_cog(AutoDelete(bot))