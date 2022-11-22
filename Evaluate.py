'''
Written by Deven Kanwal, 11/21/22
In this script: Evaluate.py is called on by Main.py to output a fitness score 
for each poem that Genpo Supreme composes. The fitness score is the difference 
between the line with the most syllables in a poem and the line with the least. 
The lower the score, the better.
'''


def syllable_counter(word):
    '''This function counts the syllables in a given word'''
    vowels_plus_y = 'aeiouy'
    lc_word = word.lower() #all counting is done in lowercase
    syllables = 0

    if lc_word[0] in vowels_plus_y:
        syllables += 1
    for i in range(1, len(lc_word)):
        if lc_word[i] in vowels_plus_y and lc_word[i-1] not in vowels_plus_y:
            syllables += 1
    if lc_word[-1] == 'e':
        syllables -= 1
    
    if syllables == 0:
        syllables += 1
    
    return syllables

def line_syllables(line):
    '''Method counts the number of syllables in a given line'''
    counter = 0
    for word in line.split():
        number_of_syllables = syllable_counter(word)
        counter += number_of_syllables
    return counter

def syllable_fitness(poem):
    '''This method take in a poem and finds the difference
    between the line with the most syllables and the line with
    the least syllables.'''
    syllables_each_line = []
    for line in poem.splitlines():
        num_syllables = line_syllables(line)
        syllables_each_line.append(num_syllables)
    minimum = min(syllables_each_line)
    maximum = max(syllables_each_line)
    difference = maximum - minimum
    return difference
