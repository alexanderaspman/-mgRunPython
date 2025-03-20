import os
from tkinter import Image

def process_metadata(metadata):
    # Use the metadata to set the desktop background
    
    image_path:str = './image.png',
 
    image_path = f"{os.getcwd()}/{metadata}"
    if os.path.exists(image_path):
        img = Image.open({image_path})
        win32gui.SystemParametersInfo(
            win32gui.SPI_SETDESKWALLPAPER, image_path
        )
    else:
        print("Image not found")

# Example usage:
decoded_string = "your-decoded-string-here"
metadata = process_metadata(decoded_string)