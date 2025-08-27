# Library imports

import os
from pdf2image import convert_from_path

#################################################################################################################################

# Dictionary with paths

dict_paths = {'payments':'G:\Mi unidad\Documentos\Finanzas\Pagos'}

#################################################################################################################################

# Functions

def change_name(directory=str, key=str):
    """
    Function to change the name of a file in the payments directory.

    Arguments:
        directory (str): The current name of the file to be changed.
        key (str): The key corresponding to the directory in dict_paths.
    
    Returns:
        None
    """

    print(f"Current directory: {directory}")

    # List all files in the specified directory
    dirs = os.listdir(os.path.join(directory, key))
    print(f"Directory to change names: {os.path.join(directory, key)}")
    print(f"Count of files in directory: {len(dirs)} \nFirst 5 files: {dirs[:5]}")

    # Iterate positions and change names
    for file in range(len(dirs)):
        # save extension
        ext = dirs[file].split(".")[-1]
        # Separating by . or -
        separar = dirs[file].split(".")[0].split("-")
        new_name = f"{separar[2]}{separar[1]}{separar[0]}.{ext}"
        # print(f"\nOld name: {dirs[file]} \nNew name: {new_name}")
        # Rename the file
        os.rename(os.path.join(directory, key, dirs[file]), os.path.join(directory, key, new_name))

def pdf_to_image(pdf_path, num_pages=None):
    """
    Function to convert PDF to images with png format and delete the original PDF file.

    Args:
        pdf_path (str): Path to the PDF file
        num_pages (int, optional): Number of pages to convert. If None, convert all pages. Defaults to None.

    Returns:
        list: List of image file paths
    """

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # If num_pages is specified, limit the number of pages to convert
    if num_pages is not None:
        images = images[:num_pages]

    for i, image in enumerate(images):
        if len(images) > 1:
            image_path = f"{os.path.splitext(pdf_path)[0]}_page_{i + 1}.png"
        else:
            image_path = f"{os.path.splitext(pdf_path)[0]}.png"
        print(f"Saving image: {image_path}")
        image.save(image_path, 'PNG')

    # Delete the original PDF file
    os.remove(pdf_path)