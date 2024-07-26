import cv2
import numpy as np

def translate_image(image, dx, dy):
    rows, cols = image.shape[:2]
    translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
    return translated_image

# Read the image
image_path = r"/Users/yogeshbohara/Downloads/myself.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Calculate the center coordinates of the image
center = (width // 2, height // 2)

# Get user inputs
rotation_value = float(input("Enter the degree of rotation: "))
scaling_value = float(input("Enter the zooming factor (e.g., 1.0 for original size): "))

# Create the 2D rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center=center, angle=rotation_value, scale=1)
rotated_image = cv2.warpAffine(src=image, M=rotation_matrix, dsize=(width, height))

# Scale the image
scaled_image = cv2.resize(rotated_image, (0, 0), fx=scaling_value, fy=scaling_value)

# Get translation values
h = int(input("How many pixels do you want the image to be translated horizontally? "))
v = int(input("How many pixels do you want the image to be translated vertically? "))

# Translate the image
translated_image = translate_image(scaled_image, dx=h, dy=v)

# Save the final image
cv2.imwrite('Final_image.png', translated_image)

print("Image processing complete. The final image is saved as 'Final_image.png'.")
