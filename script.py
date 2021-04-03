VOWELS = ['A', 'E', 'I', 'O', 'U']

word = input("Please enter a word: ").upper()

vowels_counter = 0
consonants_counter = 0

if len(word.split()) > 1:
    print("Only enter one word")
else:
    for l in word:
        if l in VOWELS:
            vowels_counter+=1
        else:
            consonants_counter+=1

    print("Vowels:", vowels_counter)
    print("Consonants:", consonants_counter)

    