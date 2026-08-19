# making a function to ask amswer from the user and to check whether the user has given a number or anything else

def get_answer():
    while True:
        try:
            answer = float(input('Answer: '))
            break
        except ValueError:
            print('Give a valid number!')
    return answer
    
# making a function to store user answers

def store_answers(questions):  
    user_answers = []  
    for question in questions:
        print(question)
        user_answers.append(get_answer())
    return user_answers 
    
# making a function check whether the answers of user are cirrect or not 

def check_answers(answer_sheet,user_answers):
    score = 0
    for user_answer, answer  in zip (user_answers,answer_sheet):
        if user_answer == answer:
            score += 1
        
    return score 
        
# defining the main function 

def main():
    questions = ['What is 88/22?','What square root of 144?'] 
    answer_sheet = [4,12]
    user_answers = store_answers(questions)
    score = check_answers(answer_sheet,user_answers)
    print(f'So your score is {score}.')
      
      
main()
        
            
            
              
 

    
        