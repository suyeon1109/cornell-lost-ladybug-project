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

def find_folder_with_least_images(folder_list):
    min_image_count = float('inf')
    min_image_folder = None

    for folder in folder_list:
        image_count = count_images_in_folder(folder)
        if image_count < min_image_count:
            min_image_count = image_count
            min_image_folder = folder

    return min_image_folder, min_image_count

def balance_image_counts(folder_list, target_count):
    for folder in folder_list:
        image_count = count_images_in_folder(folder)
        if image_count > target_count:
            images_to_remove = image_count - target_count
            images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
            for i in range(images_to_remove):
                os.remove(os.path.join(folder, images[i]))

directory_to_search = 'cornell-lost-ladybug-project/AI image'
threshold_image_count = 100

folders_with_many_images = find_folders_with_many_images(directory_to_search, threshold_image_count)

if folders_with_many_images:
    min_image_folder, min_image_count = find_folder_with_least_images(folders_with_many_images)
    print(f"Folder with the least images among folders with more than {threshold_image_count} images:")
    print("Folder:", min_image_folder)
    print("Image Count:", min_image_count)

    balance_image_counts(folders_with_many_images, min_image_count)
    print("Image counts balanced.")
else:
    print("No folders found with more than", threshold_image_count, "images.")