

# Waguri - YouTube to MP3 Discord Bot

## About
Waguri is a Discord bot that allows users to download YouTube videos and convert them to MP3 format. It uses `yt-dlp` for video extraction and conversion. This bot is created by [HAAZIQ-ALI](https://github.com/HAAZIQ-ALI).

## Features
- Download and convert YouTube videos to MP3
- Easy-to-use commands
- High-quality 320kbps audio conversion

## Prerequisites
Before running the bot, ensure you have the following:
- Python installed
- `discord.py` and `yt-dlp` libraries installed
- A Discord bot token
- FFmpeg installed (with the correct path specified in the code)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/HAAZIQ-ALI/Waguri.git
   cd Waguri
   ```
2. Install dependencies:
   ```sh
   pip install discord yt-dlp
   ```
3. Set up your bot token as an environment variable:
   ```sh
   export DISCORD_BOT_TOKEN=your_token_here
   ```
4. Run the bot:
   ```sh
   python bot.py
   ```

## How to Use
1. Add the bot to your Discord server.
2. Use the following commands:
   - `!ping` - The bot responds with "hey!"
   - `!download <YouTube_URL>` - The bot downloads the given YouTube video and converts it to MP3.
3. The MP3 file will be sent back in the Discord chat after processing.

## Notes
- Ensure the `downloads/` directory exists or the bot will create it.
- The bot uses a specific FFmpeg path. Update it if necessary.
- Running the bot requires a valid Discord bot token.

## License
This project is open-source and can be modified and distributed freely.




