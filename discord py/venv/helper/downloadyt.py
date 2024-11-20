import yt_dlp
import os
import asyncio

async def download_youtube_video(url, output_path="downloads"):
    ydl_opts = {
        'format': 'bestvideo[height<=360]+bestaudio/best',  
        'outtmpl': f'{output_path}/%(title)s.%(ext)s', 
        'noplaylist': True,  
    }

    try:
        # Run yt-dlp in a separate thread to avoid blocking the async function
        download_result = await asyncio.to_thread(yt_dlp.YoutubeDL, ydl_opts)
        with download_result as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)

            # Ensure the file was saved correctly
            if os.path.exists(filename):
                return filename 
            else:
                return f"Download failed: {filename} does not exist."
    except yt_dlp.utils.DownloadError as e:
        return f"Download error: {e}"
    except Exception as e:
        return f"Error: {e}"

