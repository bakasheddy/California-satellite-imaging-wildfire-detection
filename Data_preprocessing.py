import os
import shutil
from PIL import Image

def has_red_pixel(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        pixels = img.getdata()
        for pixel in pixels:
            if pixel == (255, 0, 0):
                return True
        return False
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return False

def move_red_images(source_folder, target_folder='fire'):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    moved_count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.png'):
            file_path = os.path.join(source_folder, filename)
            if has_red_pixel(file_path):
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} to {target_folder}")
                moved_count += 1
                
    print(f"Process complete. Moved {moved_count} images.")


source_directory = './FIRMS_Data'  
move_red_images(source_directory)