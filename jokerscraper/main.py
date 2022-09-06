import discord
from webscraper import pickRandomQuote, initSleepy


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, Batman.')

    if message.content.startswith('$joker'):
        await message.channel.send(pickRandomQuote())

    if message.content.startswith('$snooze'):
        await message.channel.send(initSleepy())

client.run("OTg0MjQ1NDAyMTA0NjQ3NzIw.GUjRUJ.Foc9ywna4P7tOwhaPO9HMkMSa5pwWVG23EPVhw")