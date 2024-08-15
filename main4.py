import numpy as np

# Array methods
# a= np.array([1,2,3])

# np.append(a, [7,8,9])
# print(np.append(a, [7,8,9]))# [1 2 3 7 8 9]
# print(a) #[1,2,3]

# a=np.append(a, [7,8,9])
# print(a) #[1 2 3 7 8 9]


# a= np.insert(a, 3 , [4,5,6]) # 3rd index insert ther array
# print(a) #[1 2 3 4 5 6 7 8 9]


a= np.array([
    [1,2,3],
    [4,5,6]
])


# print(np.delete(a,1)) # delete 2
# print(np.delete(a,3)) #delet 4
# print(np.delete(a,4)) # delete 5

# print(np.delete(a,1,0)) # it will delet whole 2nd row -> [[1 2 3]]
# print(np.delete(a,0,0)) #[[4 5 6]]


print(np.delete(a,1 ,1)) # delet index 1 column
# [[1 3]
#  [4 6]]