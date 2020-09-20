#22p21c0253-ณัฐนันท์ 
import numpy as np

def covimage(image,fillter):
    return  np.array([[((image[col:col+fillter.shape[0],row:row+fillter.shape[1]])*fillter).sum() for row in range(image.shape[1]-fillter.shape[1]+1)] for col in range(image.shape[0]-fillter.shape[0]+1)])

fillter_test = np.array([[1,0,0],
                         [0,1,0],
                         [0,0,1]])

image_test = np.arange(100).reshape(10,10)
            
print("="*30)
print("Image")          
print("="*30)
print(image_test)
print("="*30)
print("Fillter")          
print("="*30)
print(fillter_test)
result = covimage(image_test,fillter_test)
print("="*30)
print("Result of convolution")          
print("="*30)
print(result)
