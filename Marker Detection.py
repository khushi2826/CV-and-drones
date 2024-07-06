import numpy as np
import cv2

def aruco_display(corners,ids,rejected,image):
	if(len(corners)>0):
		ids=ids.flatten()
		for(markerCorner,markerID) in zip(corners,ids):
			corners=markerCorner.reshape((4,2))
			(topLeft,topRight,bottomRight,bottomLeft)=corners
			topRight=(int(topRight[0]),int(topRight[1]))
			topLeft=(int(topLeft[0]),int(topLeft[1]))
			bottomRight=(int(bottomRight[0]),int(bottomRight[1]))
			bottomLeft=(int(bottomLeft[0]),int(bottomLeft[1]))
			cv2.line(image,topLeft,topRight,(0,255,0),2)
			cv2.line(image,topRight,bottomRight,(0,255,0),2)
			cv2.line(image,bottomRight,bottomLeft,(0,255,0),2)
			cv2.line(image,bottomLeft,topLeft,(0,255,0),2)
			cX=int((topLeft[0]+bottomRight[0]+topRight[0]+bottomLeft[0])/4)
			cY=int((topLeft[1]+bottomLeft[1]+bottomRight[1]+topRight[1])/4)
			#cv2.circle(image,(cX,cY),4,(0,0,255),-1)
			print(cX,cY)
			print(str(image.shape[0])+'x'+str(image.shape[1]))
			print("[Inference] Aruco marker ID: {}".format(markerID))

	return image

def pose_estimation(frame, aruco_dict_type, matrix_coefficients, distortion_coefficients):

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	arucoDict=cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
	arucoParams=cv2.aruco.DetectorParameters_create()
	corners, ids, rejected_img_points=cv2.aruco.detectMarkers(gray,arucoDict,parameters=arucoParams)
    
   	 
	if len(corners) > 0:
		for i in range(0, len(ids)):
			rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(corners[i], 50, matrix_coefficients,distortion_coefficients)
			cv2.aruco.drawDetectedMarkers(frame, corners)
			cv2.drawFrameAxes(frame, matrix_coefficients, distortion_coefficients, rvec, tvec, 20)
			print(tvec,rvec)
	return frame

arucoDict=cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
arucoParams=cv2.aruco.DetectorParameters_create()
img=cv2.imread(r"C:\Users\khush\Desktop\opencv\cv and drones101\img0.png")
print(img.shape)
h,w,_=img.shape
width=1000
height=int(width*(h/w))
img=cv2.resize(img,(width,height),interpolation=cv2.INTER_CUBIC)
corners,ids,rejected=cv2.aruco.detectMarkers(img,arucoDict,parameters=arucoParams)
detected_markers=aruco_display(corners,ids,rejected,img)


intrinsic_camera = np.array(((207.66132141,0,251.41218615),(0,205.751007,338.91119239),(0,0,1)))
distortion = np.array(( 0.07640411,-0.06229856,0.01462332,0.0039293,0.00467759))

detected_markers=pose_estimation(detected_markers,cv2.aruco.DICT_4X4_50,intrinsic_camera,distortion)
#corners,ids,rejected=cv2.aruco.detectMarkers(img,arucoDict,parameters=arucoParams)
#detected_markers=aruco_display(corners,ids,rejected,img)
cv2.imshow("Image",detected_markers)
cv2.waitKey(0)
cv2.destroyAllWindows()	
	

	