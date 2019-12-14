import sys
import os

#from MinutiaeNetWrapper import MinutiaeNetWrapper
#from ClassifyNetWrapper import ClassifyNetWrapper

sys.path.append(os.path.realpath('./ClassifyNet'))

from ClassifyNet_utils import readMinutiaeImages

def main():
    #minutiaeNet = MinutiaeNetWrapper()
    #minutiaeNet.readImage("./ClassifyNet/testData/img_files/crd_0208s_01.png")
    #minutiaeNet.predictImage()  
    #classifyNet = ClassifyNetWrapper()
    readMinutiaeImages()
  
if __name__== "__main__":
    main()