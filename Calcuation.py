print("===================\n")
print("Arithmatic calculator \n")
print("======================\n")
print("1. Addition \n")
print("2.substraction\n")
print("3.division\n")
print("4.Multiplication\n")
print("5.Reminder\n")
print("6.Floor Division\n")
print("7.Continue\n")
print("8.Exit\n")
print("============\n")
print("Please select your choice")
print("====================\n")

while True :
    fn = int(input("enter your first number :"))
    sn = int(input("enter your second number :"))
    Choice = input("enter your Choice\n")
    res=0
    if Choice =='1':
        res = fn+sn
        print("sum of {0}{1}".format(fn,sn),res)
    elif Choice =='2':
        res = fn-sn
        print("substraction of {0} {1}=".format(fn,sn),res)
    elif Choice == '3':
        res = fn/sn
        print("divison of {0} {1}=".format(fn,sn),res)
    elif Choice == '4':
        res = fn*sn 
        print("Multiplication of {0} {1}=".format(fn,sn),res)
    elif Choice == '5':
        res = fn%sn
        print("Reminder of {0} {1}=".format(fn,sn),res)
    elif Choice =='6':
        res = fn//sn 
        print("floor division of {0} {1}=".format(fn,sn),res)
    elif Choice == '7':
        print('continue...')
    elif Choice == '8':
        print("***exit****") 
    else :
        print("invalid choice")
        def calcuation(a,b):
            addition=a+b
            mul=a*b
            sub=a-b 
            div=a/b
print("addition")
print("mul")
print("sub")
print("div")
x=int(input("Enter the first number \n"))
y=int(input("enter the second number \n"))
calculation(x,y)
  
