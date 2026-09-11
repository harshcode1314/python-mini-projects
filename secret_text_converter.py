import string 

vowels_alt = {
    'a' : 's',
    'e' : 't',
    'i' : 'p',
    'o' : 'l',
    'u' : 'm',
    'A' : 'S',
    'E' : 'T',
    'I' : 'P',
    'O' : 'L',
    'U' : 'M'  
   }
   
def convert_to_cd_language(sentence,vowels_al):
    words = sentence.split(' ')
    converted_words = []
    
    
    for word in words: 
        core_word = word.rstrip(string.punctuation)
        end_punc = word[len(core_word):]
        temp_letters = []                     
        for letter in core_word:            
            if letter in vowels_al:
                temp_letters.append(vowels_al[letter])
                
            else:
                temp_letters.append(letter)
        converted_words.append(''.join(temp_letters)  +'z' + end_punc)
            
                    
    return ' '.join(converted_words)                    
    
sentence = input().strip()
print(convert_to_cd_language(sentence,vowels_alt))
        
        
        
    