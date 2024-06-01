for t in range(int(input())):
    word = str(input())
    if len(word) > 10:
        word_lenght = (len(word)-2)
        print(f'{word[0]}{word_lenght}{word[-1]}')
    else:
        print(word)
