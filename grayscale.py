import cv2
import numpy as np

def BGR2GRAY(image):
  # convert to grayscale 
  
  # mehtod 1: by using numpy 
  '''
  gray_image = np.zeros((image.shape[0],image.shape[1]),np.uint8)
  
  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      #gray_image[i,j] = np.clip( (image[i,j,0] + image[i,j,1] + image[i,j,2] )/3, 0, 255) # using average method
      gray_image[i,j] = np.clip(0.07 * image[i,j,0]  + 0.72 * image[i,j,1] + 0.21 * image[i,j,2], 0, 255) # using luminosity method
  '''  
     
  # method 2: by using cv2. This is more efficient than method 1.     
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
  # display the image
  cv2.imshow('grayscale image',gray_image)
  cv2.waitKey(0)
    
  return gray_image 
  


  
  
  
