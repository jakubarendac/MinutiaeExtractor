import glob
import os
import cv2
import re
import numpy as np
import matplotlib.pyplot as plt

images = '/home/jakub/projects/minutiae-extractor/ClassifyNet/inputData/mnt_images/'
minutiae = '/home/jakub/projects/minutiae-extractor/ClassifyNet/inputData/mnt_results/'

# Regex
MNT_FILE_REGEX = r"(?!.*/)(.*)(?=.png)"

def readMinutiaePoints(imageName):
    imageNameRegex = re.search(MNT_FILE_REGEX, imageName).group()
    file = open(minutiae + imageNameRegex + '.mnt', "a")
    print(file)

def readMinutiaeImages(imageFormat = 'png'):
    for imageName in glob.glob(os.path.join(images, '*.' + imageFormat)):
        img = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)
        cv2.imshow('image', img)
        cv2.waitKey()
        readMinutiaePoints(imageName)
