from array import *
from PIL import Image
import os
import shutil

print "Make sure this file is in the same directory as every picture in the time lapse."
print "This program only accepts .jpg image types."

def main():
    finalImageName = raw_input('Please input final image name: ')
    #final name of image
    
    picturePaths = filenameParse()
    picturePaths.sort()
    
    print 'Would you like to order the time lapse images in chronological order?'
    reversed = raw_input('Type YES or NO: ')
    
    if (reversed == "YES"):
        picturePaths.reverse()
    else:
        print 'Proceeding with chronological order.'

    cropPictures(finalImageName, picturePaths)

    print 'Congratulations! Your time sliced picture is now ready!'
        
    
def filenameParse():
    filePaths = []

    #getting all contents of current folder
    for root, directories, files in os.walk(os.getcwd()):
        for filename in files:
            filepath = os.path.join(root, filename)
            filePaths.append(filepath)

    pictureNames = []
    #looking for only .jpg images 
    for picFileNames in filePaths:
        if picFileNames.endswith(".jpg"):
            pictureNames.append(picFileNames)
            
    return pictureNames

def cropPictures(finalImageName, picturePaths):

    #get initial picture dimensions to create new dimensions
    image = Image.open(picturePaths[0])
    finalWidth, finalHeight = image.size
    newImage = Image.new("RGB", (finalWidth, finalHeight))

    #based on how many pictures, determine how large of a rectangle to crop
    cropWidth = finalWidth / len(picturePaths)

    print 'Starting to construct your new picture. This may take a few minutes.'
    cropLocationX = 0
    #starting at left side, place images across the new blank canvas
    
    for imageIndex in range(0,len(picturePaths)):
        imageToCrop = Image.open(picturePaths[imageIndex])

        #crop rectangle that is the 'cropWidth' size
        box = (cropLocationX, 0,(cropLocationX+cropWidth),finalHeight)
        croppedImage = imageToCrop.crop(box)

        #paste onto new canvas
        newImage.paste(croppedImage,(cropLocationX,0))

        #advance cropLocationX to start where last one finished
        cropLocationX += cropWidth

        #let user know it is still working
        if imageIndex == len(picturePaths)/2:
            print 'Halfway finished constructing your new picture!'

    newImageName = finalImageName+'.jpg'
    newImage.save(newImageName)

    #move newly created image to new directory to not interfere with time lapse photo names
    moveCreatedImageToDirectory(newImage, newImageName)
    
def moveCreatedImageToDirectory(newImage, newImageName):
    
    newDirectoryPathName = os.getcwd()+'/NewImageFolder'

    if not os.path.exists(newDirectoryPathName):
        #new directory not found, create new
        print 'Creating new folder titled newImageFolder, and placing image inside of it.'
        os.makedirs(newDirectoryPathName)
        
        #finding current location of newly created image
        newImagePath = os.getcwd()+'/'+newImageName
        
        #moving new image to new directory
        shutil.move(newImagePath, newDirectoryPathName)

    else:
        #finding current location of newly created image
        newImagePath = os.getcwd()+'/'+newImageName
        
        #moving new image to new directory
        shutil.move(newImagePath, newDirectoryPathName)

main()
