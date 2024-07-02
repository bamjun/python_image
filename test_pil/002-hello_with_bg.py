from PIL import Image, ImageDraw, ImageFont, ImageSequence

# Load the background image
background_path = "test_pil/002-sizefit.png"  # Adjust the path to where your image is located
background = Image.open(background_path).convert("RGBA")

# Define text and parameters
text = "HELLO"
font_size = 100  # Increase the font size
frames = 36  # Number of frames in the GIF
width, height = background.size  # Use the background size

# Load a TTF font file. Adjust the path to where your TTF file is located.
font_path = "C:\\Windows\\Fonts\\bahnschrift.ttf"  # Example path for a common font on Windows
font = ImageFont.truetype(font_path, font_size)

# Create each frame
images = []
for i in range(frames):
    # Create a new image with the background
    image = background.copy()
    draw = ImageDraw.Draw(image)
    
    # Calculate rotation angle
    angle = i * (360 / frames)
    
    # Create rotated text
    text_image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_image)
    text_bbox = text_draw.textbbox((0, 0), text, font=font)
    text_position = ((width - (text_bbox[2] - text_bbox[0])) // 2, (height - (text_bbox[3] - text_bbox[1])) // 2)
    text_draw.text(text_position, text, font=font, fill="#ff99ff")
    rotated_text = text_image.rotate(angle, resample=Image.Resampling.BICUBIC)
    
    # Combine the background with the rotated text
    image = Image.alpha_composite(image, rotated_text)
    images.append(image)

# Save as a GIF
output_path_text = "rotating_text_with_background.gif"
images[0].save(output_path_text, save_all=True, append_images=images[1:], loop=0, duration=100)

print(f"Saved GIF: {output_path_text}")
