import cv2
import matplotlib.pyplot as plt
import numpy as np

def ig_filter(s):
    a=cv2.imread(s)
    a_rgb= cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    
    #changing saturation
    hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.5, 0, 255).astype(np.uint8)
    b= cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    
    #changing brightness and contrast
    bright=0.5
    cont=1.5
    c = cv2.convertScaleAbs(b,0,bright,cont)
    
    plt.subplot(121).imshow(a_rgb);plt.title('original');plt.axis("off")
    plt.subplot(122).imshow(c);plt.title('filtered');plt.axis("off")
    plt.show()
    
s1=r"C:\Users\khush\Desktop\opencv\sunset.jpeg"
ig_filter(s1)    