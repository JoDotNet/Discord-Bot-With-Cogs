import nextcord
from nextcord.ext import commands
from nextcord import Interaction

import os

import bot_data



intents = nextcord.Intents.default()

bot = commands.Bot(intents = intents)

# Configuring Intents you might need E.G. <intents.members = True>


# The fuction below will run when the bot starts
@bot.event
async def on_ready():

    print(f'Logged in as: {bot.user}') # Will print out logged in as: bot#1234 (Your BOT's Name)



# Ping
# Useful to check if the bot is responding normally
@bot.slash_command(name = "ping", description = "Check if the bot responds as normal")
async def ping(ctx: Interaction):

    await ctx.send("Pong :ping_pong:") # ctx.send will send the message in the channel the user sent the slash_command in





# Adding Cogs
# You don't need to understand it, but it just adds it to our bot's cogs

initial_extentions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extentions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extention in initial_extentions:
        bot.load_extension(extention)



bot.run(bot_data.bot_token) # Running our bot, be sure to add your token in bot_data.py