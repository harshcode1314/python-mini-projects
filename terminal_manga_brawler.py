import time

#The story's main characters and thier stats database

roster = {
    # The Protagonists (Balanced stats for standard combat)
    "Hero": {"HP": 120, "ATK": 80, "SPD": 50},
    "Mentor": {"HP": 80, "ATK": 40, "SPD": 60},
    "Rival": {"HP": 115, "ATK": 85, "SPD": 55},
    
    # The Speedsters (Low HP, High ATK, Extreme SPD)
    "Hidden Ninja": {"HP": 90, "ATK": 75, "SPD": 90},
    "Wind Runner": {"HP": 70, "ATK": 60, "SPD": 95},
    "Shadow Assassin": {"HP": 65, "ATK": 95, "SPD": 100},
    
    # The Tanks (Massive HP, Medium ATK, Terrible SPD)
    "Iron Golem": {"HP": 250, "ATK": 45, "SPD": 15},
    "Juggernaut": {"HP": 300, "ATK": 60, "SPD": 25},
    "Shield Master": {"HP": 220, "ATK": 35, "SPD": 30},
    
    # The Fodder (Extremely weak enemies for testing)
    "Grunt": {"HP": 45, "ATK": 10, "SPD": 20},
    "Training Dummy": {"HP": 100, "ATK": 0, "SPD": 1},
    "Goblin Scout": {"HP": 30, "ATK": 15, "SPD": 45},
    
    # The Glass Cannons (Low HP, Massive ATK)
    "Elementalist": {"HP": 75, "ATK": 90, "SPD": 65},
    "Sniper": {"HP": 50, "ATK": 100, "SPD": 70},
    
    # The Bosses (Overpowered stats across the board)
    "Shadow Boss": {"HP": 250, "ATK": 55, "SPD": 45},
    "Demon Lord": {"HP": 400, "ATK": 85, "SPD": 60},
    "Fallen Angel": {"HP": 350, "ATK": 95, "SPD": 85},
    "God Of Destruction": {"HP": 500, "ATK": 100, "SPD": 80}
}

# Defining a function to show the full roster to the user in a user friedly way


def show_roster(roster):
    if not roster:
        print('''
No character has been added in the roster yet.
        ''')
    for name,stats in roster.items():
        print(f"{name:<15} | HP: {stats['HP']:<3} | ATK: {stats['ATK']:<3} | SPD: {stats['SPD']:<3}")
        
        
#defining a function to get a stat and to check whether it is in the limit and is in valid fromat or not


def get_stat(limit,question='Give the stat points for the character: '):
    while True:
        try: 
            stat_points = int(input(question))
            if stat_points > limit:
                print(f'It is more than the limit({limit})!')
            elif stat_points <1:
                print('The stat points must be higher than 0.')
            
            else:
                return stat_points
        except ValueError:
            print('Give a positive whole number!(Decimals are not allowed.) ')
   
# Defining a function to add a character in the roster

def add_character(roster):
    name = input('Give tha name of the character you want to add in the roster: ').strip().title()
    
    HP,ATK,SPD = get_stat(300,f'What is the health of {name}: '),get_stat(100,f'What is the attack of {name}: '),get_stat(100,f'What is the reaction speed of {name}:')
    
    roster.update({name: {'HP': HP,'ATK':ATK,'SPD':SPD}})
    print(f'{name} added successfully!')
    
# defining a function to ask user for the character for fight for the battle mechanic and checking whether it is in the roster or not

def get_character(roster,question='Give the character name: '):
    while True:
        character = input(question).strip().title()
        if character in roster.keys():
            break
        else:
            print('Given character is not in the roster, ')
            print(f"{'-'*5}CURRENT ROSTER{'-'*5}")
            show_roster(roster)
    return character
        
#defining a function to conduct battle between two characters from the roster

def battle(roster_f):
    character1 = get_character(roster_f,'Give the name of the first character from the roster to battle: ')
    character2 = get_character(roster_f,f'Give the name of the second character from the roster that will fight against {character1}: ')
    
#checking that who will get first chance to attack by comparing both character's SPD stat

    if roster_f[character1]['SPD'] > roster[character2]['SPD']:
        attacker = character1
        defender= character2
    elif roster_f[character1]['SPD'] < roster[character2]['SPD']:
        attacker = character2
        defender= character1
    else:
        attacker = character1
        defender= character2
        
#extracting both character's hp
    attacker_hp = roster_f[attacker]['HP']
    defender_hp = roster_f[defender]['HP']

        
# The main fighting mechanic  
      
    print(f'''
{'-'*5}BATTLE STARTS!{'-'*5}
''')                
    while True:
        defender_hp -= roster_f[attacker]['ATK']
                        
        print(f'{attacker} strikes {defender} for', roster_f[attacker]['ATK'],'damage!')
        
        if defender_hp <= 0:
            print(f'>>>{defender} lost as his health became 0.')
            break
        else:
            print(f'{defender}\'s HP drops to {defender_hp}.')
        print('-'*20)
        time.sleep(1)
        attacker,defender = defender,attacker
        attacker_hp,defender_hp= defender_hp,attacker_hp
        

    
#defining the main manager function 

def main(roster):
    while True:
        user_choice = input('''
       === STICKMAN MANGA ENGINE ===
1. View Roster
2. Add New Character
3. Simulate Battle
4. Clear the roster
5. Exit
Select an option (1-5): ''').strip()
        if user_choice == '1':
            show_roster(roster)
        elif user_choice == '2':
            add_character(roster)
        elif user_choice == '3':
            battle(roster)
        elif user_choice == '4':
            roster.clear()
        elif user_choice == '5':
            print('Thank you for testing the program! Have a nice day!')
            break
        else:
            print('Choose a valid option!')
        
        
main(roster)
    

