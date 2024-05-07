import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Circle
import numpy as np
import json

def readImg(path, name, metaName=None):
    img = mpimg.imread(path + name + ".png")
    if (img.shape[2] > 3):
        img = img[:,:,:3]
    if metaName is None:
        metaName = name
    f = open(path + metaName + ".json")
    imgMeta = json.load(f)
    dim = [0, 0]
    dim[1], dim[0], _ = img.shape
    imgMeta["dim"] = dim
    
    return img, imgMeta

def showImg(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
def showImgUseArea(img, imgMeta):
    center = imgMeta["useCenter"]
    radius = imgMeta["useRadius"]
    plt.imshow(img)
    plt.axis('off')  # Turn off axis
    plt.scatter(center[0], center[1], color='red', s=5)
    plt.gca().add_patch(Circle(center, radius, color="red", fill=False))
    plt.show()

def showImgWithPts(img, pts):
    plt.figure()
    plt.imshow(img)
    plt.axis('off')  # Turn off axis
    plt.scatter(pts[:,0], pts[:,1], color='red', s=5)
    plt.show()

def keepUsePixels(img, imgMeta):
    center = imgMeta["useCenter"]
    radius = imgMeta["useRadius"]
    for v in range(imgMeta["dim"][1]):
        for u in range(imgMeta["dim"][0]):
            if np.linalg.norm([center[0] - u, center[1] - v]) > radius:
                img[v][u] = [0., 0., 0.]
    return img

def printMeta(imgMeta):
    print(json.dumps(imgMeta,sort_keys=True, indent=4))
    
def saveImg(img, path, name):
    plt.imsave(path + name + '.png', img)