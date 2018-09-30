

import numpy as np
import cv2 
import os

def openVideo(filename = None):
    """Given a filename, checks if the file exist and is accesible 
    and returns the capture."""
    if filename is None:
        filename = 1
    elif filename.isdigit():
        filename = int(filename)

    if isinstance(filename, int):
        print("Activating integrated webcam {}".format(filename))
        capture = cv2.VideoCapture(filename)

    if(os.path.isfile(filename)):
        print("Opening file {}".format(filename))
        capture = cv2.VideoCapture(filename)

    if not capture.isOpened():
        raise Exception("Error opening file {}".format(filename))
    
    return capture;

def showFrame(windowName, frame, absValue=False, scaleMin0Max255=False):
    """Names the window to show a given frame via GUI. Offers the options 
    to take the absolute value of the frame and normalize it if you want."""
    
    if absValue:
        frame_abs = np.abs(frame)
    else:
        frame_abs = frame
    
    if scaleMin0Max255:
        frame_norm = cv2.normalize(frame_abs, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    else:
        frame_norm = frame_abs
    cv2.imshow(windowName, frame_norm)

def sobelFilter(filename, sobel_threshold, frameStride):
    """Given a filename and a frameStride, applies a Sobel filter 
    with a sobel_threshold with a specified frameStride 
    beginning from the first frame of the capture.
    """
    capture = openVideo(filename)
    
    # DEBUG
    totalFrames = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("This video file contains " + str(int(totalFrames)) + " frames.")

    frameCount = 0
    while(capture.isOpened()):
        success, frame = capture.read()
        
        if(success):
            frameCount+=1
            if(frameCount == 1 or frameCount % frameStride == 0):
                
                # DEBUG
                frameTimestamp = "{0:.2f}".format(round(capture.get(0),2))
                frameIndex = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
                print(str(frameIndex) + " " + frameTimestamp)

                # Frame Processing

                ## Resize frame
                frame = cv2.resize(frame, (1080, 720))

                ## frame to gray scale (improves filter preformance) 
                grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                ## grayframe filtered by the Sobel Filter
                sobelX = cv2.Sobel(grayFrame, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
                sobelY = cv2.Sobel(grayFrame, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=3)

                ## Gradient Magnitude or Approximation for Gradient Magnitude (Only Choose One!)
                
                #gradientAbs = np.sqrt(np.square(sobelX) + np.square(sobelY))
                gradientAbs = np.abs(sobelX) + np.abs(sobelY)

                # Apply Sobel Threshold
                retval, borders = cv2.threshold(gradientAbs, thresh=sobel_threshold, maxval=255, type=cv2.THRESH_BINARY)

                showFrame("Filtered Frame", borders, scaleMin0Max255=True)
                
                # Normal Speed cv2.waitKey(25) 
                # Max Speed     cv.waitKey(1)
                if cv2.waitKey(45) & 0xFF == ord('q'):
                    break
        
        else:
            print("Frames Filtering has Finished!" + "\n")
            break
    capture.release()
    cv2.destroyAllWindows()



#videoPath = input("Hi! Enter the video file name to process please: ")
videoPath = '../CC5213-Tarea1/comerciales/ballerina.mpg'

sobel_threshold = 150
frameStride = 4

sobelFilter(videoPath, sobel_threshold, frameStride)
print("FIN")

