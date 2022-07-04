import nextcord
from nextcord.ext import commands
from nextcord import Interaction

import bot_data


class ExampleCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Example Command
    @nextcord.slash_command(name = "hello", description = "This makes the bot say hi")
    async def hello(self, ctx: Interaction): # Always pass in <self> followed by <ctx: Interaction>
        
        await ctx.send("Hi") # ctx.send will send the message in the channel the user sent the slash_command in



def setup(bot):
    bot.add_cog(ExampleCog(bot))