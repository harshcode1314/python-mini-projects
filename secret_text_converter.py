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
    punc = ''
    
    for word in words: 
        punc = '' 
        temp_letters = []                     
        for letter in word:            
            if letter in vowels_al:
                temp_letters.append(vowels_al[letter])
            elif letter in string.punctuation:
                punc += letter    
            else:
                temp_letters.append(letter)
        if punc:
            converted_words.append(''.join(temp_letters) + 'z' + punc)            
        else:
            converted_words.append(''.join(temp_letters) + 'z')
                    
    return ' '.join(converted_words)                    
    
sentence = input().strip()
print(convert_to_cd_language(sentence,vowels_alt))
        
        
        
    