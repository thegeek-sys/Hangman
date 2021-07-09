import argparse, random

parser = argparse.ArgumentParser()
parser.add_argument("--difficulty", "-d", help="set difficulty")

def wordsScraper():
    wordstoadd = []
    f = open("tobecleaned.txt", "r")
    accentate = r"àèìòùáéíóú"
    for x in f:
        if len(x) > 5 and not any(elem in x.encode('utf-8') for elem in accentate.encode('utf-8')):
            wordstoadd.append(x)
    print(wordstoadd)
    f.close()
    f = open("words.txt", 'w')
    f.writelines(wordstoadd)
    f.close()

def findStr(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def setdifficulty(args):
    if args.difficulty and args.difficulty in ["1", "2", "3"]:
        print("Difficoltà impostata ad %s" % args.difficulty)
        return args.difficulty
    elif not args.difficulty:
        return "2"
    else:
        print("Invalid argument")
        quit()

def selectWord(difficulty):
    word = ''
    if difficulty == "1":
        attempts = 25
        length = False
    elif difficulty == "2":
        attempts = 10
        length = False
    elif difficulty == "3":
        attempts = 5
        length = True

    if length:
        while len(word) < 8:
            line = random.randrange(0, 1013)
            f = open("words.txt", 'r')
            word = f.readlines()[line]
    else:
        line = random.randrange(0, 1013)
        f = open("words.txt", 'r')
        word = f.readlines()[line]
        word = word.strip()
    return attempts, word

def game(attempts, word):
    print(word)  
    errors = 0
    wrong = []
    word_to_find = []
    for x in range(len(word)):
        word_to_find.append('_')
    while True:
        if errors == attempts:
            print('Hai terminato i tentativi, mi spiace!')
            quit()
        elif ''.join(word_to_find) == word:
            print('')
            print(word)
            print('Complimenti, hai vinto!')
            quit()
        print('_______________________________________________')
        print('Tentativi: '+str(errors)+'/'+str(attempts))
        print('Parola da indovinare: '+' '.join(word_to_find))
        print('Sbagliate: '+', '.join(wrong))
        print('')
        letter = input('> ')
        if len(letter) != 1:
            print('Inserire una sola lettera')
        elif letter in word:
            for x in findStr(word, letter):
                word_to_find[x] = letter
        elif letter not in word:
            if letter in wrong: 
                print('Lettera già provata, ritentare')
            else:
                errors += 1
                wrong.append(letter)

def main():
    args = parser.parse_args()
    difficulty = setdifficulty(args)
    attempts, word = selectWord(difficulty)
    game(attempts, word)
    

if __name__ == '__main__':
    main()