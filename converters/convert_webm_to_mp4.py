import subprocess
from utilities.sanitize_filename import sanitize_filename
from create_logger.logger import LOGGER

logger = LOGGER


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
