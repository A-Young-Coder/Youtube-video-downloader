"""
This module deletes the raw video and audio files after the final video has been created
"""
import os
from utilities.sanitize_filename import sanitize_filename
from create_logger.logger import LOGGER

logger = LOGGER


def delete_raw_files(save_path, video_title, file_format):
    """
    Delete the raw video and audio files \n
    params: save_path: str: The path to save the downloaded files \n
    params: video_title: str: The title of the video \n
    params: file_format: str: The file format of the video \n
    """

    # Delete the raw video and audio files
    video_path = f"{save_path}/{video_title}_no_audio.mp4"
    audio_path = f"{save_path}/{video_title}.mp3"
    webm_video_path = f"{save_path}/{video_title}.webm"
    glitch_video_path = f"{save_path}/{video_title}.mp4"
    glitch_video_path_sanitized = sanitize_filename(glitch_video_path)
    file_format_video_path = f"{save_path}/{video_title}.{file_format}"

    logger.info("Deleting raw files...")
    if os.path.exists(video_path):
        os.remove(video_path)
    if os.path.exists(audio_path):
        os.remove(audio_path)
    if os.path.exists(webm_video_path):
        os.remove(webm_video_path)
    if os.path.exists(glitch_video_path):
        os.remove(glitch_video_path)
    if os.path.exists(glitch_video_path_sanitized):
        os.remove(glitch_video_path_sanitized)
    if os.path.exists(file_format_video_path):
        os.remove(file_format_video_path)
