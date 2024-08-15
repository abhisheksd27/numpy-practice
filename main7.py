import numpy as np

# number = np.random.randint(100)
# print(number)

# numbers = np.random.randint(100 , size=(2,3,4))
# print(numbers)
# [[[80 76 24 59]
#   [88 30 10  7]
#   [ 4 99 64 20]]

#  [[97 35 28 97]
#   [96 66 19 97]
#   [42 19 55 75]]]


# numbers = np.random.randint(80,100 , size=(2,3,4))
# print(numbers)
# [[[95 98 85 98]
#   [99 95 89 98]
#   [96 82 94 83]]

#  [[90 93 90 83]
#   [92 93 90 85]
#   [90 93 86 92]]]


# numbers = np.random.binomial(10, p=0.5, size=(5,10))
# print(numbers)
# [[6 5 4 4 5 8 5 4 7 5]
#  [6 6 6 4 7 4 4 5 6 3]
#  [6 4 3 5 6 8 4 7 7 7]
#  [4 4 5 6 4 4 8 5 4 5]
#  [6 3 5 6 3 3 5 4 7 6]]


# numbers = np.random.choice([1,2,3,4,5],size=(5,10))
# print(numbers)
# [[3 5 5 3 3 2 3 1 1 3]
#  [2 5 1 5 2 3 5 3 5 5]
#  [1 5 2 3 3 2 5 3 1 4]
#  [5 4 4 1 3 4 3 4 5 2]
#  [2 3 3 2 2 5 5 4 3 1]]

# import and export


# b = np.array(
#     [
#         [1,2,3,4,5,21],
#         [6,7,8,9,10,22],
#         [11,12,13,14,15,23],
#         [16,17,18,19,20,24]
#     ]
# )

# np.save("myarray.npy" ,b)


# a= np.load("myarray.npy")
# print(a)


# np.savetxt("a.csv" ,b ,delimiter=",")

# a= np.loadtxt("a.csv" , delimiter=",")
# print(a)