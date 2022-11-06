import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''      "Бaйглз" Дедуктивна гра.
      Я загадую будь-яке {}-значне число. Спробуй вгадати його. Всього у тебе 10 спроб.
      Ось деякi розшифровки:
      Коли я кажу:      Це означає:
          Пiко                    Одна правильна цифра, але не на своєму мiсцi.
          Фермi                 Одна правильна цифра та на своєму мiсцi.
          Бейглз                Жодної правильної цифри
Для прикладу, якщо секретна цифра 248, а ваша вiдповiдь 843, то комп'ютер скаже Фермi Пiко.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print('Ви маєте {} спроб, щоб вгадати число.'.format(MAX_GUESSES))
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Спроба #{}: '.format(numGuesses))
                guess = input('> ')
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('У вас закiнчилися спроби.')
                print('Секретне число - {}.'.format(secretNum))
        print('Бажаєте зiграти знову? (так або нi)')
        if not input('> ').lower().startswith('т'):
            break
    print('Дякую за гру!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Ви вгадали!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Фермi')
        elif guess[i] in secretNum:
            clues.append('Пiко')
    if len(clues) == 0:
        return 'Байглз' 
    else:
        clues.sort()
        return ' '.join(clues)
    
if __name__ == '__main__':
    main()
