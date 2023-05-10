from random import shuffle

def shuffle_cups(a_list):
    shuffle(a_list)
    return a_list

def guess_cup():
    guess = ''

    while guess not in ['0','1','2','3']:
        guess = input('Choose cup 0,1,2 or 3: ')
    
    return int(guess)

def check_cup(cups, guess):
    if cups[guess] == '100$':
        print("You have got 100$.")
    else:
        print("The cup is empty.")
        print(cups)

cups = ['empty', '100$', 'empty', 'empty']
shuffled_cups = shuffle_cups(cups)
guess = guess_cup()
check_cup(shuffled_cups, guess)

