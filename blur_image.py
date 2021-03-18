import numpy as np

def initialize_kernel(size , sigma):

  """ This function initializes a gaussian kernel with the desired size and sigma. """

  w, h = size
  
  x = np.linspace(-1,1,w)
  y = np.linspace(-1,1, h)
  x_cor, y_cor  = np.meshgrid(x, y)
  
  kernel = 1/(2*np.pi*np.power(sigma,2) ) *np.exp((- (x_cor ** 2 + y_cor ** 2) )/ (2*np.power(sigma,2)))
  
  """ Gaussion function: 1/(2 *pi*sigma^2) e^(-(x^2+y^2)/2sigma^2) """
  
  kernel = kernel/np.sum(kernel) # normalization 

  return kernel
  
def padding(image):

  padded_image = np.pad(image , ((1,1),(1,1)) , 'constant', constant_values=(0,0) )

  return padded_image
  
 
def conv2d(image, ftr):
    s = ftr.shape + tuple(np.subtract(image.shape, ftr.shape) + 1)
    sub_image = np.lib.stride_tricks.as_strided(image, shape = s, strides = image.strides * 2)
    return np.einsum('ij,ijkl->kl', ftr, sub_image) 
    
    

def GaussianBlur(gray_image):
  ftr = initialize_kernel(size=(3,3) , sigma=1.5)
  
  blurred_image = conv2d(gray_image, ftr)
  
  return blurred_image




