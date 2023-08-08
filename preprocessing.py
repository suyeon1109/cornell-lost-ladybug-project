import os
from PIL import Image

def count_images_in_folder(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']  # Add more extensions if needed
    image_count = 0

    for filename in os.listdir(folder_path):
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            image_count += 1

    return image_count

def find_folders_with_many_images(root_path, threshold=100):
    folders_with_many_images = []

    for dirpath, dirnames, filenames in os.walk(root_path):
        if count_images_in_folder(dirpath) > threshold:
            folders_with_many_images.append(dirpath)

    return folders_with_many_images


directory_to_search = 'cornell-lost-ladybug-project/AI image'
threshold_image_count = 100

folders_with_many_images = find_folders_with_many_images(directory_to_search, threshold_image_count)

print(f"Folders with more than {threshold_image_count} images:")
for folder in folders_with_many_images:
    print(folder)