"""
This module is used to download the video from the given URL
"""
from pytubefix.cli import on_progress
from pytubefix import YouTube
from create_logger.logger import LOGGER

logger = LOGGER


def download_video(url, save_path, res, video_title):
    """
    Download the video from the given URL \n
    params: url: str: The URL of the video to download \n
    params: save_path: str: The path to save the downloaded files \n
    params: res: str: The resolution of the video to download \n
    \n
    returns: video_title: str: The title of the video \n
    returns: file_format: str: The file format of the video
    """

    yt = YouTube(url, on_progress_callback=on_progress)

    logger.info(f"Video Title: {video_title}")

    for idx, i in enumerate(yt.streams):
        if i.resolution == res:
            logger.info(idx)
            logger.info(i.resolution)
            break
    logger.info(yt.streams[idx])
    yt.streams[idx].download(output_path=save_path)

    mime_type = yt.streams[idx].mime_type
    file_format = mime_type.split("/")[-1]
    logger.info(f"Downloaded file format: {file_format}")

    return file_format
