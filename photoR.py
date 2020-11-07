from PIL import Image
import PIL
import glob
import os
from os import listdir
import time
import optparse


current_path = os.getcwd()
path = os.path.join(current_path, "photos", "")

def resizeImg(directory=False):
    print("Resizing is starting...")
    photos = listdir(path)

    if directory:
        os.chdir(directory)

    sizes = input("Give sizes (example: 1920 1080): ")
    height, width = sizes.split()
    height, width = int(height), int(width)
    i = 1
    for image in photos:
        percentage = 100 * i / len(photos)
        print(f"%{percentage}")
        img = Image.open(image)
        img = img.resize((height, width))
        img.save("resized"+image)
        i += 1
        time.sleep(0.1)
        os.system(f"rm -r {image}")
        time.sleep(0.5)
    print("All of the photos were resized!")

def rotateImg(directory=False):
    print("Rotating is starting...")
    photos = listdir(path)


    if directory:
        os.chdir(directory)

    x = int(input("Degree: "))
    i = 1
    for image in photos:
        percentage = 100 * i / len(photos)
        print(f"%{percentage}")
        img = Image.open(image)        
        img = img.rotate(x, expand=True)
        img.save("rotated"+image)
        i += 1
        time.sleep(0.1)
      
        time.sleep(0.1)
    print("All of the photos were rotated!")

def compressImg(directory=False, quality=50):
    print("Compressing is starting...")
    photos = listdir(path)

    if directory:
        os.chdir(directory)

    i = 1
    for image in photos:
        
        percentage = 100 * i / len(photos)
        print(f"%{percentage}")
        img = Image.open(image)
        img.save("compressed"+image, optimize=True, quality=quality)
        i += 1
        time.sleep(0.1)
        os.system(f"rm -r {image}")
        time.sleep(0.1)
    print("All of the photos were compressed safely!")
    
def get_user_input():
    parse_object = optparse.OptionParser()
    return parse_object.parse_args()
    
user_input,arguments = get_user_input()

print(arguments[0])
arg = arguments[0]
len_arg = len(arg)
if 'r' in arg:
    rotateImg(directory=path)
    time.sleep(0.5)
if 's' in arg:
    resizeImg(directory=path)
    time.sleep(0.5)
if 'c' in arg:
    compressImg(directory=path)
    time.sleep(0.5)



