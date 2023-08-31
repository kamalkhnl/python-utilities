from PIL import Image
import os

# Set the input directory
input_directory = r'C:\Users\Kamal Khanal\Downloads\textures'

# Create the output directory
output_directory = os.path.join(input_directory, 'converted_png')
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Get a list of all .tga files in the input directory
tga_files = [f for f in os.listdir(input_directory) if f.lower().endswith('.tga')]

# Convert each .tga file to PNG and delete the original
for tga_file in tga_files:
    tga_path = os.path.join(input_directory, tga_file)
    png_file = os.path.splitext(tga_file)[0] + '.png'
    png_path = os.path.join(output_directory, png_file)
    
    # Open the .tga file and save as PNG
    img = Image.open(tga_path)
    img.save(png_path, 'PNG')
    
    # Delete the original .tga file
    os.remove(tga_path)

print("Conversion and cleanup complete. PNG files saved in:", output_directory)
