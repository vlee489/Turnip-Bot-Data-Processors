"""
This script is used to save images as PNG for the pet command
and save it with a number ID
"""

from PIL import Image
import os

folder = "InFolder"
output = "OutFolder"
counter = 0

for filename in os.listdir(folder):
    im = Image.open("{}/{}".format(folder, filename))
    im.save("{}/{}.png".format(output, counter))
    print("Saves {} as {}.png".format(filename, counter))
    counter = counter + 1
    im.close()
