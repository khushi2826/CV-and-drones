import cv2
import matplotlib.pyplot as plt
import numpy as np
def solve(s):
    a=cv2.imread(s)
    a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    a_hsv=cv2.cvtColor(a,cv2.COLOR_RGB2HSV)
    lower = np.array([100, 50, 50])  #range to detect blue color
    upper = np.array([130, 255, 255])
    masked = cv2.inRange(a_hsv, lower, upper)
    plt.imshow(masked);plt.show()
    contours,hierarchy=cv2.findContours(masked,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    copy=a.copy()
    cv2.drawContours(copy,contours,-1,(0,0,0),2)
    plt.figure(figsize=[10,10])
    
    plt.subplot(121).imshow(a);plt.title('input');plt.axis("off")
    plt.subplot(122).imshow(copy);plt.title("output");plt.axis("off")
    plt.show()
    
s1=r"C:\Users\khush\Desktop\opencv\shapes.jpeg"
b=solve(s1)
 