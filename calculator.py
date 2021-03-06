def calculator():
    #These lines take inputed values from the user and store them in variables
    number_1 = float(float(input('Please enter the first number: ')))
    number_2 = float(float(input('Please enter the second number: ')))
    operation = input('Please type in the math operation you would like to complete:+,-,*,/,//,** ')
    #These conditional statements apply the desired math function
    if operation == "+":
        print(number_1 + number_2)
    elif operation == '-':
        print(number_1 - number_2)
    elif operation == '*':
        print(number_1 * number_2)
    elif operation == '/':
        print(number_1 / number_2)
    elif operation == '//':
        print(number_1 // number_2)
    elif operation == '**':
        print(number_1 ** number_2)
    else:
        print('FALSE')
    #If the input for an operation is invalid, this message will appear
        print('You have not typed a valid operator, please run the program again.')
    input_output()
'''The calculator function takes two numbers and the desired math operation to calculate a solution'''

def input_output():
    calc_again = input('Do you wish to exit?   Please type Y for YES or N for NO.  ')

    if calc_again.upper() == 'N':
        calculator()
    elif calc_again.upper() == 'Y':
        print('See you later.')
    else:
        input_output()

calculator()
''' This function asks if the user wants to calculate another expression, if so it calls on the calculator function'''
