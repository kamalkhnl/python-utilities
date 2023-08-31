from PIL import Image
import os
import shutil

def split_and_save_channels(image_path, target_folder):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Split the image into separate channels
    r, g, b = image.split()

    # Create a list of channel images and their corresponding names
    channel_images = [
        (r, "Roughness"),
        (g, "Metallic"),
        (b, "AO")
    ]

    # Get the directory path and filename
    image_dir, image_filename = os.path.split(image_path)
    image_name, _ = os.path.splitext(image_filename)

    # Create the "converted" folder if it doesn't exist
    converted_folder = os.path.join(target_folder, "converted")
    os.makedirs(converted_folder, exist_ok=True)

    # Save each channel as a separate file in the "converted" folder
    for channel, channel_name in channel_images:
        channel_image = Image.new("L", image.size)
        channel_image.putdata(channel.getdata())
        channel_path = os.path.join(converted_folder, f"{image_name}_{channel_name}.png")
        channel_image.save(channel_path)

    print(f"Channels split and saved for {image_filename}.")

    # Delete the original image file
    os.remove(image_path)
    print("Original image file deleted.")

def find_image_files(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Find image files (PNG or JPG)
    image_files = []
    for file in files:
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".tga")):
            image_files.append(os.path.join(directory, file))

    return image_files

if __name__ == "__main__":
    target_folder = r"C:\Users\Kamal Khanal\Desktop\RMA Splitter"
    image_files = find_image_files(target_folder)

    if image_files:
        for image_path in image_files:
            split_and_save_channels(image_path, target_folder)
    else:
        print("No image files found in the specified folder.")
