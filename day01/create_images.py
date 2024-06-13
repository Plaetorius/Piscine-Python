from PIL import Image

# Create a 9x9 image with a single color (red) for JPG
image_jpg = Image.new("RGB", (9, 9), "red")
image_jpg.save("test_image.jpg", "JPEG")

# Create a 9x9 image with a single color (blue) for JPEG
image_jpeg = Image.new("RGB", (9, 9), "blue")
image_jpeg.save("test_image.jpeg", "JPEG")
