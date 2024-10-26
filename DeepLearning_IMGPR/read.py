"""
import cv2

# Read an image
image = cv2.imread('/Users/swetha/Downloads/dog.jpg')

# Display the image using OpenCV
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To check dimensions of the image
print(image.shape)
"""

#Task : in a folder, upload 10 images, read the images in this folder and display them using OpenCVx
import cv2
import os

# Path to the folder containing the images
folder_path = '/Users/swetha/Desktop/springboard/images'

# Get the list of image files in the folder
image_files = os.listdir(folder_path)

# Loop through the first 10 images
for image_file in image_files[:10]:
    # Full path of the image file
    image_path = os.path.join(folder_path, image_file)
    
    # Read the image
    img = cv2.imread(image_path)
    
    if img is not None:
        # Show the image
        cv2.imshow('Image', img)
        
        # Wait for a key press before closing the window and moving to the next image
        cv2.waitKey(0)
    else:
        print(f"Could not read {image_file}")

# Close all OpenCV windows
cv2.destroyAllWindows()