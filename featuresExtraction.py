import numpy as np
import cv2

def nFramesFromVideo(videoFile):
    cap = cv2.VideoCapture(videoFile)
    countFrames = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('Video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


print("Executing nFramesFromVideo...")
nFramesFromVideo('../CC5213-Tarea1/comerciales/ballerina.mpg')
print("Finish!")



        
        