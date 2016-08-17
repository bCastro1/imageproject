from array import *
from PIL import Image

image = Image.open("church0.jpg")
finalWidth, finalHeight = image.size
newImage = Image.new("RGB", (finalWidth, finalHeight))
cropWidth = finalWidth/30
print("cropWidth: ",cropWidth)

#box = (0,0,300,height)
#picture = image.crop(box)

#newImage.paste(picture,(0,0))

#newImage.save("newImage.jpg")

imageNameList = []

for i in range(0,30):
    imageName = "church"
    imageName+=str(i)
    imageName+=".jpg"
    imageNameList.append(imageName)


cropLocationX = 0
for newCrop in range(0,30):
    imageToCrop = Image.open(imageNameList[newCrop])
    box = (cropLocationX,0,(cropLocationX + cropWidth),finalHeight)
    croppedImage = imageToCrop.crop(box)
    newImage.paste(croppedImage,(cropLocationX,0))
    cropLocationX += cropWidth
    print("cropLocationX: ",cropLocationX)
    
newImage.save("newImage.jpg")
