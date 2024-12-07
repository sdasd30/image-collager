from PIL import Image
import os
import csv

def split_collage_to_images(collage_path, metadata_path, output_directory):
    """
    Split a collage into separate images using metadata.
    :param collage_path: Path to the collage image.
    :param metadata_path: Path to the CSV file containing image metadata.
    :param output_directory: Directory where individual images will be saved.
    """
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)
    
    # Open the collage image
    try:
        collage = Image.open(collage_path)
    except Exception as e:
        print(f"Error opening collage image: {e}")
        return
    
    # Read metadata from the CSV file
    images_metadata = []
    try:
        with open(metadata_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    print(f"Invalid row in metadata: {row}")
                    continue
                width, height, name = int(row[0]), int(row[1]), row[2]
                images_metadata.append((width, height, name))
    except Exception as e:
        print(f"Error reading metadata: {e}")
        return
    
    # Split the collage into separate images
    y_offset = 0
    for index, (width, height, name) in enumerate(images_metadata):
        try:
            # Crop the current image from the collage
            image_crop = collage.crop((0, y_offset, width, y_offset + height))
            # Save the cropped image
            output_path = os.path.join(output_directory, name)
            image_crop.save(output_path)
            print(f"Saved: {output_path}")
            y_offset += height
        except Exception as e:
            print(f"Error processing image {name}: {e}")
            continue
    
    print("Splitting complete!")

if __name__ == "__main__":
    split_collage_to_images(
        collage_path="./Output/collage.png", 
        metadata_path="./Output/data.csv", 
        output_directory="./Output/Images/"
    )
