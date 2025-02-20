from rembg import remove
from PIL import Image


def remove_background(image_name, image_format):
    input_path = f'D:/Screenshots/Filmora Projects/ESO/{image_name}.{image_format}'
    output_path = f'D:/Screenshots/Filmora Projects/ESO/{image_name}_output.png'
    input_image = Image.open(input_path)
    output = remove(input_image)
    output.save(output_path)


remove_background("para", "png")
