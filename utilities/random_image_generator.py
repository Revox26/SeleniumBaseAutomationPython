from urllib import request
from PIL import Image
from io import BytesIO


class ImageHandler:
    def __init__(self, api_url, save_path, new_size=(300, 200)):
        self.api_url = api_url
        self.save_path = save_path
        self.new_size = new_size

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
