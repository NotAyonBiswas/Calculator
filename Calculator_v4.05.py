
def num_check(num):   #checks if the input is a number or not.
    valid= False
    while valid== False:
        try:
            num= float(num) or num== int(num)
            valid= True
        except:
            num= input("Please enter a number:")
            print()
            continue
    return num

def cal_logic_single(optype, op, num):   #logic of single number operations. optype gives specific list of operation. Operation gives number specified for certain operation mentioned in the operation list and num gives the input.
    print("You've chosen",optype[int(op)-1],"operation\n")
    if int(op)==1: #Sin(x)
        print(f"Sin({num}°)= {math.sin(math.radians(num)):.3f}\n")
    elif int(op)==2:    #Cos(x)
        print(f"Cos({num}°)= {math.cos(math.radians(num)):.3f}\n")
    elif int(op)==3: #Tan(x)
        print(f"Tan({num}°)= {math.tan(math.radians(num)):.3f}\n")
    elif int(op)==4:  #Cosec(x)
        print(f"Sin({num}°)= {1/math.sin(math.radians(num)):.3f}\n")
    elif int(op)==5:    #Sec(x)
        print(f"Sec({num}°)= {1/math.cos(math.radians(num)):.3f}\n")
    elif int(op)==6:    #Cot(x)
        print(f"Sin({num}°)= {1/math.tan(math.radians(num)):.3f}\n")
    elif int(op)==7:
        print(f"Factrial of {num}!= {math.factorial(int(num)):.3f}\n")
    else:
        print(f"Gamma({num})= {(math.gamma(num)):.3f}\n")
    return op, num

def cal_logic_multi(optype, op,num1,num2): #Logic of multi number operations.
    print ("You've chosen",optype[int(op)-1],"operation.\n")
    if int(op)==1:  #addition
        print(f"{num1}+{num2}= {num1+num2}\n")
    elif int(op)==2:    #Subtraction
        print(f"{num1}-{num2}= {num1-num2}\n")
    elif int(op)==3:    #multiplication
        print(f"{num1}*{num2}= {round(num1*num2,3)}\n")
    elif int(op)==4:    #division
        print(f"{num1}/{num2}= {round(num1/num2,3)}\n")
    elif int(op)==5:    #power
        print(f"{num1}^{num2}= {round(math.pow(num1,num2),3)}\n")
    elif int(op)==6:   #logarithm
        print(f"The log(base{num2}) of {num1}= {round(math.log(num1,num2),3)}\n")
    elif int(op)==7:   #logarithm
        print(f"{num1} Perm {num2}= {math.perm(int(num1),int(num2))}\n")
    else:   #logarithm
        print(f"{num1} Comb {num2}= {math.comb(int(num1),int(num2))}\n")
    return op, num1, num2

def showables(lst): #Prints necessery info- version number, operations list etc.
    print()
    [print(i, end=" ") for i in lst]
    print(),print()
    print("""If operation number given is more than the listed number then the last operation will be performed by the calculator or if a number with decimal is entered then only the intiger part of the number will be considered.\n""")
    return lst

while True: #Main menue of calculator.
    operation_list1 = ("1: Sin(x°)", "2: Cos(x°)", "3: Tan(x°)", "4: Sec(x°)", "5: Cosec(x°)", "6: Cot(x°)", "7: Factorial(x!)", "8: Gamma(x)")
    operation_list2 = ("1: Addition","2: Subtraction","3: Multiplication", "4: Division", "5: Power (x^y)", "6: Log(X,Y)", "7: Permutation(nPk)(n>k)", "8: Combination (nCk)(n>k)")
    print("Calculator v4.05\n")
    choice_list= ["1: Single entity operations","2: Multiple entity operations","3: Exit"]
    [print(i) for i in choice_list]
    choice= num_check(input("Please enter choice (1 to 3): "))
    print()
    if choice==1:
        import math
        showables(operation_list1)
        operation= num_check(input("Please enter the number of operation: "))
        num= num_check(input("Please enter the number: "))
        cal_logic_single(operation_list1, operation, num)
        continue
    elif choice==2:
        import math
        showables(operation_list2)
        operation= num_check(input("Please enter the number of operation: "))
        num1= num_check(input("Please enter the first number: "))
        num2= num_check(input("please enter the second number: "))
        cal_logic_multi(operation_list2, operation, num1, num2)
        continue
    else:
        print("You have exited from calculator v4.05\n")
        break