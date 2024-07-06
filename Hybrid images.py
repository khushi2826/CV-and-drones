import cv2
import matplotlib.pyplot as plt
import numpy as np

def graynresize(s):
    a=cv2.imread(s)
    a=cv2.resize(cv2.cvtColor(a,cv2.COLOR_BGR2GRAY),(256,256))
    
    return a

def lpf(s):
    b=graynresize(s)
    boxa=cv2.boxFilter(b,0,(15,15))
    plt.imshow(boxa,cmap="gray");plt.title('lpf image');plt.axis("off")
    plt.show()
    return boxa

def hpf(s):
    c=graynresize(s)
    sobelx=cv2.Sobel(c,-1,1,0)
    sobely=cv2.Sobel(c,-1,0,1)                            
    gradient=cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0) 
    edged=cv2.normalize(gradient,None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F) 
    plt.imshow(edged,cmap="gray");plt.title('hpf image ');plt.axis("off")
    plt.show()
    return edged

def ftoffilter(s):
    b=graynresize(s)
    boxa=cv2.boxFilter(b,0,(15,15))
    sobelx=cv2.Sobel(b,-1,1,0)
    sobely=cv2.Sobel(b,-1,0,1)                            
    gradient=cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0) 
    edged=cv2.normalize(gradient,None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F) 
    ftl=np.fft.fft2(boxa)
    ftlshift=np.fft.fftshift(ftl)
    fth=np.fft.fft2(edged)
    fthshift=np.fft.fftshift(fth)
    plt.subplot(121).imshow(np.log1p(np.abs(ftlshift)),cmap="gray");plt.title('fourier of lpf image');plt.axis("off")
    plt.subplot(122).imshow(np.log1p(np.abs(fthshift)),cmap="gray");plt.title('fourier of hpf image');plt.axis("off")
    plt.show()

def fourier(s1,s2):
    d=graynresize(s1) ;e=graynresize(s2)
    fts1=np.fft.fft2(d) ;fts2=np.fft.fft2(e)
    fts1shift=np.fft.fftshift(fts1) ;fts2shift=np.fft.fftshift(fts2)
    plt.subplot(121).imshow(np.log1p(np.abs(fts1shift)),cmap="gray");plt.title('fourier of image 1');plt.axis("off")
    plt.subplot(122).imshow(np.log1p(np.abs(fts2shift)),cmap="gray");plt.title('fourier of image 2');plt.axis("off")
    plt.show()
    ftoffilter(s1)
    ftoffilter(s2)
    
    
    
    
def hybrid(s1,s2):
    a=graynresize(s1);b=graynresize(s2)
    plt.subplot(121).imshow(a,cmap="gray");plt.title('image1');plt.axis("off")
    plt.subplot(122).imshow(b,cmap="gray");plt.title('image2');plt.axis("off")
    plt.show()
    c=lpf(s1);lpf(s2)
    hpf(s1);d=hpf(s2)
    fourier(s1,s2)
    print(c.shape)
    print(d.shape)
    print(c.dtype)
    print(d.dtype)
    d= d.astype(np.uint8) #because both images have different dtype
    hybimg=cv2.addWeighted(c,0.5,d,0.5,0)
    plt.imshow(hybimg,cmap="gray");plt.title('hybrid image');plt.axis("off")
    plt.show()
    
    
    
    
a1=r"C:\Users\khush\Desktop\opencv\img1.jpg"
a2=r"C:\Users\khush\Desktop\opencv\image.jpeg"
hybrid(a1,a2)