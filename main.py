import os
import discord
import requests
from dotenv import load_dotenv
load_dotenv()

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Environment variables
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
COOLIFY_API_TOKEN = os.getenv('COOLIFY_API_TOKEN')
PROJECT_ID = os.getenv('PROJECT_ID')
SERVICE_ID = os.getenv('SERVICE_ID')
COOLIFY_URL = os.getenv('COOLIFY_URL')

@client.event
async def on_ready():
    """Called when the bot is ready and connected to Discord."""
    print(f'{client.user} has connected to Discord!')
    print(f'Bot is in {len(client.guilds)} guild(s)')

@client.event
async def on_message(message):
    """Handle incoming messages."""
    # Ignore messages from other bots
    if message.author.bot:
        return

    # Check if the message is the startmc command
    if message.content.lower() == '!startmc':
        await handle_startmc_command(message)

async def handle_startmc_command(message):
    """Handle the !startmc command by calling the Coolify API."""
    # Send initial response
    await message.channel.send("🚀 Triggering Minecraft server startup...")
    
    try:
        # Prepare the API request
        api_url = f"{COOLIFY_URL}/api/v1/projects/{PROJECT_ID}/services/{SERVICE_ID}/deploy"
        headers = {
            'Authorization': f'Bearer {COOLIFY_API_TOKEN}',
            'Content-Type': 'application/json'
        }
        
        # Make the POST request to Coolify
        response = requests.post(api_url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            await message.channel.send("Minecraft server deployment started via Coolify!")
        else:
            error_message = f"Error starting server: {response.status_code}\n```{response.text}```"
            await message.channel.send(error_message)
            
    except requests.exceptions.RequestException as e:
        error_message = f"Error starting server: Network error\n```{str(e)}```"
        await message.channel.send(error_message)
    except Exception as e:
        error_message = f"Error starting server: Unexpected error\n```{str(e)}```"
        await message.channel.send(error_message)

def main():
    """Main function to run the bot."""
    if not DISCORD_BOT_TOKEN:
        print("Error: DISCORD_BOT_TOKEN not found in environment variables")
        return
    
    if not all([COOLIFY_API_TOKEN, PROJECT_ID, SERVICE_ID, COOLIFY_URL]):
        print("Error: Missing required Coolify configuration in environment variables")
        print("Required: COOLIFY_API_TOKEN, PROJECT_ID, SERVICE_ID, COOLIFY_URL")
        return
    
    print("Starting Discord Minecraft Bot...")
    print(f"Coolify URL: {COOLIFY_URL}")
    print(f"Project ID: {PROJECT_ID}")
    print(f"Service ID: {SERVICE_ID}")
    
    try:
        client.run(DISCORD_BOT_TOKEN)
    except discord.LoginFailure:
        print("Error: Invalid Discord bot token")
    except Exception as e:
        print(f"Error starting bot: {e}")

if __name__ == "__main__":
    main() 