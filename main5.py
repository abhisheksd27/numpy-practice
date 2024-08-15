import numpy as np

a= np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

# print(a.shape) #(4,5)
# print(a.reshape((5,4)))
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]

# print(a.reshape((20,))) #[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
# print(a.reshape((20,1))) # 20 list with 1 values each in 20 list
# [[ 1]
#  [ 2]
#  [ 3]
#  [ 4]
#  [ 5]
#  [ 6]
#  [ 7]
#  [ 8]
#  [ 9]
#  [10]
#  [11]
#  [12]
#  [13]
#  [14]
#  [15]
#  [16]
#  [17]
#  [18]
#  [19]
#  [20]]

# print(a.reshape((2,2,5))) #main list conatins 2 sub list and each sublist conatins 2 sub sub list and each subsub list conatians the 5 values
# [[[ 1  2  3  4  5]
#   [ 6  7  8  9 10]]

#  [[11 12 13 14 15]
#   [16 17 18 19 20]]]

# a.resize((10,2))
# print(a) # it will rezise the main array no need to reassign to the value


# print(a.flatten()) #[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20] it return the copy of flatten array
# print(a.ravel()) # same as flatten but it return the same array but flatten view
 
 
# var = [v for v in a.flat]
# print(var) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# print(a.transpose())
# [[ 1  6 11 16]
#  [ 2  7 12 17]
#  [ 3  8 13 18]
#  [ 4  9 14 19]
#  [ 5 10 15 20]]

