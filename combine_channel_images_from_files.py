import os
from PIL import Image
import glob

def extract_channel(image_path, channel_index):
    img = Image.open(image_path)
    channel = img.split()[channel_index]
    return channel

def combine_channels(red_file, green_file, blue_file, output_file):
    # Extract channels from each file
    green_channel = extract_channel(green_file, 1)  # Green channel has index 1
    blue_channel = extract_channel(blue_file, 2)    # Blue channel has index 2
    red_channel = extract_channel(red_file, 0)      # Red channel has index 0

    # Create a new image with the same dimensions
    new_img = Image.merge("RGB", (red_channel, green_channel, blue_channel))

    # Save the new image
    new_img.save(output_file)
    print(f"Channels combined and saved to {output_file}")

if __name__ == "__main__":
    input_folder = "C:\\Users\\Kamal Khanal\\Desktop\\Photoshop\\"
    output_file_path = "C:\\Users\\Kamal Khanal\\Desktop\\Photoshop\\output_combined.jpg"

    # Search for files with the specified suffixes in the input folder
    metallic_file = glob.glob(os.path.join(input_folder, "*_metallic.jpg"))[0]
    ao_file = glob.glob(os.path.join(input_folder, "*_AO.jpg"))[0]
    roughness_file = glob.glob(os.path.join(input_folder, "*_Roughness.jpg"))[0]

    combine_channels(roughness_file, metallic_file, ao_file, output_file_path)
