import cv2
import numpy as np
import grayscale 




def sobel_CV2(image):

  sobelx64f = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
  abs_sobel_x64f = np.absolute(sobelx64f)
  sobel_x_8u = np.uint8(abs_sobel_x64f)
  
  sobely64f = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
  abs_sobel_y64f = np.absolute(sobely64f)
  sobel_y_8u = np.uint8(abs_sobel_y64f)
  
  magnitude = np.hypot(sobel_x_8u, sobel_y_8u)
  theta = np.arctan2(sobel_y_8u , sobel_x_8u) 
  

  return magnitude , theta  

if __name__ == "__main__": 

  im_location = '/home/lina/Desktop/'

  file_name = 'dragon.jpeg'
  # read the image 
  image = cv2.imread(im_location+file_name) 
  
  # convert the image into grayscale
  gray_image = grayscale.BGR2GRAY(image)
  
  # apply sobel 
  M, theta = sobel_CV2(gray_image)
  
  # display the result

  cv2.imshow('M',np.uint8(M)) 
  cv2.waitKey(0)
  
