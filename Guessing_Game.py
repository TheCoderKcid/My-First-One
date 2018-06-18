def GuessingGame():
    print('This is a demo. In the game, the computer randomly selects one word from a list of so far four words. You must guess this word within three tries. Make sure to guess with the first letter of the word capitalized. If you want an expanded version of the game, go to issues, and comment with the title ''<Like the Game>'' Thanks for playing the game!') 
    import random
    wrong=0
    WordList=['Parakeet', 'Pseudonym', 'Brahms', 'Bacon']
    word=random.choice(WordList)
    if word=='Parakeet':
          print('''Your five clues are:
                1. It is small.
                2. It is avian.
                3. It rhymes with 'cheat' and begins with a 'P'.
                4. It makes a great pet and is probably found a a Petco near you.
                5. It likes warm climates.''')
          guess=input('The word has been chosen and the clues are shown. Please input your guess. ')
          if guess==word:
              print('You won!')
          else:
              print('Sorry, that is incorrect.')
              wrong=1
              guess2=input('You have two more tries. Guess again! ')
              if guess2==word:
                  print('You won!')
              else:
                  print('Sorry, that is also incorrect.')
                  wrong=2
                  guess3=input('This is yout last guess! Be sure before you answer!')
                  if guess3==word:
                      print('You won!')
                  else:
                      print('Sorry, you have not guessed the word within the three tries alotted. You lose')
    if word=='Pseudonym':
          print('''Your five clues are:
                1. It's latin root means 'False'.
                2. Authors sometimes use it as their name on a book.
                3. It rhymes with 'Rim' and begins with a 'P'.
                4. The 'P' is silent.
                5. Theodore Geisel's was Dr. Seuss.''')
          guess=input('The word has been chosen and the clues are shown. Please input your guess. ')
          if guess==word:
              print('You won!')
          else:
              print('Sorry, that is incorrect.')
              wrong=1
              guess2=input('You have two more tries. Guess again! ')
              if guess2==word:
                  print('You won!')
              else:
                  print('Sorry, that is also incorrect.')
                  wrong=2
                  guess3=input('This is yout last guess! Be sure before you answer!')
                  if guess3==word:
                      print('You won!')
                  else:
                      print('Sorry, you have not guessed the word within the three tries alotted. You lose')
    if word=='Brahms':
          print('''Your five clues are:
                1. It is the name of a composer.
                2. One of the three B's.
                3. The composer wrote a lullaby known by a lot of people today.
                4. The composer was part of The War of the Romantics.
                5. The composer was a perfectionist.''')
          guess=input('The word has been chosen and the clues are shown. Please input your guess. ')
          if guess==word:
              print('You won!')
          else:
              print('Sorry, that is incorrect.')
              wrong=1
              guess2=input('You have two more tries. Guess again! ')
              if guess2==word:
                  print('You won!')
              else:
                  print('Sorry, that is also incorrect.')
                  wrong=2
                  guess3=input('This is yout last guess! Be sure before you answer!')
                  if guess3==word:
                      print('You won!')
                  else:
                      print('Sorry, you have not guessed the word within the three tries alotted. You lose')
    if word=='Bacon':
          print('''Your five clues are:
                1. It is a food.
                2. It is usually made with pig.
                3. It is also usually eaten at breakfast time.
                4. It is eaten in strip.
                5. It starts with a 'B'.''')
          guess=input('The word has been chosen and the clues are shown. Please input your guess. ')
          if guess==word:
              print('You won!')
          else:
              print('Sorry, that is incorrect.')
              wrong=1
              guess2=input('You have two more tries. Guess again! ')
              if guess2==word:
                  print('You won!')
              else:
                  print('Sorry, that is also incorrect.')
                  wrong=2
                  guess3=input('This is yout last guess! Be sure before you answer!')
                  if guess3==word:
                      print('You won!')
                  else:
                      print('Sorry, you have not guessed the word within the three tries alotted. You lose')
    
              
    
