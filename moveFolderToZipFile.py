import os
import shutil


def move_zip_files(source_folder, destination_folder):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Loop over all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith('.zip'):
            # Get the full path to the source file
            source_file = os.path.join(source_folder, filename)

            # Get the name of the folder to create (without the .zip extension)
            folder_name = filename.rsplit('.', 1)[0]
            target_folder = os.path.join(destination_folder, folder_name)

            # Create the target folder
            os.makedirs(target_folder, exist_ok=True)

            # Move the zip file to the target folder
            shutil.move(source_file, os.path.join(target_folder, filename))
            print(f'Moved {filename} to {target_folder}')


# Usage example
source_folder = '/Users/{user}/{folder}/'
destination_folder = '/Users/{user}/{folder}/'

move_zip_files(source_folder, destination_folder)