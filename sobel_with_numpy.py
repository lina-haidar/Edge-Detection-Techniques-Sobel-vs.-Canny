import cv2
import numpy as np
import grayscale


def sobel_x():

  gaussian_1d = np.array([1,2,1],np.float32)
  x_derivative = np.array([-1,0,1],np.float32)
  s_x = np.outer(gaussian_1d,x_derivative) 
  
  return s_x
  
def sobel_y():

  gaussian_1d = np.array([1,2,1],np.float32)
  x_derivative = np.array([-1,0,1],np.float32)
  s_y = np.outer(x_derivative,gaussian_1d) 

  return s_y
  

  
def padding(image):

  padded_image = np.pad(image , ((1,1),(1,1)) , 'constant', constant_values=(0,0) )

  return padded_image
  
  
def conv2d(image, ftr):
    image = padding(image)
    s = ftr.shape + tuple(np.subtract(image.shape, ftr.shape) + 1)
    sub_image = np.lib.stride_tricks.as_strided(image, shape = s, strides = image.strides * 2)
    return np.einsum('ij,ijkl->kl', ftr, sub_image) 
    
    

  
def sobel(gray_image):  
  
  # ___________________ Sobel Algorithm _______________________ # 
  
  
  #     ____________________STEP 1:___________________          #
  # 	   Find G_x and G_y by applying sobel_x and sobel_y

  G_x = conv2d(gray_image , sobel_x())
  G_y = conv2d(gray_image , sobel_y())

  #     ____________________STEP 2:___________________          #
  #	    Calculate the magnitude and direction
  
  M = np.sqrt( np.power(G_x,2)  +  np.power(G_y,2) )
 
  
  theta = np.arctan2(G_y,G_x)
  
  
  return M, theta 
  
  
  
  
if __name__ == "__main__": 

  im_location = '/home/lina/Desktop/'

  file_name = 'dragon.jpeg'
  # read the image 
  image = cv2.imread(im_location+file_name) 
  
  # convert the image into grayscale
  gray_image = grayscale.BGR2GRAY(image)
  
  # apply sobel 
  M, theta = sobel(gray_image)
  
  # display the result
  cv2.imshow('M',np.uint8(M)) # what is np.uint8 ?
  cv2.waitKey(0)
  cv2.imwrite('/home/lina/Desktop/sobel.png', np.uint8(M))
  
  
  
  
  
  



  


