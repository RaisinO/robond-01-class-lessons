import numpy as np
import cv2


def perspect_transform(img, src, dst):

    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    return warped

#dst_size = 5
#bottom_offset = 6
#src = np.float32([[15, 140], [301 ,140],[200, 96], [118, 96]])
#dst = np.float32([[image.shape[1]/2 - dst_size, image.shape[0] - bottom_offset],
#                  [image.shape[1]/2 + dst_size, image.shape[0] - bottom_offset],
#                  [image.shape[1]/2 + dst_size, image.shape[0] - 2*dst_size - bottom_offset],
#                  [image.shape[1]/2 - dst_size, image.shape[0] - 2*dst_size - bottom_offset],
#                  ])

def color_thresh(img, rgb_thresh=(175, 172, 160)):
    color_select = np.zeros_like(img[:,:,0])
    above_thresh = (img[:,:,0] > rgb_thresh[0]) \
                & (img[:,:,1] > rgb_thresh[1]) \
                & (img[:,:,2] > rgb_thresh[2])
    color_select[above_thresh] = 1
    return color_select

def rover_coords(binary_img):
    ypos, xpos = binary_img.nonzero()
    x_pixel = np.absolute(ypos - binary_img.shape[0]).astype(np.float)
    y_pixel = -(xpos - binary_img.shape[0]).astype(np.float)
    return x_pixel, y_pixel
