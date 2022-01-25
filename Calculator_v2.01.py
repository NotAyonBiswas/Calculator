
#Dynamic Simple Calculator- Goal 2
import math
print()
print("Calculator v2.02")
print()
operation_list = ("1: Addition","2: Subtraction","3: Multiplication",
                  "4: Division", "5: Power (x^y)","6: Log(X,Y)")
print(operation_list)
print()

#Asks for operation type and digits to operate on.
operation= int(input("Please enter the number of operation: "))
print()
num1= float(input("Please enter the first number: "))
print()
num2= float(input("please enter the second number: "))
print()

#Main codeblock
if int(operation)==1:
    print ("The addition of,",num1,"and",num2,"is",str(num1+num2)+".")
    print()
elif int(operation)==2:
    print ("The subtraction of,",num1,"and",num2,"is",str(num1-num2)+".")
    print()
elif int(operation)==3:
    print ("The multiplication of,",num1,"and",num2,"is",str(round(num1*num2),3)+".")
    print()
elif int(operation)==4:
    print ("The division of,",num1,"and",num2,"is",str(round(num1/num2),3)+".")
    print()
elif int(operation)==5:
    print (num1,"to the power of",num2,"is",str(round(math.pow(num1,num2),3))+".")
    print()
else:
    print ("The logarithm of,",num1,"with base",num2,"is",str(round(math.log(num1,num2),3))+".")
    print()