import numpy as np

# a = np.array([1,2,3,4,5])
# print(a)
# print(type(a))
# a_mul = np.array([[[1,2,3] , [4,5,6]] , [[1,1,1] ,[2,3,4]]])
# # print(a_mul[1])
# print(a_mul.shape) #shape
# print(a_mul.ndim) #depth 
# print(a_mul.size) # total number of elements
# print(a_mul.dtype) #int32



# a = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [2,"5", 6], # if the string is "hello it does not work when we specify the datatype"
#     [7,8,9] 
# ], dtype =np.int32)

# print(a.dtype) #u11 -> a string data type
# print(a[0][0]) #1
# print(type(a[0][0])) #<class 'numpy.str_'>
# # if any 1 value in list contains str value then all the value becomes string and list type becomes U11
# # we can specify the dta type in list 
# # if the string which is a charecter then it will give error but it  works is a number which is as a string :- "5" will converted into int32
# print(a[1,1]) # it wil print 5




# d={
#     "1": "A"
# }

# b = np.array([
#     [1,2,3],
#     [4,d,6],
#     [7,8,9],
#     [2,"Hello", 6], 
#     [7,8,9] 
# ])

# print(b.dtype) #object  -> if the array conatine any non primitive datatypes it becomes object
# print(b[1,1])
# print(type(b[1,1])) #dict
# print(type(b[1,0]))  #INT


# c=np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [2,7, 6], 
#     [7,8,9]
# ] , dtype="<U2")

# print(c.dtype) # U7 or U2 anything this is basically a string





