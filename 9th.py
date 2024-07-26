
           
import cv2
import numpy as np

# Load the image
image_path = r"R.jpeg" 
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge detection
edges = cv2.Canny(gray, 100, 200) 

# Texture extraction
kernel = np.ones((5, 5), np.float32) / 25 
texture = cv2.filter2D(gray, -1, kernel)

# Display the original image, edges, and texture
cv2.imshow("Original Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Texture", texture)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()





