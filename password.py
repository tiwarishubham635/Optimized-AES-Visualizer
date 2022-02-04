import random
import sys
from math import log

if sys.version_info < (3, 0):
    input = raw_input

# Just some colors and shit
green = '\033[1;32m'
end = '\033[1;m'
question = '\033[1;34m[?]\033[1;m'

print('''\n\n%s WELCOME TO THE EASY TO REMEMBER PASSWORD GENERATOR ! %s\n\n''' % (green, end))


name = input('%s Enter your Name: ' % question).lower()
choice = input(
    '%s Do you want to Obsfucate the name? [Y/n] ' % question).lower()
if choice == 'n':
    obsfucate = False
else:
    obsfucate = True

first = ['had', 'throws', 'buys', 'eats', 'wishes', 'hates', 'likes', 'hits', 'touches', 'has', 'boils',
         'wants', 'cooks', 'spoils', 'travels', 'damages', 'destroys', 'cuts', 'rocks',
         'accepts', 'adds', 'admires', 'admits', 'advises', 'affords', 'agrees', 'alerts', 'allows', 'amuses', 'analyzes', 'announces', 'annoyes', 'answers', 'apologises', 'appears', 'applauds', 'appreciates', 'approves', 'argues', 'arranges', 'arrests', 'arrives', 'asks', 'attaches', 'attacks', 'attempts', 'attends', 'attracts', 'avoids',
         'begs', 'behaves', 'belongs', 'bleaches', 'blesses', 'blinds', 'blinks', 'blots', 'blushes', 'boasts']

second = ['your', 'our', 'white', 'cute', 'many', 'green', 'giant', 'all', 'three',
          'five', 'hundred', 'beautiful', 'my', 'red', 'nice', 'small', 'intelligent', 'little', 'ten', 'eager', 'easy', 'elated', 'elegant', 'embarrassed', 'enchanting', 'encouraging', 'energetic', 'enthusiastic', 'envious', 'evil', 'excited', 'expensive', 'exuberant', 'fair', 'faithful', 'famous', 'fancy', 'fantastic', 'fierce', 'filthy', 'fine', 'foolish', 'fragile', 'frail', 'frantic', 'friendly', 'frightened', 'funny', 'gentle', 'gifted', 'glamorous', 'gleaming', 'glorious', 'good', 'gorgeous', 'graceful', 'grieving', 'grotesque', 'grumpy', 'handsome', 'happy', 'healthy', 'helpful', 'helpless', 'hilarious', 'homeless', 'homely', 'horrible', 'hungry', 'hurt', 'ill', 'important', 'impossible', 'inexpensive', 'innocent', 'inquisitive', 'itchy', 'jealous', 'jittery', 'jolly', 'joyous', 'kind'
          ]

third = ['books', 'apples', 'butterflies', 'children', 'kids', 'hands', 'horses', 'trees', 'stones',
         'shirts', 'cats', 'boys', 'girls', 'computers', 'mangoes', 'pens', 'brushes', 'dogs', 'chairs', 'aliens', 'tables', 'students', 'relations', 'laptops', 'beds', 'shoes', 'socks', 'pans', 'rocks', 'humans', 'teachers', 'fairies', 'wise people', 'scientists', 'engineers', 'doctors', 'soldiers', 'businessmen', 'fan', 'AC', 'document', 'class', 'internet', 'randomness', 'song', 'phone', 'robber', 'batsman', 'bowler', 'wikcketkeeper', 'umpire', 'audience', 'artist', 'birds', 'animals', 'pets', 'doors', 'old people', 'youth', 'leaders', 'country', 'state', 'schools', 'colleges']

seperators = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '.', '-', '/', ':', ';', '<', '>', '=', '?', '@', '\\','\[','\]', '^', '_', '{', '}', '~', '|']

generated_passwords = []


def generate(name):
    wordlist = []
    wordlist.append(random.choice(first))
    wordlist.append(random.choice(second))
    wordlist.append(random.choice(third))
    seperator = random.choice(seperators)
    name = name.title()
    if obsfucate:
        name = name.replace('a', '@').replace('b', '6').replace('e', '3').replace(
            'i', '!').replace('l', '1').replace('T', '7').replace('s', '$').replace('o', '0')
    password = name + seperator + seperator.join(wordlist)
    entropy = (log(82)/log(2)) * len(password)
    pass_entry = [password, entropy]
    generated_passwords.append(pass_entry)


def initiate():
    print('')
    print(' %s+------------------------------------+---------------------+%s' % (green, end))
    print(' %s| Password                           | Entropy             |%s' % (green, end))
    print(' %s+------------------------------------+---------------------+%s' % (green, end))
    for y in range(0, 10):
        generate(name)
    generated_passwords.sort(key=lambda x: x[1], reverse=True)
    for password in generated_passwords:
        print(' %s|%s %-35s%s|%s %-20s%s|%s' %
              (green, end, password[0], green, end, password[1], green, end))
        print(' %s+--------------------------+-------------------------------+%s' % (green, end))
    choice = input(
        '\n%s Do you wish to generate more passwords? [y/N] ' % question).lower()
    if choice == 'y':
        initiate()
    else:
        quit()


initiate()
