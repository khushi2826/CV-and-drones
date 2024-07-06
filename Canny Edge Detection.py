import cv2
import matplotlib.pyplot as plt
import numpy as np
def solve(s):
    a=cv2.imread(s)
    #code for canny edge detection
    a = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    blurred=cv2.GaussianBlur(a,(5,5),0)
    edges=cv2.Canny(blurred,20,150)
    plt.figure(figsize=[10,10])
    
    #code to output the image
    plt.subplot(121).imshow(a);plt.title('image');plt.axis("off")
    plt.subplot(122).imshow(edges,cmap="gray");plt.title("edges image");plt.axis("off")
    plt.show()
    

s1=r"C:\Users\khush\Desktop\opencv\butterfly.jpeg"
b=solve(s1)
 
