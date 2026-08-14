
# making fuction to ask user about the last game result and check if the user has given right input or not 

def ask_result(question):
    while True:
        answer = input(question).strip().lower()
        if answer != 'w' and answer != 'l' and answer != 'd':
            print('Give the result in W/L/D')
            
        else:
            break
            
    return answer
    
# making a function to decide what the user has given from w ,l and d and updating the wins , losses and draw variable as per user input

def update_stats(result, wins, losses,draws):
    if result == 'w':
        wins += 1
    elif result == 'l':
        losses += 1
    elif result == 'd':
        draws += 1
     
    return wins, losses, draws
    
# making a fuction to calculate the win % of the user by taking total wins and total games played 

def get_win_percent(wins,total_games):
    try:
        win_percent = str(round((wins/total_games)*100))
        return win_percent +'%'
    except ZeroDivisionError:
        return 'No win percent yet'

# making the main loop function


def main():
    # making four variables for wins , losses draws and total games played
    wins = 0
    losses = 0
    draws = 0
    total_games = 0
    
    while True:
        choice = input('''
--- CHESS PERFORMANCE TRACKER ---
Choose an option:
1. Log a Match
2. View Performance Stats
3. Exit 

'''
).strip()
        if choice == '1':
            result = ask_result("Enter match result (W for Win, L for Loss, D for Draw): "
)
            wins, losses, draws  = update_stats(result,wins, losses,draws)
        
        elif choice == '2':
            total_games = wins + losses + draws
            win_percent= get_win_percent(wins, total_games)
            print(f'''
--- CURRENT STATS ---
Total Games Played: {total_games}
Record: {wins} Wins, {losses} Losses, {draws} Draws
Win Percentage: {win_percent}
---------------------
''')
        elif choice == '3':
            print("Thanks for using the Chess Tracker. Goodbye!"
)
            break
        else:
            print('Choose an valid option from 1/2/3.')
            
main()

     