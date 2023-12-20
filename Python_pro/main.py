import random

SOZLER=[
    'python',
    'javascript',
    'ruby'
    'clean', 
    'translate',
    'cook',
    'wash',
    'watch',
    'bake',
    'fry',
    'boil',
    'dust',
    'want',
    'repair',
    'fix',
    'play',
    'live',
    'like',
    'open',
    'clothe',
    'explain',
    'love',
    'start'
]

MAX_QATELER= 15
def soz_oylaw():
    return random.choice(SOZLER)

def harip_kiritiw():
    a=input('Haripti kiritin: ')
    return a.lower()

def get_initial_statuses(word):
    statuses = []
    for letter in word:
        statuses.append(False)
    return statuses

def finish(statuses, current_errors):
    if current_errors >= MAX_QATELER:
        return True
    for status in statuses:
        if not status:
            return False
    return True

def tekseriw(word, statuses, letter): 
    if letter not in word:
        return False
 
    for index, l in enumerate(word):
        if letter == l:
            statuses[index] = True
 
    return True

def print_word(word, statuses):  
    for index, letter in enumerate(word):
        if statuses[index]:
            print(letter, end='')
        else:
            print('_', end=' ')
    print()

def main():  
    word = soz_oylaw()
    statuses = get_initial_statuses(word)
    current_errors = 0
    while not finish(statuses, current_errors):
        print_word(word, statuses)
        print('Qalgan urinislariniz: ', MAX_QATELER - current_errors)
        letter = harip_kiritiw()
        result = tekseriw(word, statuses, letter)
 
        if not result:
            current_errors += 1
 
    if current_errors >= MAX_QATELER:
        print('Siz utildiniz!')
    else:
        print('Siz uttiniz!')   
        
main() 
 
