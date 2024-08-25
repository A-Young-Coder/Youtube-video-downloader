import os
import zipfile
from flask import Flask, request, jsonify, send_file
from main import main

app = Flask(__name__)

@app.route("/download", methods=["POST"])
def download_videos():
    try:
        data = request.json
        app.logger.info(f"Received data: {data}")
        if not data or not isinstance(data, list):
            return jsonify({"error": "Invalid JSON payload"}), 400

        zip_files = []
        results = []
        save_path = "/Users/atharva/Downloads"  # Assuming this is the path where files are saved

        for item in data:
            url = item.get("url")
            resolution = item.get("resolution")
            try:
                zip_filename = main(url, save_path, resolution)
                zip_files.append(zip_filename)
                results.append(
                    {"url": url, "status": "Download and processing completed"}
                )
            except Exception as e:
                results.append({"url": url, "status": f"Error: {str(e)}"})

        if len(zip_files) == 1:
            return send_file(
                zip_files[0],
                as_attachment=True,
                download_name=os.path.basename(zip_files[0]),
            )
        else:
            combined_zip_filename = os.path.join(save_path, "combined_videos.zip")
            with zipfile.ZipFile(combined_zip_filename, "w") as combined_zip:
                for zip_file in zip_files:
                    combined_zip.write(zip_file, os.path.basename(zip_file))

            return send_file(
                combined_zip_filename,
                as_attachment=True,
                download_name="combined_videos.zip",
                mimetype="application/zip",
            )
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    PORT = 5000
    app.run(debug=True, host="0.0.0.0", port=PORT)
