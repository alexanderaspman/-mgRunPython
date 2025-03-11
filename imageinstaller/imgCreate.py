from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
img = Image.new('RGB', (400, 200), (255, 255, 255))

# Add text to the image using a font
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((10, 10), "Hello, world!", font=font)

# Save the image with the Python script embedded
img.save('image.png')