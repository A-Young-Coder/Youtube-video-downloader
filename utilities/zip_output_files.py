import os
import zipfile
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
