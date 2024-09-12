"""
Master Module to call all the other modules.
"""

from converters.convert_webm_to_mp4 import convert_webm_to_mp4
from converters.merge_video_and_audio import merge_video_audio

from utilities.delete_raw_files import delete_raw_files
from utilities.zip_output_files import zip_output_files
from utilities.get_video_title import get_video_title

from download.download_video import download_video
from download.download_audio import download_audio


def main(url, save_path, res, file_type):
    """
    Combine all the functions to download, convert, and merge the video and audio files.
    Central function to call all the other functions. \n
    params: url: str: The URL of the video to download \n
    params: save_path: str: The path to save the downloaded files \n
    params: res: str: The resolution of the video to download \n

    returns: zip_filename: str: The path to the created ZIP file
    """
    video_title = get_video_title(url)

    if file_type == "video":
        file_format = download_video(url, save_path, res, video_title)

        convert_webm_to_mp4(video_title, save_path, file_format)

        download_audio(url, save_path, video_title)

        merge_video_audio(save_path, video_title)

        delete_raw_files(save_path, video_title, file_format)

    elif file_type == "audio":
        download_audio(url, save_path, video_title)

    zip_filename = zip_output_files(save_path, video_title)

    return zip_filename
