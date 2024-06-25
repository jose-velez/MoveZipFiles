import os
import shutil
import zipfile
import re


def compress_and_move_files(source_folder, destination_folder):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Dictionary to group files by {lastName}-{firstName}
    grouped_files = {}

    # Regex pattern to match {firstName}-{lastName}-{intakeId} and flip names
    pattern = re.compile(r'^([^-]+)-\s*([^-]+)')

    # Loop over all files in the source folder
    for filename in os.listdir(source_folder):
        if not filename.endswith('.zip'):  # Ignore already zipped files
            match = pattern.match(filename.strip())
            if match:
                first_name, last_name = match.groups()
                base_name = f"{last_name.strip()}-{first_name.strip()}"
                if base_name not in grouped_files:
                    grouped_files[base_name] = []
                grouped_files[base_name].append(filename)
                print(f"Added {filename} to group {base_name}")
            else:
                print(f"No match for {filename}")

    # Compress each group of files
    for base_name, files in grouped_files.items():
        zip_filename = f"{base_name}.zip"
        zip_filepath = os.path.join(source_folder, zip_filename)

        with zipfile.ZipFile(zip_filepath, 'w') as zipf:
            for file in files:
                file_path = os.path.join(source_folder, file)
                zipf.write(file_path, arcname=file)
                os.remove(file_path)  # Remove the original file after adding to zip

        # Move the zip file to the destination folder
        shutil.move(zip_filepath, os.path.join(destination_folder, zip_filename))
        print(f'Compressed and moved {zip_filename} to {destination_folder}')
        print(f'Count of files for {base_name}: {len(files)}')
        print(f'Files: {files}')


# Usage example
source_folder = '/Users/{user}/{folder}/'
destination_folder = '/Users/{user}/{folder}/'

compress_and_move_files(source_folder, destination_folder)