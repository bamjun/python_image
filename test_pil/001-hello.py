from PIL import Image, ImageDraw, ImageFont, ImageSequence

# Define text and parameters
text = "HELLO"
font_size = 100
font = ImageFont.load_default()  # Use default PIL font
frames = 36  # Number of frames in the GIF
width, height = 200, 200  # Size of the image

# Create each frame
images = []
for i in range(frames):
    # Create a new image with a transparent background
    image = Image.new("RGBA", (width, height), "white")
    draw = ImageDraw.Draw(image)
    
    # Calculate rotation angle
    angle = i * (360 / frames)
    
    # Create rotated text
    text_image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_image)
    text_bbox = text_draw.textbbox((0, 0), text, font=font)

    # 글자 회전 모양이 틀려짐
    # 가운데 공간을 두고 회전
    # text_position = (111, 111)  
    # 제자리에서 회전
    text_position = ((width - (text_bbox[2] - text_bbox[0])) // 2, (height - (text_bbox[3] - text_bbox[1])) // 2)
    text_draw.text(text_position, text, font=font, fill="black")
    rotated_text = text_image.rotate(angle, resample=Image.Resampling.BICUBIC)
    
    # Combine the background with the rotated text
    image = Image.alpha_composite(image, rotated_text)
    images.append(image)

# Save as a GIF
output_path_text = "rotating_text.gif"
images[0].save(output_path_text, save_all=True, append_images=images[1:], loop=0, duration=100)

print(f"Saved GIF: {output_path_text}")
