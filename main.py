import discord
from discord.ext import commands
import os
import logging
from dotenv import load

load('.env')

token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler('discord.log', mode='w')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready to go. Good job, little piggy!")

@bot.event
async def on_message(message):
    if message.channel.name == 'counting':
        messages = [m async for m in message.channel.history(limit=2)]
        previous = messages[1]
        current = messages[0]

        try:
            previous = int(previous.content)
            current = int(current.content)
        
            if current != previous + 1:
                await message.delete()
            else:
                print("Congrats, piggy! Your not as dumb as you look, oink oink!")

        except ValueError:
            print("the message is not a number, piggy!")
            await message.delete()
        await bot.process_commands(message)



bot.run(token=token, log_handler=handler, log_level=logging.DEBUG)