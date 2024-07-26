import cv2
import numpy as np

def split_image(image):
    height, width = image.shape[:2]
    center_x, center_y = width//2, height//2
    top_left = image[:center_y, :center_x]
    top_right = image[:center_y, center_x:]
    bottom_left = image[center_y:, :center_x]
    bottom_right = image[center_y:, center_x:]

    return top_left, top_right, bottom_left, bottom_right

image_path = r"/Users/yogeshbohara/Downloads/myself.jpeg"

image = cv2.imread(image_path)
if image is None:
    print("Error loading image")
    exit()

top_left, top_right, bottom_left, bottom_right = split_image(image)

cv2.imshow('Original Image', image)
cv2.imshow('Top Left Quadrant', top_left)
cv2.imshow('Top Right Quadrant', top_right)
cv2.imshow('Bottom Left Quadrant', bottom_left)
cv2.imshow('Bottom Right Quadrant', bottom_right)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow('Original Image', image)
cv2.imshow('Top Left Quadrant', top_left)
cv2.waitKey(0)
cv2.destroyAllWindows()
