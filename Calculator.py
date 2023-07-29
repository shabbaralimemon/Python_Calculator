num_1 = int(input("Enter the first number : "))
num_2 = int(input("Enter the second number : "))
operator = input("Enter the operator to perform the task : ")
if operator == '+':
    print("Addition of",num_1,"and",num_2,"is equal to : ",num_1+num_2)
elif operator == '-':
    print("Subtraction of",num_1,"and",num_2,"is equall to : ",num_1-num_2)
elif operator == '*':
    print("Multiplication of",num_1,"and",num_2,"is equall to :",num_1*num_2)
elif operator == '/':
    print("Division of",num_1,"and",num_2,"is equall to :",num_1/num_2)
else:
    print("Kindly Enter the wright operator ! +,-.*,/")
print("Thanks !")