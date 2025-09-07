#expenses = [10.5,8,5,15,20,5,3]
expenses = []

# ask for total no of inputs from the user
tol_exp = int(input("Total number of inputs of expenses"))

# loop to take inputs from the user
for x in range(tol_exp):
    expenses.append(float(input("enter the expense:")))
    

print("Expenses you have entered",expenses)

#Calculate the total amount

total = sum(expenses)
print('total amount is $', total , sep = '')