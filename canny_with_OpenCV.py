import cv2
import numpy as np
import grayscale 
import blur_image


def canny_CV2(image,low_threshold, high_Threshold):

  edges = cv2.Canny(image,low_threshold, high_Threshold)
  
  
  return edges 
  
  

if __name__ == "__main__": 

  im_location = '/home/lina/Desktop/'

  file_name = 'dragon.jpeg'
  # read the image 
  image = cv2.imread(im_location+file_name) 
  
  # convert the image into grayscale
  gray_image = grayscale.BGR2GRAY(image)
  
  # blur the gray image
  
  blurred_image = blur_image.GaussianBlur(gray_image)
  
  # apply canny 
  edges = canny_CV2(blurred_image.astype(np.uint8), 100, 200)
  
  # display the result
  cv2.imshow('M',np.uint8(edges))
  cv2.waitKey(0)
  
    
  
  
  
  
  
