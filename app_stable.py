"""
Contains the Flask application that will listen for incoming requests
"""

import os
import zipfile
from flask import Flask, request, jsonify, send_file
from constants.constants import *
from create_logger.logger import create_logger
from main import main

create_logger()

app = Flask(__name__)

@app.route("/download", methods=["POST"])
def download_videos():
    """
    Download videos from the provided URLs and resolutions
    """
    data = request.json
    save_path = SAVE_PATH
    urls = data.get("urls")

    # Check if the list of URLs is provided
    if not urls or not isinstance(urls, list):
        return (
            jsonify({"error": "A list of dictionaries with 'url' and 'resolution' is required"}),
            400,
        )

    results = []
    zip_files = []

    # Process each URL
    for item in urls:
        url = item.get("url")
        resolution = item.get("resolution")

        # Check if the URL and resolution are provided
        if not url or not resolution:
            results.append({"url": url, "status": "Error: 'url' and 'resolution' are required"})
            continue

        # Download and process the video
        try:
            zip_filename = main(url, save_path, resolution)
            zip_files.append(zip_filename)
            results.append({"url": url, "status": "Download and processing completed"})
        except Exception as e: # Catch all exceptions
            results.append({"url": url, "status": f"Error: {str(e)}"})

    # Returning only one zip file
    if len(zip_files) == 1:
        return send_file(
            zip_files[0],
            as_attachment=True,
            download_name=os.path.basename(zip_files[0]),
        )
    else:
        # If there are multiple zip files, create a combined zip file
        combined_zip_filename = os.path.join(save_path, "combined_videos.zip")
        with zipfile.ZipFile(combined_zip_filename, 'w') as combined_zip:
            for zip_file in zip_files:
                combined_zip.write(zip_file, os.path.basename(zip_file))

    # Return the combined zip file
    return send_file(
        combined_zip_filename,
        as_attachment=True,
        download_name="combined_videos.zip",
        mimetype="application/zip",
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
