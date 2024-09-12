"""
This module contains the function to create a ZIP file containing the output file
"""
import os
import zipfile
from create_logger.logger import LOGGER

logger = LOGGER


def zip_output_files(save_path, video_title):
    """
    Create a ZIP file containing the output file \n
    params: save_path: str: The path where the output file is saved \n
    params: video_title: str: The title of the video \n
    returns: str: The path to the created ZIP file
    """
    zip_filename = os.path.join(save_path, f"{video_title}.zip")
    video_filename = os.path.join(f"{save_path}/{video_title}_merged.mp4")

    logger.info(f"Creating ZIP file: {zip_filename}")
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        zipf.write(video_filename, os.path.basename(video_filename))

    return zip_filename
