# defining a function to print the roster values im a good manner

def show_roster(roster):
    roster_size = len(roster)
    if roster_size > 0:
        print('''
--- CURRENT ROSTER ---
''')
        for index in range(roster_size):
            print(index+1,roster[index])
    else:
        print("The roster is currently empty! Time to draw some stick men."
)

#making a function to add a character name in the roster

def add_character(roster):
    character_name = input("Enter the name of the new character: "
).strip()
    roster.append(character_name)
    print("Character added successfully!"
)
    return roster
 
 # defining a function to remove a character name in the roster
 

def remove_character(roster):
    while True:
        character_name = input("Enter the name of the character to erase: "
).strip()
        if character_name == 'exit':
            break
        try:
            roster.remove(character_name)
            print("Character erased from the roster." 
)
            break    
        except ValueError:
            print("Wait! That character is not in the roster.(Type exit to go to the main menu.)"
)
            
    return roster
    
# defining the main loop function 

def main():
    roster = []
    while True:
        user_choice = input('''
--- STICK MAN MANGA ROSTER ---
Choose an option:
1. View Roster
2. Add a Character
3. Remove a Character
4. Exit

Choice: '''
).strip()
        if user_choice == '1':
            show_roster(roster) 
        elif user_choice == '2':
            roster = add_character(roster)
        elif user_choice == '3':
            roster = remove_character(roster)
        elif user_choice == '4':
            print("Closing the manga roster... Goodbye!"
)
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4."
)
            
            
main()                                   
    

    
