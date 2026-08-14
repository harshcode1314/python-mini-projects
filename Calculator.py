print('''
=============== CALCULATOR==============

''')
first_number = int(input('Give the first number: '))
operator = input('Give the operator( +, -, * or /):')
second_number = int(input('''Give the second number: 
'''))

if operator == '+':
    result = first_number + second_number 
    print('''
Result:''', result)

elif operator == '-':
    result = first_number - second_number 
    print('''
Result:''', result)

elif operator == '*':
    result = first_number * second_number 
    print('''
Result:''', result)

elif operator == '/':
    result = first_number / second_number 
    print('''
Result:''', result
)

else:
    print('-> Please choose a correct operator!')
    
print('=====Thanks for testing the program=====')