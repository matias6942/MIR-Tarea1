

import numpy as np
import cv2 
import os
from datetime import datetime

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

    # Data extracted from video
    frameTimestamps = []
    frameDescriptors = []

    frameCount = 0
    while(capture.isOpened()):
        success, frame = capture.read()
        
        if(success):
            frameCount+=1
            if(frameCount == 1 or frameCount % frameStride == 0):
                

                # Save timestamp for each frame in seconds
                frameTimestamp = "{0:.1f}".format(round(capture.get(0)/1000,2))
                frameTimestamps.append(frameTimestamp)

                """
                # DEBUG                
                frameIndex = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
                print(str(frameIndex) + " " + frameTimestamp)
                """
                
                # Frame Processing

                ## Resize frame
                frame = cv2.resize(frame, (10, 10))

                ## frame to gray scale (improves filter preformance) 
                grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
                ## grayframe filtered by the Sobel Filter
                sobelX = cv2.Sobel(grayFrame, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
                sobelY = cv2.Sobel(grayFrame, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=3)

                ## Gradient Magnitude or Approximation for Gradient Magnitude 
                
                gradientAbs = np.sqrt(np.square(sobelX) + np.square(sobelY))

                # Apply Sobel Threshold to obtain a descriptor 
                retval, borders = cv2.threshold(gradientAbs, thresh=sobel_threshold, maxval=255, type=cv2.THRESH_BINARY)

                # Save each descriptor normalized
                frameDescriptors.append(borders.flatten()/255)     
               

                """
                showFrame("Filtered Frame", frame, scaleMin0Max255=True)
                # Normal Speed cv2.waitKey(25) 
                # Max Speed     cv.waitKey(1)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                """
        
        else:
            break

    capture.release()
    cv2.destroyAllWindows()

    frameTimestamps = np.asarray(frameTimestamps)
    frameDescriptors = np.asarray(frameDescriptors)

    return frameTimestamps, frameDescriptors

def npArraytoFolder(folderName, npArray, npArrayName):
    """Saves an npArray in a folder with folderName
    in the current directory.
    """
    if not os.access(folderName, os.F_OK):
        os.mkdir(folderName)

    os.chdir("./" + folderName)
    np.save(npArrayName, npArray)
    os.chdir("../")


## Set Params and Run

### Extracción de Características
sobel_threshold = 150
frameStride = 4

### Búsqueda por Similitud
distance_threshold = 1.5

"""
std_input = input("\n" + "Ingrese el nombre del video de televisión" + 
"(con su extensión) y luego el nombre de la carpeta con los comerciales " +
"a detectar SEPARADOS POR UN ESPACIO: " + "\n") 
"""

t_inicial = datetime.now()

std_input = "mega-2014_04_10.mp4 comerciales"

video_television = std_input.split(" ")[0]
video_comercial_path = "../" + std_input.split(" ")[1]

video_television_path = "./television/" + video_television

#frameTimestamps, frameDescriptors =  sobelFilter(video_television_path, sobel_threshold, frameStride)

videoName = str(os.path.basename(video_television_path).split(".")[0])

TelevisionDescriptors = "TelevisionDescriptors"
CommercialsDescriptors = "CommercialsDescriptors"

"""
npArraytoFolder(TelevisionDescriptors, frameTimestamps, "frameTimestamps_" + videoName)
npArraytoFolder(TelevisionDescriptors, frameDescriptors, "frameDescriptors_" + videoName)

if not os.access(CommercialsDescriptors, os.F_OK):
    os.mkdir(CommercialsDescriptors)

os.chdir("./" + CommercialsDescriptors)
for commercial in os.listdir(video_comercial_path):
    video_comercial = video_comercial_path + "/" + commercial
    frameTimestamps, frameDescriptors = sobelFilter(video_comercial, sobel_threshold, frameStride)
    commercial = str(os.path.basename(commercial.split(".")[0]))
    np.save("frameDescriptors_" + commercial, frameDescriptors)
os.chdir("../")


print("\n" + " I) La extracción de características ha terminado! " + 
"Los descriptores calculados se encuentran en las carpetas: " +
"\n" + "\n" + "     " + TelevisionDescriptors + " y " + CommercialsDescriptors)
"""

# Búsqueda por Similitud

SimilaritySearch = "SimilaritySearch"

"""
os.chdir("./" + TelevisionDescriptors)
tv_descriptors = np.load("frameDescriptors_" + videoName + ".npy") 
tv_timestamps = np.load("frameTimestamps_"+ videoName + ".npy")
os.chdir("../")

bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=False)

os.chdir("./" + CommercialsDescriptors)
for commercial in os.listdir(os.getcwd()):
    video_comercial = commercial.split("_")[1].split(".")[0]
    commercial_descriptors = np.load(commercial)
    matches = bf.match(tv_descriptors, commercial_descriptors)
    Q = []
    K = []
    for match in matches:
        if match.distance <= distance_threshold:
            Q.append(tv_descriptors[match.queryIdx])
            K.append(commercial_descriptors[match.trainIdx])
            
            #print("timestamp = " + tv_timestamps[match.queryIdx])

            #DEBUG
            #print("distance with best match = " + str(match.distance))

    Q = np.asarray(Q)
    K = np.asarray(K)

    os.chdir("../")
    npArraytoFolder(SimilaritySearch, K, "K_" + video_comercial)
    os.chdir("./" + CommercialsDescriptors)
    

os.chdir("../")
npArraytoFolder(SimilaritySearch, Q, "Q_" + videoName)


print("\n" + " II) La búsqueda por similitud ha terminado! " + 
"Los conjuntos Q y K se encuentran en la carpeta: " +
"\n" + "\n" + "     " + SimilaritySearch)
"""

#Detección de Apariciones

detections = open("detecciones.txt", "w")
detections.write(videoName + "\t" + "timestamp" + "\t" + "duracion"
+ "\t" + "comercialName")
detections.close()

t_final = datetime.now()
t_delta = t_final- t_inicial
print("\n" + "El tiempo de ejecución fue de: " + str(t_delta) + "\n")


