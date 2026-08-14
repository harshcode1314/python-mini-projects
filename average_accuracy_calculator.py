#asking the user for the accuracy of last 5 matches 

while True:
    try:
        match1_accuracy = float(input('What was your accuracy of last match? '))
        match2_accuracy = float(input('What was your accuracy of second last match? '))
        match3_accuracy = float(input('What was your accuracy of third last match? '))
        match4_accuracy = float(input('What was your accuracy of fourth last match? '))
        match5_accuracy = float(input('What was your accuracy of fifth last match? '))
        break
    except:
        print('Enter an valid value! ')
        
average_accuracy = (match1_accuracy+match2_accuracy+match3_accuracy+match4_accuracy+match5_accuracy)/5

print(f'So your average accuracy is {average_accuracy}.')
#calculating average accuracy and giving it to user