"""
Module to get the title of the video from the URL.
"""

from pytubefix import YouTube
from pytubefix.cli import on_progress
from create_logger.logger import LOGGER

logger = LOGGER

def get_video_title(url):
    yt = YouTube(url, on_progress_callback=on_progress)

    video_title = yt.title
    logger.info(f"Video Title: {video_title}")

    return video_title