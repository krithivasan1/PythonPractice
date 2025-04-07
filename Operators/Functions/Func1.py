# sample function 
# def fruits_shake(fruit):
#     print ('Peel',fruit)
#     print('add milk')
#     print('Mixie it ')

# fruits_shake('banana')

# fruits_shake('Chiku')

# def family_intro(father,mother,sibling):
#     print('father',father)
#     print('mother',mother)
#     print('sibling',sibling)

# family_intro('ks','sp','sk')

"""
this is the doc string for the calculator 
"""
# def calculator(a,b):
#     print('add',(a+b))
#     print('sub',(a-b))
#     print('Multi',(a*b))
#     print('div',a/b)

# calculator(10,2)


# add function with return 

# def add(a,b):

#     print("This will be printed since it is before return ")
#     return a+b
#     print("This will not be printed since it is after the return ")
# x = add(5,10)
# print(x)

# if it is not returning then None will be printed 
# none is also a data type 

#----
# returning multiple values 
# def fun1(a,b,c):
#     return a,b,c

# x,y,z =fun1(1,3,4)
# print(x)
# print(y)
# print(z)

# This is tuple - x,y,z

#----
# Keyword based argument 
# def family_members(father,mother,sibling):
#     print('father is ',father)
#     print('mother is ',mother)
#     print('sibling is ',sibling)

# family_members("dad","mom","sibling")
# #Prints as expected, we have giventhe positional arguments 
# family_members("dad1",sibling="sibling1", mother="mom1")
# # positional should be first then keyword based argument should follow 
# # if positional first, keyword can be given on any order 
# # Position, Keyword - Right 
# # Keyword, Position - wrong 

#--- 
# def kingdom():
#     king="Rahul"
#     print(king)

# kingdom()
# # output : Rahul . 

#-- 
# king ="Global King"
# def kingdom():
#     global king
#     king="Rahul"
#     print(king)

# print(king) # Global King 
# kingdom() # Rahul 
# print(king) # Rahul 
# # output : Rahul .
# # # It will overwrite the value in local 

#----
# Lambda one liner function 
# def random(x):
#     return x+10

# print(random(10))

# #lambda representation 
# random1 = lambda x:(x+10)
# print(random1(5))
# #another way to call the lambda function 
# print((lambda x:x+23)(5))

#(lambda :print("hello scaler"))("Scaler")
# it will show the error , since we don't have any arguments 
# but we are passing arguments 

# func = lambda x : x+10
# print(func(2))



# no reference to call this function 
lambda :print("Hello Scaler")



