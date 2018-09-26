
import numpy as np
import cv2

def nFramesFromVideo(videoFile, n):
    """Return frames indexes from a video file every n frames with its timestamps 
    in miliseconds"""

    print("\n" + "Frames Extraction has Started...")
    capture = cv2.VideoCapture(videoFile)
    frameCounter = 0
"""
    totalFrames = capture.get(7)
    print("This video file contains " + str(int(totalFrames)) + " frames.")
"""
    while(capture.isOpened()):
        success, frame = capture.read()
        if success:
            frameCounter +=1
            if(frameCounter % n == 0):
                
                cv2.imshow('Video', frame)
                frameTimestamp = "{0:.2f}".format(round(capture.get(0),2))
                frameIndex = int(capture.get(1))
                print(str(frameIndex) + " " + frameTimestamp)

                # cv2.waitKey(25) for normal speed
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
nFramesFromVideo('../CC5213-Tarea1/comerciales/ballerina.mpg', 4)





        
        