from pytubefix.cli import on_progress
from pytubefix import YouTube
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


def download_video(url, save_path, res):
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

    video_title = yt.title
    logger.info(f"Video Title: {video_title}")

    for idx, i in enumerate(yt.streams):
        if i.resolution == res:
            print(idx)
            print(i.resolution)
            break
    print(yt.streams[idx])
    yt.streams[idx].download(output_path=save_path)

    mime_type = yt.streams[idx].mime_type
    file_format = mime_type.split("/")[-1]
    logger.info(f"Downloaded file format: {file_format}")

    return video_title, file_format
