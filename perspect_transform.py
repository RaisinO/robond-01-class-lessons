def perspect_transform(img, src, dst):

    # Get transform matrix using cv2.getPerspectivTransform()
    M = cv2.getPerspectiveTransform(src, dst)
    # Warp image using cv2.warpPerspective()
    # keep same size as input image
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    # Return the result
    return warped

#dst_size = 5
#bottom_offset = 6
#src = np.float32([[15, 140], [301 ,140],[200, 96], [118, 96]])
#dst = np.float32([[image.shape[1]/2 - dst_size, image.shape[0] - bottom_offset],
#                  [image.shape[1]/2 + dst_size, image.shape[0] - bottom_offset],
#                  [image.shape[1]/2 + dst_size, image.shape[0] - 2*dst_size - bottom_offset],
#                  [image.shape[1]/2 - dst_size, image.shape[0] - 2*dst_size - bottom_offset],
#                  ])
