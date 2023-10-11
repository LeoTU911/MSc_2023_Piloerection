# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 20:00:14 2023

@author: sharp
"""

import os
from PIL import Image, ImageDraw, ImageFont

def get_matching_filenames(dir1, dir2):
    filenames1 = set(os.listdir(dir1))
    filenames2 = set(os.listdir(dir2))
    matching_filenames = filenames1.intersection(filenames2)
    return matching_filenames

def merge_matching_images(dir1, dir2, matching_filenames, merged_images_dir):
    
    os.makedirs(merged_images_dir, exist_ok=True)
    
    # Set font properties for subtitles
    font = ImageFont.truetype("arial.ttf", 20)  # You may need to specify a valid font file path
    text_color = (255, 255, 255)  # black color

    for filename in matching_filenames:
        img1_path = os.path.join(dir1, filename)
        img2_path = os.path.join(dir2, filename)

        img1 = Image.open(img1_path)
        img2 = Image.open(img2_path)

        # Calculate the size for the merged image
        merged_width = img1.width + img2.width
        merged_height = max(img1.height, img2.height)

        # Create a new image with the calculated size
        merged_image = Image.new('RGB', (merged_width, merged_height))

        # Paste the two images side by side
        merged_image.paste(img1, (0, 0))
        merged_image.paste(img2, (img1.width, 0))
        
        # Draw subtitles on the merged image
        draw = ImageDraw.Draw(merged_image)
        subtitle_left = "4"
        subtitle_right = "7"
        draw.text((10, 10), subtitle_left, font=font, fill=text_color)
        draw.text((img1.width + 10, 10), subtitle_right, font=font, fill=text_color)

        # Save the merged image
        merged_image_path = os.path.join(merged_images_dir, f"merged_{filename}")
        merged_image.save(merged_image_path)



# if __name__ == "__main__":
#     dir1 = "path/to/first/set/of/pictures"
#     dir2 = "path/to/second/set/of/pictures"

#     matching_filenames = get_matching_filenames(dir1, dir2)
#     merge_matching_images(dir1, dir2, matching_filenames)


def main(dir1, dir2, merged_images_dir):
    matching_filenames = get_matching_filenames(dir1, dir2)
    merge_matching_images(dir1, dir2, matching_filenames, merged_images_dir)
    

dir1='C:\\Piloerection\\data\\prediction_result\\4model\\output_smoothed_plot\\output_plot'
dir2='C:\\Piloerection\\data\\prediction_result\\0806\\plot'
merged_images_dir='C:\\Piloerection\\data\\prediction_result\\compare'
main(dir1, dir2, merged_images_dir)
