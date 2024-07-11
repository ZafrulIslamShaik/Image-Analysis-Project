import numpy as np
# function for template matching
def template_matching_NCC (src, temp):
    # obtaining the height and width of the image
    h_src, w_src = src.shape
    # obtaining the height and width of the template
    ht_temp, wt_temp = temp.shape
    # array for storing the differences
    diff = np.empty((h_src - ht_temp, w_src - wt_temp))
    src = np.array(src, dtype="float")
    temp = np.array(temp, dtype="float")
    # searching for template in the image
    for dy in range(0, h_src - ht_temp):
        for dx in range(0, w_src - wt_temp):
            # for obtaining absolute sum of differences
            r_o_i = src[dy:dy + ht_temp, dx:dx + wt_temp]
            numerator = np.sum(r_o_i * temp)
            denominator = np.sqrt((np.sum(r_o_i ** 2))) * np.sqrt(np.sum(temp ** 2))
            if denominator == 0 : diff[dy, dx] = 0
            diff[dy, dx] = numerator / denominator

    # returns the searched position with the lowest difference
    pt = np.unravel_index(diff.argmax(), diff.shape)
    return (pt[1], pt[0])