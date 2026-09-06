#defining a function to take user input and checking it that is it has an valif format

def get_num(question='Give the number: '):
    while True:
        try:
            return int(input(question))
        except ValueError:
            print('Invalid input! Please enter a whole number')
            
#defining a function to get the size of the list in which we will insert the numbers which we will add

def get_size():
    while True:
        size = get_num("How many numbers do you want to add? ")
        if size > 0:
            return size
            
        else:
            print("Size must be greater than 0.")


#making a function to sort even numbers from a list
def get_even_num(nums):
    evens = []
    for num in nums:
        if num%2 == 0:
            evens.append(num)
    return evens



#defining the main manager function

def main():
    nums = []
    size = get_size()
    for i in range(size):
        nums.append(get_num())
        
    sum_of_evens = int(sum(get_even_num(nums)))
    print(f'\nSum of all even numbers in your list is {sum_of_evens}')
    
    
main()
        