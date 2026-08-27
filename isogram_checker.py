#making a function to ask the user for a word and to ensure that the user only gives one word 

def get_word():
    while True:
        word= input('Give a word to check whether it is isogram or not:  ').strip().lower()
        if ' 'in word:
            print('Give only one word!')
        else:
            break
    return word
    
    
#making a function to check whether a specific word is a isogram or not

def is_isogram():
    word= get_word()
    letters = []
    result = 'Yes,this is a isogram.'
    for letter in word:
        if letter in letters:
            result = 'No,it is not a isogram.'
            break
        letters.append(letter)
    return result
    
    

print(is_isogram())
    
            
  
        