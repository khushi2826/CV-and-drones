import cv2
import numpy as np
import matplotlib.pyplot as plt

def hough_line(s):
# Read image
    image = cv2.imread(s)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# Convert image to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# Use canny edge detection
    edges = cv2.Canny(gray,50,150)

# Apply HoughLinesP method to 
# to directly obtain line end points
    lines_list =[]
    lines = cv2.HoughLinesP(edges,1,np.pi/180,threshold=100,minLineLength=5,maxLineGap=10)

# Iterate over points
    for points in lines:
	    x1,y1,x2,y2=points[0];cv2.line(image,(x1,y1),(x2,y2),(255,0,0),2);lines_list.append([(x1,y1),(x2,y2)])
     
    cv2.imwrite('detectedLines.png',image)
    plt.subplot(121).imshow(image);plt.axis("off")
    plt.subplot(122).imshow(edges,cmap="grey");plt.axis("off");plt.show()



s1=r"C:\Users\khush\Desktop\opencv\roads.jpg"
b=hough_line(s1)
