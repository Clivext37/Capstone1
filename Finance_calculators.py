#created by :Clive Mncwango
#on ths day :20/01/2020
#calculating the amount of money accumulated after some year, including interest.

import math
#A = P(1+ R/100)T
#A is the amount of money accumulated after some years,including interest.
#P is the principalb amount
#R is the rate
#T is the time span

print("please choose either 'investment' or 'bond' from the menu below to proceed: ")
print(" ")
print("investment - to calculate the amount of interest you will earn on enterest: ")
print("bond - to calculate the amount you wwil have on a home loan: ")
print(" ")
menu1 = input("please choose either 'investment' or 'bond': ")


#investment calculation

while menu1 == " " or menu1 == "":
    print("you have not entered anything.please either choose between 1 for'investment' or 2 for 'bond': ")
    menu1 = input("please either choose between 1 for'investment' or 2 for 'bond':")


#calculation = int(input(menu))

if menu1.lower() == "investment":

    menu2 = input("Please choose either 'simple' or 'compound' ") 
    #simple_interest = 3
    #compound_interest = 4

    #calculate simple interest
    if menu2.lower() ==  "simple":

        #simple_interest(deposit, interest, year_term):


        principleAmount = float(input("please enter principal amount: "))
        interest = float(input("please enter interest rate: "))
        termInYears = float(input("please enter year term: "))
        interest = interest / 100.0
        #A = P * (1 + r * t)
        final_amount = principleAmount * (1 + interest * termInYears)
        interest = float(final_amount) - principleAmount
        print(f"simple amount is R{final_amount:.2f}")
        print(f"simple interest is R{interest: .2f}")

        #calculating compund interest

    if menu2 == "compound": 

        #compound_interest(principal, rate, year_term):
        
        p = float(input("please enter prinsipal amount: "))
        r = float(input("please enter interest rate: "))
        y = float(input("please enter year term: "))
        # A = P * math.pow((1+r),t)
        

        final_amount = p * ((1 + (r / 100))**y)
        interest = final_amount - p
        print(f"compaund amount acquired in total is R{final_amount:.2f}")
        print(f"compound interest earned is R{interest:.2f}")

        #bond calculation

        #calculation = int(menu2)
if menu1 == "bond":
    bond_repayment = 0.0

    #program calculates the bond repayment according to the figures given

    p = input("please enter the value of the house: ")
    i_new = float(input("please enter the interest rate per month: "))
    n = float(input("please enter the term in months: "))
    i = (i_new / 100.0) / 12
    bond_repayment = float(p)*(i*(1.0 + i)**n) / ((1.0 + i)**n-1.0)
    print(f"bond repayment monthly is R{bond_repayment:.2f}. ")