import numpy as np
import cv2 as cv
import glob


################ FIND CHESSBOARD CORNERS - OBJECT POINTS AND IMAGE POINTS #############################

chessboardSize = (8,6)
frameSize = (640,480)



# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)


# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)

size_of_chessboard_squares_mm = 20
objp = objp * size_of_chessboard_squares_mm


# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.


images = glob.glob(r"C:\Users\khush\Desktop\opencv\cv and drones101\cam\*.jpeg")
 
for image in images:

    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)

    # If found, add object points, image points (after refining them)
    if ret == True:

        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
        



############## CALIBRATION #######################################################

ret, cameraMatrix, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, frameSize, None, None)

print(dist)
print("Camera Matrix",cameraMatrix)

def undistort(s):
    # Load the distorted image
    distorted_img = cv.imread(s)
    
    if distorted_img is None:
        print(f"Error: Failed to load the image at path: {s}")
        return

    # Undistort the image
    undistorted_img = cv.undistort(distorted_img, cameraMatrix, dist)

    # Display the original and undistorted images
    cv.imshow("Original Image", distorted_img)
    cv.imshow("Undistorted Image", undistorted_img)
    cv.waitKey()
    cv.destroyAllWindows()

undistort(r"C:\Users\khush\Desktop\opencv\cv and drones101\cam\8.jpeg")