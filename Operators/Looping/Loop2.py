# print 4 # in a single line 
# for i in range(0,4):
#     print("#",end='')

# print 1 4 7  10 13 16 
# for i in range (1,16,3):
#     print(i)

# continue example 
# for i in range (1,10):
#     if(i==5):
#         continue
#     print(i)
    

# break example 
# for i in range (1,10):
#     if(i==5):
#         break
#     print(i)

# continue + while 
# x =0 
# while (x<5):
#     x+=1
#     if(x==3):
#         break
#     print(x)



#pass example 
# i=0
# while(i<10):
#     pass
#     i+=1

# break + while 
# i=0
# while (i<5):
#     if(i==4):
#         break
#     print(i)
#     i+=1


# continuosly ask the input and stops when the user gives 5 
# counter=0
# while(True):
#     a = int(input())
#     if(a==5):
#         break
#     counter+=1
# print(counter, ' times , input given')

# x=0
# while x<5:
#     x+=1
#     if x==3:
#         break
#     print (x)

# print("Loop finished")

# print matrix grid for the input from the user usingth ewhile loop 


# x =int(input())
# count=0
# while count<x:
#     count1=0
#     while count1<x:
#         print("#",end=" ")
#         count1+=1
#     count+=1
#     print()

# same program using the for loop 

# x =int(input())
# for i in range(0,x):
#     for j in range(0,x):     
#         print("#",end=" ")
#     print()

# program to pring n*m rows 
# x = int(input())
# y = int(input())
# for i in range(0,x):
#     for j in range(0,y):     
#         print("#",end=" ")
#     print()

# program to print two different ranges inside the loop 
# for i in range (2):
#     for j in range(3):
#         print(i,j, end='*')
#     print()

# Prime number which has only two factors, which is 1 and that number itself 
# co prime if we have two numbers and both are prime, then they are co prime numbers 
# in case of two numbers which are co prime, then the GCD is always 1 
# Eg . 3 and 5. For 3  it is 1,3 and for 5 , it is  1 and 5 
# 6,8 --> 6 - 1,2,3,6  8 -> 1 ,2,4,8  ans =2 
# 5,10 --> 5 - 1,5  10 - 1,2,5,10  ans =5 
# at any case highest of GCD is min of two numbers 
# GCD ( A,B)  [1,min(A,B)]
# Program to find all the factors of the given number 
# a = int(input())
# for i in range(1,a+1):
#     if a%i==0:
#         print(i)


# program to find the GCD of two numbers 
# a = int(input())
# b = int(input())
# for i in range (1,min(a,b)+1):
#     if(a%i==0 ) and (b%i==0):
#         print(i)


# program with the decreasing order 
# a = int(input())
# b = int(input())
# for i in range (min(a,b)+1,0,-1):
#     if(a%i==0 ) and (b%i==0):
#         print(i)

#program which prints only the highest number
# a = int(input())
# b = int(input())
# for i in range (min(a,b)+1,0,-1):
#     if(a%i==0 ) and (b%i==0):
#         print('The gcd of ',a,' and ',b,' is ',i)
#         break



# LCM  - least common multiple 
# 2 - 2 4 6 8 , 3 - 3 6 9 12 , Lcm =6 
# 2 , 4 2 - 2 4 6 8 .. 4 - 4 8 12 16 
# Unlike GCD , LCM will not be greater than highest of two numbers 
# LCM(A,B) = Max(a,b), A* B 
# LCM (A,B) = A*B/ HCF ( A,B ) 
# Eg. lcm (5,10) = 5*10/5 = 10 

# a = int(input())
# b = int(input())
# gcd=0

# for i in range (min(a,b)+1,0,-1):
#     if(a%i==0 ) and (b%i==0):
#         print('The gcd of ',a,' and ',b,' is ',i)
#         gcd=i
#         break
# lcm = int((a*b)/i)
# print(lcm)
    
