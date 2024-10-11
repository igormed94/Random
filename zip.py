import os
import zipfile
from tqdm import tqdm

def zip_dir_with_strong_compression(folder_path, output_path, exclude_folders=None, max_file_size_mb=100):
    exclude_folders = exclude_folders or []

    # Count the total number of files to track progress
    file_count = sum(len(files) for _, _, files in os.walk(folder_path) if not any(excluded in _ for excluded in exclude_folders))

    with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_LZMA) as zipf:  # Using LZMA for better compression
        with tqdm(total=file_count, unit='file') as progress_bar:
            for root, dirs, files in os.walk(folder_path):
                # Exclude certain folders
                if any(excluded in root for excluded in exclude_folders):
                    continue
                for file in files:
                    file_path = os.path.join(root, file)
                    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                    # Exclude files that are too large
                    if file_size_mb <= max_file_size_mb:
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname)
                    progress_bar.update(1)

# Set the folder you want to compress, the output zip file, and folders to exclude
folder_to_zip = r"C:\Users\igor_\Downloads\Auto_Jobs_Applier_AIHawk-main"
output_zip = r"C:\Users\igor_\Downloads\compressed_project_lzma.zip"
exclude = ['__pycache__', 'venv', 'node_modules', '.git']

# Compress the folder with strong compression (LZMA)
zip_dir_with_strong_compression(folder_to_zip, output_zip, exclude_folders=exclude)
