import cv2
import matplotlib.pyplot as plt
import numpy as np

#defining sobel filter
def sobel(s):
    a=cv2.imread(s)
    a=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)                  #conversion to grayscale
    sobelx=cv2.Sobel(a,-1,1,0)                            
    sobely=cv2.Sobel(a,-1,0,1)                            
    gradient=cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0) #magnitude of gradient
    edged=cv2.normalize(gradient,None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)                         
    plt.subplot(121).imshow(a,cmap="gray");plt.title('grayscaled image');plt.axis("off")
    plt.subplot(122).imshow(edged,cmap="gray");plt.title('edge detected image');plt.axis("off")
    plt.show()
    

s1=r"C:\Users\khush\Desktop\opencv\butterfly.jpeg"

b=sobel(s1)
print(type(b))