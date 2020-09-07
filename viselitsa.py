import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    0   |
        |
        |
       ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
    |
       ===''', '''
    +---+
    0   |
   /|\  |
  / |   |
       ===''', '''
    +---+
    0   |
   /|\  |
   / \  |
       ===''','''
    +---+
   [0   |
   /|\  |
   / \  | 
       ===''','''
    +---+
   [0]  |
   /|\  |
   / \  | 
       ===''']
words = { 'животные':'аист акула бабуин баран барсук кобра коза козел койот корова кошка кролик '.split(),
'цвет' : 'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
'фигуры':'квадрат треугольник прямоугольник круг эллипс ромб трапеция восьмиугольник куб'.split(),
"фрукты" :'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split()}
#'
# Дополнительные слова
# бобр бык верблюд волк воробей ворон выдра голубь
# крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул 
# муравей мышь норка носорог обезьяна овца окунь олень орел
#  осел панда паук питон попугай пума семга
#  скунс собака сова тигр тритон тюлень утка форель 
# хорек черепаха ястреб ящерица.'

def getRandomWord(wordDict):
     # Эта функция возвращает случайную строку из переданного словаря списков строк, а также ключ.
     # Во-первых, случайным образом выбираем ключ из словаря:
        wordKey = random.choice(list(wordDict.keys()))
    # Во-вторых, случайным образом выбираем слово из списка ключей в словаре:
        wordIndex = random.randint(0,len(wordDict[wordKey]) -1)
        return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:',end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Показывает секретное слово с пробелами между буквами
            print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
 # Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше.
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')

        else:
            return guess

def playAgain():
    # Эта функция возвращает значение True, если игрок хочет сыграть заново; в противном случае возвращает False.
    print('Хотите сыграть еще? (да или нет)')
    return input().lower().startswith('д')

print('В И С Е Л И Ц А')


difficulty = ''
while difficulty not in ['Л','С','Т']:
    print('Выберите уровень сложности: Л - легкий, С - Средний, Т - Тяжелый ')
    difficulty = input().upper()
if difficulty == 'C':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'Т':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
    
missedLetters = ''
correctLetters = ''
secretWord , secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print(' Секретное слово принадлежиит набору : ' + str(secretSet))
    displayBoard(missedLetters, correctLetters, secretWord)

    # Позволяет игроку ввести букву.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

         # Проверяет, выиграл ли игрок.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Проверяет, превысил ли игрок лимит попыток и проиграл.
    if len(missedLetters) == len(HANGMAN_PICS) - 1:
        displayBoard(missedLetters, correctLetters, secretWord)
        #print('Вы исчерпали все попытки!\nНеугадано букв:'+str(len(missedLetters))+'и угадано букв:'+str(len(correctLetters))+'.Было загадано слово"'+secretWord+'".')
        print('Вы исчерпали все попытки!\t Неугадано букв: ' + str(len(missedLetters))+'\t Было угадано букв '+str(len(correctLetters)) +'\tБыло загадано слово : '+ str(secretWord))
        gameIsDone = True

#Написание кода игры «Виселица» 123,
 # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord , secretSet = getRandomWord(words)
        else:
            break
