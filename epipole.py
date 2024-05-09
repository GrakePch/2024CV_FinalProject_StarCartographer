import matplotlib.pyplot as plt
import numpy as np


def draw_epipolar_lines(img, pts1, pts2, F):
    """
    Params:
    -------
    pts1: np.array
        array of size (N, 2). N points of coordinates (x, y) in view 1.
    pts2: np.array
        array of size (N, 2). N points of coordinates (x, y) in view 2.
    F: np.array
        array of size (3, 3). fundamental matrix.

    Returns:
    --------
    lines: list
        list of tuples. Each tuple contains the coordinates of the two extremal points of the epipolar segment drawn.
    """
    lines = []

    plt.figure()
    plt.imshow(img)
    plt.axis('off')  # Turn off axis
    for i in range(len(pts1)):
        plt.scatter(pts2[i,0], pts2[i,1], s=10)
        
    # fix the xlim and ylim
    xlim = plt.xlim()
    ylim = plt.ylim()
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    h, w, _ = img.shape
        
    for i in range(len(pts1)):
        # Get homogeneous coordinates
        pt1_homo = np.hstack((pts1[i], 1))
        pt2_homo = np.hstack((pts2[i], 1))
        # pt1.T @ F @ pt2 = 0
        # F.T @ pt1 = l2
        #   F @ pt2 = l1
        epipolarLine1inView2 = F.T @ pt1_homo
        
        epiPtLeft = [0, -epipolarLine1inView2[2] / epipolarLine1inView2[1]]
        epiPtRight = [w, (-epipolarLine1inView2[2] - epipolarLine1inView2[0] * w) / epipolarLine1inView2[1]]
        
        lines.append((epiPtLeft, epiPtRight))
        
        plt.plot([epiPtLeft[0], epiPtRight[0]], [epiPtLeft[1], epiPtRight[1]], alpha=0.5)
        
    return lines