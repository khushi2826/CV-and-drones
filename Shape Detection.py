def shape(s):
    #code to solve the problem
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    
    image = cv2.imread(s)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 30, 100)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    # Filter out small contours
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]

    # Sort contours based on area in descending order
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Create a copy of the image to draw on
    result_image = image.copy()

    # Mark centers of the largest two contours
    for idx, contour in enumerate(contours[:2]):
        # Calculate the moments of the contour
        M = cv2.moments(contour)

        # Calculate the center of mass (centroid)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        # Draw a circle at the center
        cv2.circle(result_image, (cx, cy), 5, (255, 0, 0), -1)

        # Mark the center with a text label
        cv2.putText(result_image, f"largeCenter {idx+1}", (cx + 10, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)


    # Loop over the contours
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Get the number of vertices (sides) of the polygon
        num_sides = len(approx)
        # Determine the shape based on the number of sides
        shape = "unknown"
        if num_sides == 3:
            shape = "triangle"
        elif num_sides == 4:
            # Check if it's a rectangle or square
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            shape = "square" if 0.95 <= aspect_ratio <= 1.05 else "rectangle"
        elif num_sides == 5:
            shape = "pentagon"
        elif num_sides == 6:
            shape = "hexagon"
        elif num_sides == 7:
            shape = "heptagon"
        elif num_sides == 8:
            shape = "octagon"
        elif num_sides == 9:
            shape = "nonagon"
        else:
            shape = "circle"  

        # Draw contours and display the shape name around recognized shapes
        if shape != "unknown":
            cv2.drawContours(result_image, [approx], -1, (0, 0, 255), 2)
            x, y = approx[0][0]
            cv2.putText(result_image, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 4)
    

    plt.subplot(121).imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB));plt.title('Input');plt.axis('off')
    plt.subplot(122).imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB));plt.title('Result');plt.axis('off')
    plt.show()
    


s=r"C:\Users\khush\Desktop\opencv\shapedet.jpg"
shape(s)
 
 