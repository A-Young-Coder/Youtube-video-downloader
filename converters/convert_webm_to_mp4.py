import subprocess
from utilities.sanitize_filename import sanitize_filename
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


def convert_webm_to_mp4(video_title, save_path, file_format="webm"):
    """
    Convert the downloaded WebM video to MP4 format \n
    params: video_title: str: The title of the video \n
    params: file_format: str: The file format of the video
    """
    output_path = f"{save_path}/{video_title}_no_audio.mp4"
    video_title = sanitize_filename(video_title)
    input_path = f"{save_path}/{video_title}.{file_format}"

    # Construct the FFmpeg command with libx264 codec
    logger.debug(f"Converting {file_format} to MP4...")
    command = [
        "ffmpeg",
        "-i",
        input_path,
        "-c:v",
        "libx264",
        "-c:a",
        "aac",
        output_path,
    ]
    # Run the command
    subprocess.run(command, check=True)
