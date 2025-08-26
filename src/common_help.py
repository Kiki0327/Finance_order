# Library imports

import os

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