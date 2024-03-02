from PIL import Image, ImageOps
import os
import time

def main():
    frame = getFrame()
    mask = getMask()
    images = getImages()

    convert(frame, mask, images)

def getFrame():
    inpt = input("Name of frame image: ")
    try:
        Image.open(f'.//frames//{inpt}')
        return inpt
    except:
        return getFrame()

def getMask():
    inpt = input("Name of mask image: ")
    try:
        Image.open(f'.//masks//{inpt}')
        return inpt
    except:
        return getMask()

def getImages():
    files = os.listdir(".//images")
    list_of_images = []
    for file in files:
        try:
            image = Image.open(f".//images//{file}")
            list_of_images.append(image)
        except:
            continue
    return list_of_images

def convert(frame, mask, images: list):
    frame = Image.open(f'.//frames//{frame}')
    mask = Image.open(f'.//masks//{mask}').convert("L")
    new_folder = time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    os.mkdir(f".//output//{new_folder}")
    for count, image in enumerate(images):
        output = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)
        output.paste(frame, (0, 0), mask=frame)
        output.save(f'.//output//{new_folder}//image_{count}.png')

if __name__ == "__main__":
    main()