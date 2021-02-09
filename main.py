import discord
import os
from pycoingecko import CoinGeckoAPI
from keep_alive import keep_alive

# coin gecko instantiation
cg = CoinGeckoAPI()

# instantiate the discord client
client = discord.Client()

# start up event


@client.event
async def on_ready():
    print("We have logged on as {0.user}".format(client))


def get_coin_price(coin):
    try:
        coin_info = cg.get_price(ids=coin, vs_currencies='usd')
        coin_price = coin_info[coin]['usd']
        coin_format = f'{coin_price:,}'
        coin_message = "The price of " + coin + " is $" + coin_format
    except KeyError:
        return "Error: Check the coin name eg. XRP is 'ripple'"

    return coin_message


def get_coin24(coin):
    try:
        coin_info = cg.get_price(
            ids=coin, vs_currencies='usd', include_24hr_change='true')

        coin_change = coin_info[coin]['usd_24h_change']

        formatted_change = f'%{round(coin_change,4):,}'

        message = "The change of " + coin + " in the last 24 hours is: " + formatted_change

    except KeyError:
        return "Error: Check the coin name eg. XRP is 'ripple'"

    return message


# message events
@client.event
async def on_message(message):
    if message.author == client:
        return

    msg = message.content

    # function to check the price of most coins
    if msg.startswith("%price"):
        coin_id = msg.split("%price ", 1)[1]
        coin_message = get_coin_price(coin_id)
        await message.channel.send(coin_message)

    # function to check the coin change in the last 24h
    if msg.startswith("%change"):
        coin_id = msg.split("%change ", 1)[1]
        coin_message = get_coin24(coin_id)
        await message.channel.send(coin_message)


# keep the server keep_alive
keep_alive()

# run the bot
client.run(os.getenv('TOKEN'))
