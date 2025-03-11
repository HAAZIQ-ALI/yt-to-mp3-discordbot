import discord
from discord.ext import commands
import yt_dlp
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Bot Name: Waguri
intents = discord.Intents.default()
intents.message_content = True

Waguri = commands.Bot(command_prefix="!", intents=intents)

# YT-DLP options with correct FFmpeg path
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'ffmpeg_location': '/nix/store/3zc5jbvqzrn8zmva4fx5p0nh4yy03wk4-ffmpeg-6.1.1-bin/bin/ffmpeg',  # Updated FFmpeg path
    'outtmpl': 'downloads/%(title)s.%(ext)s'
}


@Waguri.event
async def on_ready():
    print(f"Logged in as {Waguri.user}")

@Waguri.command()
async def ping(ctx):
    await ctx.send("hey!")

@Waguri.command()
async def download(ctx, url: str):
    """Downloads a YouTube video and converts it to MP3"""
    await ctx.send("Downloading... Please wait.")

    # Create downloads directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'unknown')
            file_path = f"downloads/{title}.mp3"

            # Send the file
            if os.path.exists(file_path):
                await ctx.send(f"Download complete! Sending: {title}")
                await ctx.send(file=discord.File(file_path))
            else:
                await ctx.send("Something went wrong with the download.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

Waguri.run(TOKEN)