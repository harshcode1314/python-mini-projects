#making a function to get the word to check that is it a palindrome

def get_word():
    while True:
        word= input('Give the word: ').strip().lower()
        if ' 'in word:
            print('Give only one word!')
        else:
            break
    return word
        
        
#making a function to generate a reverse version of the word given by the 

def do_reverse():
    word = get_word()
    reversed_word= word[::-1]
    return word,reversed_word
    
  
#making a function to check that a given word is a palindrome

def is_palindrome(word,reversed_word):
    if word == reversed_word:
        print('Yes this word is a palindrome.')
    else:
        print('No, this is not a palindrome.')
        
     
#making the main function
def main():
    word,reversed_word = do_reverse()
    is_palindrome(word,reversed_word)
    
    
    
main()