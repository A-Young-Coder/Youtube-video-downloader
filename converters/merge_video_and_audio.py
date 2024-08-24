import os
import subprocess
import logging
from create_logger.logger import LOGGER

logger = LOGGER


def merge_video_audio(save_path, video_title):
    """
    Merge the video and audio files \n
    params: save_path: str: The path to save the downloaded files \n
    params: video_title: str: The title of the video
    """

    # Construct the FFmpeg command to merge video and audio
    video_path = f"{save_path}/{video_title}_no_audio.mp4"
    audio_path = f"{save_path}/{video_title}.mp3"
    output_path = f"{save_path}/{video_title}_merged.mp4"

    # Check if input files exist
    if not os.path.exists(video_path):
        logger.info(f"Video file not found: {video_path}")
        return
    if not os.path.exists(audio_path):
        logger.info(f"Audio file not found: {audio_path}")
        return

    # Construct the FFmpeg command to merge video and audio
    logger.debug(f"Merging video and audio files...")
    command = [
        "ffmpeg",
        "-i",
        video_path,
        "-i",
        audio_path,
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        output_path,
    ]
    # Run the command
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"FFmpeg command failed with error: {e}")
