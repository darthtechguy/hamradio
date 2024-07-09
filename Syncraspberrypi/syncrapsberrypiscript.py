import os
import shutil
import time

def copy_files_and_dirs(src, dst):
    """Copy files and directories from src to dst."""
    if os.path.isdir(src):
        os.makedirs(dst, exist_ok=True)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            copy_files_and_dirs(s, d)
    else:
        shutil.copy2(src, dst)

def scan_directory(path):
    """Scan the directory and return a set of file paths."""
    files = set()
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            files.add(os.path.join(root, filename))
    return files

# Define the source and destination folders
source_folder = r'R:\\'
destination_folder = r'C:\\Users\\curti\\OneDrive\\Desktop\\SATRecordings\\GOESImages\\goestools-win64-1.0.7\\Saved'

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Set to remember the state of the source folder
previous_state = set()

while True:
    current_state = scan_directory(source_folder)

    # Determine new or changed files
    new_or_changed_files = current_state - previous_state
    for file_path in new_or_changed_files:
        relative_path = os.path.relpath(file_path, source_folder)
        dest_path = os.path.join(destination_folder, relative_path)

        try:
            # Copy the file or directory
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(file_path, dest_path)
            print(f"Successfully copied: {relative_path}")
        except Exception as e:
            print(f"Failed to copy {relative_path}: {e}")

    # Update the previous state
    previous_state = current_state

    # Wait for a bit before checking again
    time.sleep(7200)  # Checks every 2 hours in seconds; adjust as needed
