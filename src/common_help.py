import os

dict_paths = {'payments':'G:/Mi unidad/Documentos/Finanzas/Pagos/'}

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
    print(f"Count of files in directory: {len(dirs)} \nFirst 5 files: {dirs[:5]}")