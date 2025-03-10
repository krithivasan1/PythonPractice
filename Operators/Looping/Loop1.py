#Simple while loop 

# a = 5 
# while(a<10):
#     print(a)
#     a=a+1

# L there is a++ in python, only a-=1

# while loop to print number 10 to 1 
# a=10
# while(a>=1):
#     print(a)
#     a-=1

#Print all the even number with while and if 
# a=1
# while(a<50):
#     if(a%2==0):
#         print(a)
#     a+=1

# print all the even number with while and  without if 
# a=0
# while(a<50):
#     print(a)
#     a+=2


#Print all the odd number with while and if 
# a=1
# while(a<50):
#     if(a%2!=0):
#         print(a)
#     a+=1

# print all the odd  number with while and  without if 
# a=1
# while(a<50):
#     print(a)
#     a+=2

#L print ( content , sep, end ) 
# printing with seperator 
# print("a","b","c",sep="$")
#output a$b$c



#L printing on the same line 
# print("a","b","c",end="$")
# print("e","F")
# Output - a b c$e F

#L print ( content , sep, end ) 
# printing with seperator 
# print("a","b","c",sep="\n")
# output:
# a
# b
# c

# printing the table 
# a=5
# while(a<=50):
#     print(a)
#     a+=5

# printing the table after getting the input 
# a=int(input())
# start = a
# while(start <=a*10):
#     print(start)
#     start+=a

# print the table get the input , and printing those tables 

# n = int(input())
# start = 1
# while(start<=n):
#     tableNum = int(input())
#     start1 = tableNum
#     while(start1<=10*tableNum):
#         print(start1)
#         start1+=tableNum

#     start+=1

# range(a,b)
# a to b 
# inclusive of a and exclusive of b 
# range(start,end, jump)
# range (2,10,-1) - Invalid 
# range(5,5) - default jump is 1 and the list is empty 



# print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(list(range(2,10)))
# [2, 3, 4, 5, 6, 7, 8, 9]

# print(list(range(2,10,2)))
# [2, 4, 6, 8]

# for i in range(1,10,1):
#     print(i)
# no need to increment, for loop will be taking care of it 

# printing first 10 natural numbers 
# for i in range (1,11):
#     print(i)

# total , get the first 10 natural number and print the total 
# total =0
# for i in range(1,11):
#     total +=i

# print(total)
#55

# print(list(range(10,1,-1)))
# [10, 9, 8, 7, 6, 5, 4, 3, 2]

# get the input and print reverse
# n =int(input())
# print(list(range(n,0,-1)))

# even number using if and range
# for i in range(1,10):
#     if(i%2==0):
#         print(i) 

# even number using jump and not if 
# for i in range(0,11,2):
#     print(i)

# odd number using if and range
# for i in range(1,10):
#     if(i%2!=0):
#         print(i) 

# odd  number using jump and not if 
# for i in range(1,11,2):
#     print(i)

# program to print all the even numbers from 1 to N 
# N has to take from input 
# n = int(input())
# for i in range(0,n,2):
#     print(i)


# program to print perfect square from the given input 

# a = int(input())
# for i in range(1,a):
#     if(i**2<=a):
#         print(i**2)

# Assignement 
# for i in range(-6, -10, -1):
#      print(i, end =" ")

#summation 
# a = int(input())
# total =0
# for i in range(1,a+1):
#     total +=i

# print(total)

# program to find the exponent 
# num=16
# base=4
# cnt=0
# while(num>1):
#   num/=base
#   cnt+=1
# print(cnt)

# a = int(input())
# start =1
# while(start<=a):
#     b = int(input())
#     count=1
#     while(b>9):
#         count+=1
#         b=b/10
#     print(count)
#     start+=1


# a =0
# while True:
#     a=a+2
#     print('1',a)
#     a%=5
#     print('2',a)
#     a+=1
#     print('3',a)
#     if(a==5):
#         break
# print (a)


# x = int(input())
# y = int(input())

# q = 0
# r = 0
# while x >= y:
#     x -= y
#     q += 1
# print(q, r)

n =int(input())
for i in range(0,n):
    print('*',end="")