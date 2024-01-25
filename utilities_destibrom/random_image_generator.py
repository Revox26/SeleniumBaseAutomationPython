import os
from urllib import request
from PIL import Image, ImageOps
from io import BytesIO


class ImageHandler:
    def __init__(self, api_url, save_path, icon_size=(150, 150), new_size=(300, 200), target_size_kb=30):
        self.api_url = api_url
        self.save_path = save_path
        self.new_size = new_size
        self.icon_size = icon_size
        self.target_size_kb = target_size_kb

    def download_and_resize_image(self):
        # API call to fetch image data
        response = request.urlopen(self.api_url)
        image_data = response.read()

        # Save the original image
        with open(self.save_path + "//original_image.png", "wb") as image_file:
            image_file.write(image_data)

        # Open the image using Pillow
        img = Image.open(BytesIO(image_data))

        # Resize the image
        resized_img = img.resize(self.new_size)

        # Save the resized image
        resized_img.save(self.save_path + "//resized_image.png")

    def download_and_resize_icon(self):
        # API call to fetch image data
        response = request.urlopen(self.api_url)
        image_data = response.read()

        # Save the original image
        original_path = os.path.join(self.save_path, "original_icons.png")
        with open(original_path, "wb") as image_file:
            image_file.write(image_data)

        # Open the image using Pillow
        img = Image.open(BytesIO(image_data))

        # Resize the first image
        resized_img1 = img.resize(self.icon_size)

        # Save the first resized image in JPEG format with reduced quality
        resized_path1 = os.path.join(self.save_path, "resized_icons.jpg")
        resized_img1.save(resized_path1, 'JPEG', quality=85)  # Adjust quality as needed

        # Check and compress until the file size is within the target limit for the first image
        while os.path.getsize(resized_path1) > self.target_size_kb * 1024:
            resized_img1.save(resized_path1, 'JPEG', quality=resized_img1.info['quality'] - 5)

        # Invert colors for the second image
        inverted_img = ImageOps.invert(resized_img1)

        # Save the second resized image in JPEG format with reduced quality
        resized_path2 = os.path.join(self.save_path, "resized_icons2.jpg")
        inverted_img.save(resized_path2, 'JPEG', quality=85)  # Adjust quality as needed

        # Check and compress until the file size is within the target limit for the second image
        while os.path.getsize(resized_path2) > self.target_size_kb * 1024:
            inverted_img.save(resized_path2, 'JPEG', quality=inverted_img.info['quality'] - 5)
