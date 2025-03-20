import os
import win32gui
from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background

img = Image.new('RGB', (400, 200), (205, 255, 255))

# Add text to the image using a font

draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((10, 10), "Hello, world!", font=font, fill=(0, 0, 0))
draw.metadata = {
    'author': 'Alice',
    'description': '110000011100001111101011100100011101000111001011110111101111101110110110101110011010101100101011101101110101111100000111000011111010111001000111010001110010111101111011111011101101101011100110101011001010110110111010111010110110110110111010110110',
}
# Save the image
img.save('image.png')

def process_metadata(metadata):
    # Use the metadata to set the desktop background

    image_path = 'image.png'

    if os.path.exists(image_path):
        win32gui.SystemParametersInfo(
            win32gui.SPI_SETDESKWALLPAPER, image_path
        )
    else:
        print("Image not found")

# Example usage:
decoded_string = "your-decoded-string-here"
process_metadata(decoded_string)