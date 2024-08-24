"""
This script downloads a video or audio from a given URL
# Date: 16 August 2024
# Author: Atharva Rusia
"""

import yt_dlp as youtube_dl

SAVE_PATH = "/Users/atharva/Downloads"
URL = "https://www.youtube.com/watch?v=3kuLPz65uUU"


def download(url, download_type="video"):
    """
    Download the video or audio from the given URL
    params: url: str: The URL of the video to download
    params: type: str: The type of download (audio or video)
    """

    def progress_hook(d):
        if d['status'] == 'downloading':
            print(f"Downloading: {d['_percent_str']} complete")
        elif d['status'] == 'finished':
            print("Download complete, now converting...")

    def download_video(url):
        """
        Download the video with audio from the given URL
        params: url: str: The URL of the video to download
        """

        ydl_opts = {
            "format": "bestvideo+bestaudio",  # Ensure both best video and best audio are selected
            "outtmpl": f"{SAVE_PATH}/%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",  # Convert video format
                    "preferedformat": "mp4",  # Convert to mp4 if necessary
                },
                {"key": "FFmpegEmbedSubtitle"},  # Embed subtitles if available
            ],
            # "postprocessor_args": [
            #     "-c:v",
            #     "h264_videotoolbox",  # Use hardware-accelerated encoding on M1
            #     "-c:a",
            #     "aac",  # Use AAC audio codec
            # ],
            "progress_hooks": [progress_hook],  # Show download progress
            "external_downloader": "aria2c",  # Use aria2c for faster downloads
            "external_downloader_args": [
                "-x",
                "16",
                "-k",
                "1M",
            ],  # Use 16 connections and 1M chunk size
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def download_audio(url):
        """
        Download the audio from the given URL
        params: url: str: The URL of the video to download
        """

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{SAVE_PATH}/%(title)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "external_downloader": "aria2c",  # Use aria2c for faster downloads
            "external_downloader_args": [
                "-x",
                "16",
                "-k",
                "1M",
            ],  # Use 16 connections and 1M chunk size
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    if (
        download_type.lower() == "audio"
        or download_type.lower() == "a"
        or download_type.lower() == "mp3"
        or download_type.lower() == "aud"
    ):
        download_audio(url)
    elif (
        download_type.lower() == "video"
        or download_type.lower() == "v"
        or download_type.lower() == "mp4"
        or download_type.lower() == "vid"
    ):
        download_video(url)
    else:
        print("Invalid type. Please enter either 'audio' or 'video'")


download(URL, "video")
