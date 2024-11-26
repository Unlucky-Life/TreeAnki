import os

def retrieve_sprites_info(SPRITES_PATH):
    # Initialize the result dictionary
    folder_image_counts = {}
    parent_folder = SPRITES_PATH  # Or directly use the `parent_folder` variable
    
    # Iterate through all items in the parent folder
    for foldername in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, foldername)
        
        # Check if the current item is a directory
        if os.path.isdir(folder_path):
            # Initialize a variable to store the first image type encountered
            first_image_type = None
            image_count = 0
            # Iterate over the files in the folder
            for file in os.listdir(folder_path):
                # Check if the file is an image
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
                    # Increment the image count
                    image_count += 1
                    # Set the first image type encountered (only once)
                    if first_image_type is None:
                        first_image_type = file.split('.')[-1].lower()
            
            # Store the result in the dictionary
            folder_image_counts[foldername] = {
                "image_count": image_count,
                "image_type": first_image_type  # Only the first image type encountered
            }
    
    return folder_image_counts

"""Example:
{'AppleTree': {'image_count': 6, 'image_type': 'png'},
'BirchTree': {'image_count': 6, 'image_type': 'png'},
'CedarTree': {'image_count': 6, 'image_type': 'png'},
'CherryblossomTree': {'image_count': 6, 'image_type': 'png'},
'CrystalbirchTree': {'image_count': 5, 'image_type': 'png'},
'DragonwoodTree': {'image_count': 5, 'image_type': 'png'},
'FirTree': {'image_count': 5, 'image_type': 'png'},
'GoldleafTree': {'image_count': 5, 'image_type': 'png'},
'HazelTree': {'image_count': 5, 'image_type': 'png'},
'MapleTree': {'image_count': 5, 'image_type': 'png'},
'OakTree': {'image_count': 7,'image_type': 'png'},
'WillowTree': {'image_count': 5, 'image_type': 'png'}}
"""