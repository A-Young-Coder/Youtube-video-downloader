import os
import shutil

def file_mover(filename):
    def mover(source_dir, dest_dir, filename):
        # Ensure the destination directory exists
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # List all files in the source directory
        files = os.listdir(source_dir)

        for file_name in files:
            # Check if the file name contains the specified filename
            if file_name == filename:
                # Construct full file path
                source_file = os.path.join(source_dir, file_name)
                dest_file = os.path.join(dest_dir, file_name)

                # Move the file
                shutil.move(source_file, dest_file)
                print(f"Moved: {source_file} to {dest_file}")

    if __name__ == "__main__":
        # Define source and destination directories
        source_dir = "/Users/atharva/Downloads/"
        dest_dir = "/Users/atharva/Documents/Youtube-video-downloader/templates/upload/"

        # Move files from source to destination
        mover(source_dir, dest_dir, filename=filename)