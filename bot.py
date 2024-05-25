import requests
from bs4 import BeautifulSoup
import discord

# Initialize Discord client
client = discord.Client()

# URL of the web page to monitor
url = "https://dafuqboom.shop"

# Variable to store the previous version of the content
previous_content = None

# Function to send message to Discord channel
async def send_message(message):
    channel_id = 1243967560647577710  # Replace with your Discord channel ID
    channel = client.get_channel(channel_id)
    await channel.send(message)

# Function to check for updates
async def check_for_updates():
    global previous_content
    while True:
        # Retrieve the content of the web page
        response = requests.get(url)
        current_content = response.text

        # Check if there's a difference between current and previous content
        if current_content != previous_content:
            # Send notification to Discord channel
            await send_message("The web page has been updated!")

            # Update previous_content with the current content
            previous_content = current_content

        # Wait for a certain amount of time before checking again
        await asyncio.sleep(60)  # Check every minute

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    # Start checking for updates
    await check_for_updates()

# Run the bot
client.run('YOUR_DISCORD_BOT_TOKEN')  # Replace with your Discord bot token
