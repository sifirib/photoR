import PIL
import PIL.Image
import glob
import os
from os import listdir
import time
from tkinter import *


current_path = os.getcwd()
path = os.path.join(current_path, "photos", "")

def resize_img(sizes, directory=False):
    print("Resizing is starting...")
    photos = listdir(path)

    if directory:
        os.chdir(directory)

    height, width = int(sizes[0]), int(sizes[1])
    i = 1
    for image in photos:
        percentage = 100 * i / len(photos)
        print(f"%{percentage}")
        img = PIL.Image.open(image)
        img = img.resize((height, width))
        img.save("resized"+image)
        i += 1
        time.sleep(0.1)
        os.system(f"rm -r {image}")
        time.sleep(0.5)
    print("All of the photos were resized!")

def rotate_img(degree, directory=False):
    print("Rotating is starting...")
    photos = listdir(path)
    degree = int(degree)
    if directory:
        os.chdir(directory)

    i = 1
    for image in photos:
        percentage = 100 * i / len(photos)
        print(f"%{percentage}")
        img = PIL.Image.open(image)        
        img = img.rotate(degree, expand=True)
        img.save("rotated"+image)
        i += 1
        time.sleep(0.1)
      
        time.sleep(0.1)
    print("All of the photos were rotated!")

def compress_img(quality=50, directory=False):
    print("Compressing is starting...")
    photos = listdir(path)
    quality = int(quality)
    if directory:
        os.chdir(directory)

    i = 1
    for image in photos:
        
        percentage = 100 * i / len(photos)
        print(f"%{percentage}")
        img = PIL.Image.open(image)
        img.save("compressed"+image, optimize=True, quality=quality)
        i += 1
        time.sleep(0.1)
        os.system(f"rm -r {image}")
        time.sleep(0.1)
    print("All of the photos were compressed safely!")



root = Tk()

var_resize = IntVar()
var_rotate = IntVar()
var_compress = IntVar()
check_resize = Checkbutton(root, text = "Boyutlandir", variable = var_resize)
check_rotate = Checkbutton(root, text = "Dondur", variable = var_rotate)
check_compress = Checkbutton(root, text = "Sikistir", variable = var_compress)
check_resize.grid()
check_rotate.grid()
check_compress.grid()

is_apply = False
def apply_the_process():
    global is_apply
    is_apply = True
    root.quit()
    

apply_button = Button(root, text = "Uygula", command = apply_the_process)


resize_labels = {"width":Label(root, text = "Genislik: "), "height":Label(root, text = "Yukseklik: ")}
resize_entries = {"width":Entry(root), "height":Entry(root)}
rotate_label = Label(root, text = "Derece: ")
rotate_entry = Entry(root)
compress_label = Label(root, text = "Kalite: ")
compress_entry = Entry(root)

resize_labels["width"].grid()
resize_entries["width"].grid()
resize_labels["height"].grid()
resize_entries["height"].grid()
rotate_label.grid()
rotate_entry.grid()
compress_label.grid()
compress_entry.grid()
apply_button.grid()

root.mainloop()

sizes = [resize_entries["width"].get(), resize_entries["height"].get()]
rotate_degree = rotate_entry.get()
compress_quality = compress_entry.get()

processes = [var_resize.get(), var_rotate.get(), var_compress.get()]

print(processes[1])
if is_apply:
    if processes[0] == 1:
        resize_img(sizes, directory=path)
        time.sleep(2)
    if processes[1] == 1:
        rotate_img(rotate_degree, directory=path)
        time.sleep(2)
    if processes[2] == 1:
        compress_img(compress_quality, directory=path)
        time.sleep(2)

else:
    root.destroy()
    exit()
