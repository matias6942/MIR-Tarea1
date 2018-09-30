
import cv2 
import os
import easygui


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

def sobelFilter(filename, sobel_threshold):
    """Given a filename, applies a Sobel filter with a threshold
    to the file and returns .............
    """
    capture = openVideo(filename)
    frameStride = 4
    
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

                # Wait for a key
                # Normal Speed cv2.waitKey(25) 
                # Max Speed     cv.waitKey(1)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
        
        else:
            print("Frames Filtering has Finished!" + "\n")
            break
    capture.release()
    cv2.destroyAllWindows()



#videoPath = input("Hi! Enter the video file name to process please: ")
videoPath = '../CC5213-Tarea1/comerciales/ballerina.mpg'

sobel_threshold = 150

sobelFilter(videoPath, sobel_threshold)
print("FIN")