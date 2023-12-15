# import cv2
# import pytesseract
# import numpy as np

# def get_contours(image):
#     """Get the contours of the objects in the image."""
#     contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     return contours

# def get_bounding_boxes(contours):
#     """Get the bounding boxes of the objects in the image."""
#     bounding_boxes = []
#     for contour in contours:
#         x, y, w, h = cv2.boundingRect(contour)
#         bounding_boxes.append((x, y, w, h))
#     return bounding_boxes

# def get_text(bounding_boxes):
#     """Get the text inside the bounding boxes."""
#     text = []
#     for bounding_box in bounding_boxes:
#         x, y, w, h = bounding_box
#         image = image[y:y+h, x:x+w]
#         text.append(pytesseract.image_to_string(image, lang='eng'))
#     return text

# def main():
#     """The main function."""
#     image = cv2.imread('image.PNG')
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#     thresh_image = cv2.threshold(blur_image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
#     contours = get_contours(thresh_image)
#     bounding_boxes = get_bounding_boxes(contours)
#     text = get_text(bounding_boxes)
#     print('The text in the image is:', ' '.join(text))

# if __name__ == '__main__':
#     main()


####this is the second choice

#==========================================================


# # import pytesseract
# imoprt cv2
# # from PIL import Image

# # # Load the image containing the hand-written text
# # image_path = 'image.PNG'
# # img = Image.open(image_path)

# # # Use Tesseract to recognize the text in the image
# # text = pytesseract.image_to_string(img)

# # # Print the recognized text
# # print(text)

import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
import pytesseract
from PIL import Image

# Load the image containing handwritten text 
image = cv2.imread('E:\PROJECT\Python\image_2.jpg') 
  
#Plot the original image 
plt.subplot(1, 2, 1) 
plt.title("Original") 
plt.imshow(image) 
  
# Adjust the brightness and contrast 
# Adjusts the brightness by adding 10 to each pixel value 
brightness = 10 
# Adjusts the contrast by scaling the pixel values by 2.3 
contrast = 2.3  
image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness) 
  
#Save the image 
cv2.imwrite('modified_image.jpg', image2) 
# Use Tesseract-OCR to extract the text from the image
extracted_text = pytesseract.image_to_string(image2, lang='eng')

for c in extracted_text:
    if c.isdigit():
        print("Extracted numbers from the list : " +c)
 
# Print the extracted text
print(extracted_text)

plt.subplot(1, 2, 2) 
plt.title("Brightness & contrast") 
plt.imshow(image2) 
plt.show() 