from PIL import Image
from colorim import *
import sys
import shutil

result = ""

if len(sys.argv) == 1:
    print(Color.red("Drag an image into the program first."))
elif len(sys.argv) > 2:
    print(Color.red("Too many files, only one image can be uploaded at a time."))
else:
    path = sys.argv[1]
    try:
        counter = 0
        size = shutil.get_terminal_size()
        width = shutil.get_terminal_size().columns
        image = Image.open(path)
        new_width = width
        aspect_ratio = image.height / image.width
        new_height = int(new_width * aspect_ratio * 0.55)
        image = image.resize((new_width, new_height))
        image_width = image.width
        print("Image successfully loaded.")
        ascii_chars = ":/;?%+=~.#@*_-+|&$[]}){(!"
        image = image.convert("L")
        pixels = list(image.getdata())

        for pixel in pixels:
            pixel = pixel * len(ascii_chars) // 256
            ascii_char = ascii_chars[pixel]
            result += ascii_char
            counter +=1
            if counter == image_width:
                result += "\n"
                counter = 0
        print(result)
        with open("result.txt", "w") as file:
            file.write(result)
        print(Color.light_yellow("Image successfully saved in result.txt."))

    except IOError:
        print("Could not load image.")
input("Press Enter to continue...")