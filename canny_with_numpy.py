import cv2
import numpy as np
import grayscale 
import blur_image
import sobel_with_numpy
import sobel_with_OpenCV




def non_max_suppression(img, D):
    M, N = img.shape
    Z = np.zeros((M,N), dtype=np.int32)
    angle = D * 180. / np.pi
    angle[angle < 0] += 180

    
    for i in range(1,M-1):
        for j in range(1,N-1):
            try:
                q = 255
                r = 255
                
               #angle 0
                if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                    q = img[i, j+1]
                    r = img[i, j-1]
                #angle 45
                elif (22.5 <= angle[i,j] < 67.5):
                    q = img[i+1, j-1]
                    r = img[i-1, j+1]
                #angle 90
                elif (67.5 <= angle[i,j] < 112.5):
                    q = img[i+1, j]
                    r = img[i-1, j]
                #angle 135
                elif (112.5 <= angle[i,j] < 157.5):
                    q = img[i-1, j-1]
                    r = img[i+1, j+1]

                if (img[i,j] >= q) and (img[i,j] >= r):
                    Z[i,j] = img[i,j]
                else:
                    Z[i,j] = 0

            except IndexError as e:
                pass
    
    return Z


def threshold(img, lowThresholdRatio , highThresholdRatio ):
    
    highThreshold = img.max() * highThresholdRatio;
    lowThreshold = highThreshold * lowThresholdRatio;
 
    M, N = img.shape
    res = np.zeros((M,N), dtype=np.int32)
    
    weak = np.int32(25)
    strong = np.int32(255)
    
    strong_i, strong_j = np.where(img >= highThreshold)
    zeros_i, zeros_j = np.where(img < lowThreshold)
    
    weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))
    
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    return res, weak, strong

def hysteresis(img, weak, strong=255):
    M, N = img.shape  
    for i in range(1, M-1):
        for j in range(1, N-1):
            if (img[i,j] == weak):
                try:
                    if ((img[i+1, j-1] == strong) or (img[i+1, j] == strong) or (img[i+1, j+1] == strong)
                        or (img[i, j-1] == strong) or (img[i, j+1] == strong)
                        or (img[i-1, j-1] == strong) or (img[i-1, j] == strong) or (img[i-1, j+1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass
    return img

if __name__ == "__main__": 
 
  im_location = '/home/lina/Desktop/'

  file_name = 'dragon.jpeg'
  # read the image 
  image = cv2.imread(im_location+file_name) 

  # STEP 0:
  gray_image = grayscale.BGR2GRAY(image) 
  cv2.imwrite('/home/lina/Desktop/dragon_gray.png' , gray_image)
  
  # STEP 1:

  blurred_image = blur_image.GaussianBlur(gray_image)

  # STEP 2:

  #M , theta = sobel_with_numpy.sobel(blurred_image)
  M , theta = sobel_with_OpenCV.sobel_CV2(blurred_image)

  # display the result
  cv2.imshow('step 2',np.uint8(M))
  cv2.waitKey(0)

  # STEP 3: 
  Z = non_max_suppression(M,theta)
  
  cv2.imshow('step 3',np.uint8(Z))
  cv2.waitKey(0)
  
  # STEP 4:   
  res, weak, strong = threshold(Z, lowThresholdRatio=0.05, highThresholdRatio=0.09) 
  
  # STEP 5:
  
  canny =  hysteresis(res, weak, strong=255)
  cv2.imshow('step 5', np.uint8(canny) )
  cv2.waitKey(0)
  
  cv2.imwrite('/home/lina/Desktop/canny.png' , canny)








  

