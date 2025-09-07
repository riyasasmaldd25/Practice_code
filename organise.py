import os
import shutil

# Path of the Desktop folder
desktop_path = os.path.expanduser("~/Desktop")
print('Desktop-Path: ', desktop_path)

# Dictionary containing folder names and their file extensions
folders = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".doc", ".docx", ".pdf", ".txt", ".rtf", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

# Create subfolders if they don’t exist
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files into the right folders
for filename in os.listdir(desktop_path):
    original_file_path = os.path.join(desktop_path, filename)
    if os.path.isfile(original_file_path):
        for folder_name, extensions in folders.items():
            for extension in extensions:
                if filename.endswith(extension):
                    destination_folder = os.path.join(desktop_path,folder_name)
                    print(origina_file_path,destination_folder)
                    #shutil.move(originsl_file_path,destination_folder)



