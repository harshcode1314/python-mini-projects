#asking the user for their bank balance 
while True:
    try:
        balance = int(input('What\'s your bank balance? '))
        print('Logged in successfully. ')
        break
    except:
        print('Enter an valid value! ')
        
# making the all function loop
        
while True:
    user_choice = input(f'''
--- ADVANCED SMART ATM ---
Current Balance: {balance}

1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Exit

Choose an option (1-4): 
''')

#deposit feature
    if user_choice == '1':
        try:
            deposited_money = int(input('How much would you like to deposit? '))
            balance += deposited_money
            print(f'Success! ₹{deposited_money} has been added to your account.')        
        except:
            print('Invalid amount!')
            
#withdraw feature
    elif user_choice == '2':
            try:
                withdraw_money = int(input('How much would you like to withdraw? '))
                if withdraw_money > balance:
                    print('Transaction denied! Do not have enough balance.')
                else:
                    balance -= withdraw_money 
                    print('Transaction Approved! Take your cash. ')
            except:
                print('Invalid amount!')
                
# check balance feature
    elif user_choice == '3':
            print(f'Current balance:{balance}₹')
            
#exit feature
    elif user_choice == '4':
          print('Thank you for using the Smart ATM. Goodbye.')
          break
          
    else:
          print('Choose a correct option! ')
          
   
