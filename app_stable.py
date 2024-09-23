"""
Contains the Flask application that will listen for incoming requests
"""

import os
import zipfile
from flask import Flask, request, jsonify, send_file, send_from_directory, session, render_template
from constants.constants import SAVE_PATH, WIFIHOST, PORT

from create_logger.logger import create_logger
from main import main

create_logger()

app = Flask(__name__)
app.config["SECRET_KEY"] = "myseceretkey"  # Set the secret key for the session
UPLOAD_FOLDER = "./templates/upload"  # Specify the directory to save uploaded files
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/download", methods=["POST", "GET"])
def download(url = "", resolution = "", file_type = ""):
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
        file_type = item.get("file_type")
        # Process the download based on the format

        # Check if the URL and resolution are provided
        if not url or not resolution:
            results.append({"url": url, "status": "Error: 'url' and 'resolution' are required"})
            continue

        # Download and process the video
        try:
            zip_filename = main(url, save_path, resolution, file_type)
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

@app.route("/home", methods=["POST", "GET"])
def home():
    """
    creating home page for website
    """
    url = None
    resolution = None
    file_type = None
    session.clear()
    if request.method == "POST":
        url = request.form.get("url")
        resolution = request.form.get("resolution")
        file_type = request.form.get("file_type")

        # Ensure the variables are not None
        if not url:
            return "URL is required", 400
        if not resolution:
            return "Resolution is required", 400
        if not file_type:
            return "File type is required", 400

    session["url"] = url
    session["resolution"] = resolution
    session["file_type"] = file_type

    return render_template("home.html")


@app.route("/download_web", methods=["POST", "GET"])
def download_web():
    """
    Provides download functionality for the website
    """
    url = request.form.get("url")
    resolution = request.form.get("res")
    file_type = request.form.get("format")
    save_path = SAVE_PATH
    zip_files = []
    results = []

    zip_filename = ""  # Initialize zip_filename

    try:
        zip_filename = main(url, save_path, resolution, file_type)
        # replace Save path with empty string
        zip_filename = zip_filename.replace(SAVE_PATH, "")
        zip_filename = os.path.normpath(zip_filename)
        zip_files.append(zip_filename)
        results.append({"url": url, "status": "Download and processing completed"})
    except Exception as e:  # Catch all exceptions
        results.append({"url": url, "status": f"Error: {str(e)}"})

    return render_template("download.html", filename=zip_filename)


@app.route("/upload/<filename>")
def upload_file(filename):
    """
    Upload the file to the server
    """
    return send_from_directory(
        app.config["UPLOAD_FOLDER"], filename, as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True, host=WIFIHOST, port=PORT)
