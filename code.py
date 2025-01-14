import os
import shutil

folder_to_organize = r"C:\Mobile" # the small R is representing a raw path. This usually avoids errors

categories = {
    "Camera Images": {
        "name_patterns": ["img_", "image_", "dsc_"],
        "extensions": [".jpg", ".jpeg", ".raw", ".cr2", ".nef"],
    },
    "Screenshots": {
        "name_patterns": ["screenshot", "screen"],
        "extensions": [".png", ".jpg", ".jpeg"],
    },
    "Videos": {
        "name_patterns": ["video_", "vid_", "movie_"],
        "extensions": [".mp4", ".avi", ".mkv", ".mov"],
    },
    "Others": {
        "name_patterns": [],
        "extensions": [],
    },
}

def matches_name_pattern(file_name, patterns):
    return any(pattern in file_name.lower() for pattern in patterns)

def organize_files(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isdir(file_path):
            continue

        moved = False

        for folder, criteria in categories.items():
            if (
                matches_name_pattern(file, criteria["name_patterns"])
                or file.lower().endswith(tuple(criteria["extensions"]))
            ):
                folder_path = os.path.join(directory, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                moved = True
                break

        if not moved:
            others_path = os.path.join(directory, "Others")
            os.makedirs(others_path, exist_ok=True)
            shutil.move(file_path, os.path.join(others_path, file))

organize_files(folder_to_organize)
print("Files organized successfully!")
