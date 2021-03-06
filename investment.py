def calculate_apr():
    print("This function calculates the future value")
    #The following three line take the input from the user
    principal = int(input("Enter the initial principal: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))
    
    for i in range(years):
    #This loop will repeat for the amount of years input by the user
        principal = principal * (1 + interest_rate)
    print("The future value is:", principal)
calculate_apr()
''' This function takes the inputed values from the user for principal, interest rate and years to calculate the amount made on an investment'''
