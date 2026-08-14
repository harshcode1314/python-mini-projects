#asking user for their win % and rating
while True:
    try:
        win_percentage = int(input('What is your current win percentage? '))
        current_rating = int(input('What is your current chess rating? '))
        break
    except:
        print('Enter an valid value! ')
#checking whether the user is qualified fir the chess tournament or not and gving result to the user

if current_rating > 0:
    if win_percentage >= 75 or current_rating >= 1500:
        print("You Qualify!")
        
    else:
        print("You Do Not Qualify!")
        
else:
    print('Player with 0 rating are strictly not allowed in the tournament')
    
