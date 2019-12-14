import glob
import os
import cv2
import re
import matplotlib

matplotlib.use('TkAgg')

import numpy as np
import matplotlib.pyplot as plt

images = '/home/jakub/projects/minutiae-extractor/ClassifyNet/inputData/mnt_images/'
minutiae = '/home/jakub/projects/minutiae-extractor/ClassifyNet/inputData/mnt_results/'

# Regex
MNT_FILE_REGEX = r"(?!.*/)(.*)(?=.png)"

class MinutiaeData:
    def __init__(self, xPosition, yPosition, theta):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.theta = theta


def getMinutiaeCount(data):
    splittedData = data.split()
    
    return int(splittedData[0])

def getMinutiaePoints(data):
    minutiaeDataList = []

    for rawMinutiaeData in data:
        minutiaeData = rawMinutiaeData.split()

        yPosition = int(minutiaeData[0])
        xPosition = int(minutiaeData[1])
        theta = float(minutiaeData[2])

        data = MinutiaeData(xPosition,yPosition, theta)
        minutiaeDataList.append(data)

    return minutiaeDataList


def readMinutiaeData(imageName):
    imageNameRegex = re.search(MNT_FILE_REGEX, imageName).group()
    file = open(minutiae + imageNameRegex + '.mnt', "rb")
    rawData = file.readlines()[1:]

    minutiaeCount = getMinutiaeCount(rawData[0])
    minutiaeData = getMinutiaePoints(rawData[1:])

    return minutiaeCount, minutiaeData
    

def readFingerprintImage(imageName):
    img = cv2.imread(imageName, cv2.IMREAD_GRAYSCALE)
    
    return img

def readMinutiaeImages(imageFormat = 'png'):
    for imageName in glob.glob(os.path.join(images, '*.' + imageFormat)):
        image = readFingerprintImage(imageName)
        minutiaeCount, minutiaeData = readMinutiaeData(imageName)

        patch_minu_radio = 32
        for minutiae in minutiaeData:
            x_begin = minutiae.xPosition - patch_minu_radio
            y_begin = minutiae.yPosition - patch_minu_radio
            patch_minu = image[x_begin:x_begin + 2 * patch_minu_radio,
                                 y_begin:y_begin + 2 * patch_minu_radio]
            cv2.imshow('image', patch_minu)
            cv2.waitKey()
