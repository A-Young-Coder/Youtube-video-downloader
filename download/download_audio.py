import yt_dlp as youtube_dl
import logging
import os
from create_logger.logger import LOGGER

logger = LOGGER


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
