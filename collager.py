from PIL import Image
import os
import math

def merge_images_to_collage(folder_path, output_directory, grid_size=None):
    """
    Merge images from a folder into a single collage.
    :param folder_path: Path to the folder containing images.
    :param output_file: Path for the output collage image.
    :param grid_size: Tuple of (rows, cols) for the grid. Auto-calculated if None.
    """
    # Load all image file paths from the folder
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if (len(image_files) == 0):
        print("No images loaded")
        return
    # Open the output file for writing

    height_list = []
    overall_height = 0
    max_width = 0
    
    output_file = output_directory + "data.csv"

    with open(output_file, 'w') as file:
        # Iterate through each file in the folder
        for image_name in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image_name)
            # Check if the file is an image
            if os.path.isfile(image_path) and image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                try:
                    # Open the image and get dimensions
                    with Image.open(image_path) as img:
                        width, height = img.size
                        file.write(f"{width},{height},{image_name}\n")
                        overall_height += height
                        max_width = max(max_width, width)
                        height_list.append(height)
                except Exception as e:
                    print(f"Could not process {image_name}: {e}")
        print(f"Image dimensions written to '{output_file}'.")

    # Create a blank canvas for the collage
    collage_width = max_width
    collage_height = overall_height
    collage = Image.new('RGB', (collage_width, collage_height))

    images = [Image.open(img) for img in image_files]
    y_offset = 0
    for index, img in enumerate(images):
        collage.paste(img, (0, y_offset))
        y_offset += height_list[index]

    collage_output = output_directory + "collage.png"
    collage.save(collage_output)
    print(f"Collage saved as {collage_output}")


if __name__ == "__main__":
    merge_images_to_collage("Test", "./Output/")