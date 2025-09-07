# get details of loan
money_own = float(input("how much money have you taken: \n"))
percent = float(input("enter the rate \n"))
payment = float(input("How much do you pay each month \n"))
months = int(input("months for the result \n"))

monthly_rate = percent/100/12

for i in range(months):
    ####
    #Calculate interest to pay
    interest_paid = money_own * monthly_rate

    #Add in interest
    money_own = money_own + interest_paid

    if (money_own - payment< 0):
        print('The last payment is:', money_own)
        print('you paid off the loan in:', i+1, 'months')
        break

    #Make payment
    money_own = money_own - payment

    print("paid", payment, 'of which' , interest_paid, 'was interest', end = ' ')
    print('Now i owed', money_own)


