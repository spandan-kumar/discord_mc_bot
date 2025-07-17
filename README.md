# Discord Minecraft Bot

A Python-based Discord bot that can start a Minecraft server via Coolify deployment API using the `!startmc` command.

## Features

- Listens for `!startmc` command in any Discord server
- Integrates with Coolify deployment API
- Runs 24/7 on VPS
- Ignores messages from other bots
- Provides real-time status updates

## Prerequisites

- Python 3.8 or higher
- A Discord bot token
- Coolify instance with API access
- VPS or server to run the bot 24/7

## Setup Instructions

### 1. Clone and Install Dependencies

```bash
cd discord_mc_bot
pip install -r requirements.txt
```

### 2. Create Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section
4. Create a bot and copy the token
5. Enable "Message Content Intent" under Privileged Gateway Intents

### 3. Configure Environment Variables

Copy the example environment file and configure your settings:

```bash
cp env.example .env
```

Edit `.env` with your actual values:

```env
# Discord Bot Configuration
DISCORD_BOT_TOKEN=your_actual_discord_bot_token

# Coolify API Configuration
COOLIFY_API_TOKEN=your_coolify_api_token
PROJECT_ID=your_project_id
SERVICE_ID=your_service_id
COOLIFY_URL=https://your-coolify-domain.com
```

### 4. Get Coolify Configuration

1. **API Token**: Generate an API token in your Coolify dashboard
2. **Project ID**: Find your project ID in the Coolify URL or dashboard
3. **Service ID**: Find your Minecraft service ID in the Coolify dashboard
4. **Coolify URL**: Your Coolify instance URL (e.g., https://coolify.mydomain.com)

### 5. Invite Bot to Discord Server

Use this URL (replace `YOUR_BOT_CLIENT_ID` with your bot's client ID):
```
https://discord.com/api/oauth2/authorize?client_id=YOUR_BOT_CLIENT_ID&permissions=2048&scope=bot
```

## Usage

### Running the Bot

```bash
python main.py
```

### Using the Bot

In any Discord channel where the bot is present, simply type:
```
!startmc
```

The bot will:
1. Respond with "🚀 Triggering Minecraft server startup..."
2. Make a POST request to your Coolify deployment API
3. Respond with success or error message

## API Endpoint

The bot calls the following Coolify API endpoint:
```
POST {COOLIFY_URL}/api/v1/projects/{PROJECT_ID}/services/{SERVICE_ID}/deploy
```

With headers:
```
Authorization: Bearer {COOLIFY_API_TOKEN}
Content-Type: application/json
```

## Running on VPS

### Using systemd (Recommended)

1. Create a systemd service file:

```bash
sudo nano /etc/systemd/system/discord-mc-bot.service
```

2. Add the following content:

```ini
[Unit]
Description=Discord Minecraft Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/discord_mc_bot
Environment=PATH=/path/to/venv/bin
ExecStart=/path/to/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

3. Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable discord-mc-bot
sudo systemctl start discord-mc-bot
```

### Using screen/tmux

```bash
screen -S discord-bot
cd /path/to/discord_mc_bot
python main.py
# Press Ctrl+A, then D to detach
```

## Troubleshooting

### Common Issues

1. **Bot not responding**: Check if the bot has "Message Content Intent" enabled
2. **API errors**: Verify your Coolify API token and project/service IDs
3. **Network errors**: Ensure your VPS can reach your Coolify instance

### Logs

Check the console output for error messages. The bot will print:
- Connection status
- Configuration validation
- API request results

## Security Notes

- Keep your `.env` file secure and never commit it to version control
- Use a dedicated Discord bot token for this application
- Consider using a dedicated Coolify API token with minimal permissions

## License

This project is open source and available under the MIT License.