# defining the fuction to handle user mistakes, giving wrong value for area

def get_num(question):
    while True:
        try:
            answer = float(input(question))
            break
            
        except ValueError:
            print('Give a real number!!')
    return answer


# defining triangle area function

def area_of_triangle():
    height = get_num('Give the height: ')
    base = get_num("Give the base length: ")
            
    area = (height*base)/2
    return area
    
#defining square area fuction 
   
def area_of_sqaure():
    side = get_num('Give the length of the side: ')         
    area = side*side
    return area
    
#defining parallelogram area function 

def area_of_para():
    height = get_num('Give the height: ')
    base = get_num('Give the lenght of base: ')
    area = height*base
    return area 
    
# defining Rhombus area function

def area_of_rhombus():
    diagonal1 = get_num('Give the length of the first diagonal: ')
    diagonal2  = get_num('Give the length of the second diagonal: ')
            
    area = (diagonal1*diagonal2)/2
    return area
            
            
# defining main loop fuction    
    
def main():
    while True:
        choice = input('''
Welcome to easy math application.
Choose any following option:-
1. Area of Triangle
2. Area of Sqaure
3. Area of Parallelogram
4. Area of Rhombus
5. Exit
''').strip()
                    
        if choice == '1':
            area = area_of_triangle()
            shape = 'Triangle' 
            
        elif choice == '2':
            area = area_of_sqaure()
            shape = 'Sqaure'
            
        elif choice == '3':
            area = area_of_para()
            shape = 'Parallelogram'
            
        elif choice == '4':
            area = area_of_rhombus()
            shape = 'Rhombus'
            
        elif choice == '5':
            print('Thanks for using the application.')
            break
            
        else:
            print('Choose an valid option')
            continue
            
 
# asking unit of length           
      
        while True:
            unit = input('Give the unit of length: ').strip().lower()               
            if unit == 'm' or unit == 'cm':
                print(f'The area of {shape} is {area}{unit}².')
                break
            else:
                print('Give an valid unit of length!! ')
                                 
main()
