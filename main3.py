import numpy as np

# Nan and Inf
# print(np.nan) # usefull if the dataset has some empty value so we can put nan there and we can remove them easily
# print(np.inf)

# print(np.isnan(np.nan)) # True
# print(np.isnan(np.sqrt(-1))) #true
# # np.inf is infinity
# print(np.inf + 1) # infinity
# print(np.inf - np.inf) # infinity
# print(np.inf * 0) # infinity



# mathemnetical opearation

# l1=[1,2,3,4,5]
# l2=[6,7,8,9,0]

# a1=np.array(l1)
# a2=np.array(l2)

# # operation
# print(l1 *5) #[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(a1*5) #[5 10 15 20 25]
# print(a1 +a2) #[ 7  9 11 13  5]
# print(a1 -a2) #[-5 -5 -5 -5  5]

# a1 = np.array([1,2,3])
# a2=np.array([[1],
#              [2]])


# print(a1 +a2)
#[[2 3 4]
#  [3 4 5]]

# print(a1 * a2)
# [[1 2 3]
#  [2 4 6]]


# a1 = np.array([1,2,3])
# a2=np.array([[1, 2],
#              [2,4]])

# print(a1 +a2) #error
# print(a1 * a2) #error

a= np.array([[1,2,3],
             [4,5,6]])
# print(np.sqrt(a))
# [[1.         1.41421356 1.73205081]
#  [2.         2.23606798 2.44948974]]

# print(np.sin(a))
# [[ 0.84147098  0.90929743  0.14112001]
#  [-0.7568025  -0.95892427 -0.2794155 ]]





