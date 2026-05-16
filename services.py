import yt_dlp
import os
import asyncio

class SoundCloudDownloader:
    def __init__(self):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'no_warnings': True,
            'ignoreerrors': True,
        }

    async def get_info(self, url):
        loop = asyncio.get_event_loop()
        with yt_dlp.YoutubeDL({'quiet': True, 'extract_flat': True}) as ydl:
            return await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=False))

    async def download(self, url):
        loop = asyncio.get_event_loop()
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            await loop.run_in_executor(None, lambda: ydl.download([url]))