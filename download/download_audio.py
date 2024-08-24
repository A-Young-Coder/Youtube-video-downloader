import yt_dlp as youtube_dl
import logging
import os

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Ensure the logs directory exists
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Create a file handler
log_file = os.path.join(log_dir, "application.log")
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)

# Create a formatter and set it for the file handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


def download_audio(url, save_path, video_title):
    """
    Download the audio from the given URL \n
    params: url: str: The URL of the video to download \n
    params: save_path: str: The path to save the downloaded files
    """

    logger.debug(f"Downloading audio of url: {url}...")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{save_path}/{video_title}.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
        "external_downloader": "aria2c",  # Use aria2c for faster downloads
        "external_downloader_args": [
            "-x",
            "16",
            "-k",
            "1M",
        ],  # Use 16 connections and 1M chunk size
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
