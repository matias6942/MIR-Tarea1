
import numpy as np
import cv2

def nFramesFromVideo(videoFile, frameStride, width, height):
    """Return frames resized to width and heigth from a video file every n frames with its timestamps 
    in miliseconds"""

    print("\n" + "Frames Extraction has Started...")
    capture = cv2.VideoCapture(videoFile)
    
    totalFrames = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("This video file contains " + str(int(totalFrames)) + " frames.")
    
    frameCounter = 0
    while(capture.isOpened()):
        success, frame = capture.read()
        if success:
            frameCounter +=1
            if(frameCounter % frameStride == 0):
                frame = cv2.resize(frame, (width, height))
                cv2.imshow('Video', frame)
                
                frameTimestamp = "{0:.2f}".format(round(capture.get(0),2))
                frameIndex = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
                print(str(frameIndex) + " " + frameTimestamp)

                # Normal Speed cv2.waitKey(25) 
                # Max Speed     cv.waitKey(1)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        else:
            print("Frames Extraction has Finished!" + "\n")
            break
        
    capture.release()
    cv2.destroyAllWindows()


print("\n" + "Executing featuresExtraction.py..." + "\n")

#videoPath = input("Hi! Enter the video file name to process please: ")
#commFolder = input("\n" + "Now,  enter the folder name that contains the commercials to look for: ")

# Set frame stride
frameStride = 4

# Resize to 10x10 to reduce quantity of pixels at every frame
width = 1080
height = 720

nFramesFromVideo('../CC5213-Tarea1/comerciales/ballerina.mpg', frameStride, width, height)
        
        