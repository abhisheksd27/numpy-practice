import numpy as np

# concatenating , stacking and splitting

a1 = np.array(
    [
        [1,2,3,4,5],[6,7,8,9,10]
    ]
    
)


a2= np.array(
    [
        [11,12,13,14,15],[16,17,18,19,20]
    ]
)


# a= np.concatenate((a1,a2), axis=0)  # row
# print(a)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

# a= np.concatenate((a1,a2), axis=1) #column
# print(a)
# [[ 1  2  3  4  5 11 12 13 14 15]
#  [ 6  7  8  9 10 16 17 18 19 20]]



# a= np.stack((a1,a2))
# print(a)
# [[[ 1  2  3  4  5]
#   [ 6  7  8  9 10]]

#  [[11 12 13 14 15]
#   [16 17 18 19 20]]]

# a= np.vstack((a1,a2))
# print(a)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

# a= np.hstack((a1,a2))
# print(a)
# [[ 1  2  3  4  5 11 12 13 14 15]
#  [ 6  7  8  9 10 16 17 18 19 20]]


# split
b = np.array(
    [
        [1,2,3,4,5,21],
        [6,7,8,9,10,22],
        [11,12,13,14,15,23],
        [16,17,18,19,20,24]
    ]
)

# print(np.split(b, 2 , axis=0))
# [array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10]]), array([[11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20]])]

# print(np.split(b, 2 , axis=1)) 
# [array([[ 1,  2,  3],
#        [ 6,  7,  8],
#        [11, 12, 13],
#        [16, 17, 18]]), 
# 
# array([[ 4,  5, 21],
#        [ 9, 10, 22],
#        [14, 15, 23],
#        [19, 20, 24]])]


# print(b.min())
# print(b.max())
# print(b.mean())
# print(b.std())
# print(b.sum())
# print(np.median(b))


