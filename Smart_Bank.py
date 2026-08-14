#making a function to ask user about his current balance
def ask_balance():
    while True:
        try:
            balance = float(input('Whats your current balance? '))
            if balance < 0:
                print('Negative value is not allowed! ')
                continue
            else: 
                print('Logged in successfully.')
            break
        except ValueError:
            print('Enter a valid amount! ')
    return balance
            
            
#making a function to deposit money in the balance

def deposit_money(current_balance):
    while True:
        try:
            amount_to_deposit = float(input('How much would you like to deposit? '))
            if amount_to_deposit <= 0:
                print('0 or neagtive amount is not allowed! ')
            else:
                current_balance += amount_to_deposit
                print(f'Success! ₹{amount_to_deposit} has been added to your account.')
                break
            
        except ValueError:
            print('Invalid amount! ')
    return current_balance, amount_to_deposit

# making a function to withdraw money from the account   
        
def withdraw_money(current_balance):
    while True:
        try:
            amount_to_withdraw = float(input('How much would you like to withdraw? '))
            if amount_to_withdraw > current_balance or amount_to_withdraw < 0 :
                print('Transaction denied! Invalid amount for your account.')
                choice = input('Want to exit to the main menu(y/n)').lower().strip()
                if choice == 'y':
                    amount_to_withdraw = 0
                    break
            else:
                current_balance -= amount_to_withdraw
                print('Transaction Approved! Take your cash.')                   
                break
        except ValueError:
            print('Invalid amount!')
    return current_balance, amount_to_withdraw
    
    
    
# making a function to show the current balance 

def show_balance(current_balance):
    print(f'Current balance:{current_balance}₹')

# making a function to add transactions in the list transactions    
        
def add_transaction(transactions,amount,transaction_type):
    transaction_type = transaction_type.lower().strip()
    if amount == 0:
        print('')
    else:
        
        if transaction_type == 'deposit':
            transactions.append(f"You deposited ₹{amount} into your account.")
        elif transaction_type == 'withdrawal':
            transactions.append(f"You withdrew ₹{amount} from your account.")
        
        
    return transactions
    
# making a function to show history

def show_history(history):
    print('''
======= TRANSACTION HISTORY =======
''')
    for transaction in history:
        print(f'>>> {transaction}')
    print('''
===================================
''')

# making the main manager function

def main():
    current_balance = ask_balance()
    history = []
    
    while True:
        user_choice = input(f'''
--- ADVANCED SMART ATM ---
Current Balance: ₹{current_balance}

1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Show History
5. Exit

Choose an option (1-5): 
''')
        if user_choice == '1':
            current_balance, amount = deposit_money(current_balance)
            history = add_transaction(history,amount,'deposit')
            
        elif user_choice == '2':
            current_balance,amount = withdraw_money(current_balance)
            history = add_transaction(history,amount,'withdrawal')
            
        elif user_choice == '3':
            show_balance(current_balance)
            
        elif user_choice == '4':
            show_history(history)
            
        elif user_choice == '5':
            print('Thank you for using the Smart ATM. Goodbye.')
            break
        else:
            print('Choose a valid option')
           
    
main()

        
        
        
        