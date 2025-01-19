# concatenation 
print('a'+'a'+'a')
# another form of concatenation 
print ('a'*3)
# both prints aaa 
x=10
y=5
print(x,y)
print(y-x) # -5

print(5-2.0) # 3.0
print(x/y ) # 2.0

# power 
print (x**2) #100 

# floor operator
print(x/2.2) # 4.54
print(x//2.2) # 4.0 

#04.01.2025 - python operators 
print(10//3) # 3
print(123//10) #12
print(12//10) #1
# if we have to cut down the last digit,then we have to floor with 10 
# last number will be chopped off 

#modulus operator 
print(10%3) # 1 - gives the remainder 
# x%y = remainder of x/y 
# if x is negative , then it is y - ( x%y) 
print(-10%3) #2 
# if y is negative, the value will be y - (x%y) and change the sign 
print (10%-3) #-2
# if both x and y are negative , then x%y and put the negative sign 
print(-10%-3)

#15.01.2025 
x=2
print(type(x)) # class int will be printed 
x=2.5
print(type(x)) # class float will be printed 
print(float(2.5) ) #2.5
print(int(2.5) ) #2
print(float(2)) #2.0
print(int(2.0)) #2

# integer to string 
x = str(123)
print(x)
print(type(x)) #str type 

#string to int 
x = '123'
print(int(x))
print(type(int(x))) #int type

#x = int('2.4') # this will throw the error 
#print(x)


x=bool(0)
print(x) #false 
x = bool(1)
print(x) # True , any value if it is non zero , then it is true 

x = bool(0.0)
print(x) #false
x=bool(234.343)
print(x) #true 

x = ""
print(bool(x)) # prints false 
x ='2342423'
print(bool(x)) # prints true . any value which is not empty is true 

# input to true or false 
print(bool(int(input()))) # if 0 , false, If it is 1, then it is true 


#logical operator 
print(True and True)
# same for other operators 

#19.01.2025 - Assignment
print((3 + 4) // 2 + 6) # print 9 

a = 10 # change this
b = 5 # change this
c = 6
 # change this

# DO NOT CHANGE THIS
x = a < b + c # + is higher precedence than < operator 

print(x) # this should be True
