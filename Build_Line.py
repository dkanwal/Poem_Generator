import Word_Classifier
from Word_Classifier import noun_phrases as nouns
from Word_Classifier import verbs
import numpy as np

def build_line(num_words):
    '''This method builds each line for the generated poem'''
    line = ''
    if num_words == 0:
        line = 'A poem with no words is not a poem...or is it?'
        return line

    if num_words < 5:
        words_at_a_time = num_words
    elif num_words >= 5 and (num_words % 4 == 0):
        words_at_a_time = 4
    elif num_words >= 5 and (num_words % 3 == 0):
        words_at_a_time = 3
    elif num_words >= 5 and (num_words % 2) == 0:
        words_at_a_time = 2
    elif num_words >= 5:
        words_at_a_time = 1
    
    num = 0
    while num < num_words:
        format_selection = np.random.randint(9, size=1)
        if len(nouns) > 0: noun_phrase = np.random.choice(nouns, size=1)
        if len(verbs) > 0: verb_phrase = np.random.choice(verbs, size=1)
        if len(Word_Classifier.proper_nouns) > 0: proper_noun = np.random.choice(Word_Classifier.proper_nouns, size=1)
        if len(Word_Classifier.adjectives) > 0: adjective = np.random.choice(Word_Classifier.adjectives, size=1)
        if len(Word_Classifier.adverbs) > 0: adverb = np.random.choice(Word_Classifier.adverbs, size=1)
        if len(Word_Classifier.transition) > 0: transition = np.random.choice(Word_Classifier.transition, size=1)
        if len(Word_Classifier.conjunctions) > 0: conjuntion = np.random.choice(Word_Classifier.conjunctions, size=1)
        if len(Word_Classifier.pronouns) > 0: pronoun = np.random.choice(Word_Classifier.pronouns, size=1)
        if len(Word_Classifier.numbers) > 0: number = np.random.choice(Word_Classifier.numbers, size=1)
            
        if words_at_a_time == 1:
            if format_selection == 0:
                line = line + noun_phrase[0] + ' '
            elif format_selection == 1:
                line = line + verb_phrase[0] + ' '
            elif format_selection == 2:
                line = line + proper_noun[0] + ' '
            elif format_selection == 3:
                line = line + adjective[0] + ' '
            elif format_selection == 4:
                line = line + adverb[0] + ' '
            elif format_selection == 5:
                line = line + transition[0] + ' '
            elif format_selection == 6:
                line = line + conjuntion[0] + ' '
            elif format_selection == 7:
                line = line + pronoun[0] + ' '
            elif format_selection == 8:
                line = line + number[0] + ' '
            num = num + 1
            continue
        elif words_at_a_time == 2:
            if format_selection == 0:
                line = line + noun_phrase[0] + ' ' + verb_phrase[0] + ' '
            elif format_selection == 1:
                line = line + verb_phrase[0] + ' ' + adverb[0] + ' ' 
            elif format_selection == 2:
                line = line + proper_noun[0] + ' ' + verb_phrase[0] + ' ' 
            elif format_selection == 3:
                line = line + adjective[0] + ' ' + noun_phrase[0] + ' ' 
            elif format_selection == 4:
                line = line + adverb[0] + ' ' + adjective[0] + ' ' 
            elif format_selection == 5:
                line = line + transition[0] + ' ' + noun_phrase[0] + ' ' 
            elif format_selection == 6:
                line = line + conjuntion[0] + ' ' + adjective[0] + ' '
            elif format_selection == 7:
                line = line + pronoun[0] + ' ' + noun_phrase[0] + ' ' 
            elif format_selection == 8:
                line = line + number[0] + ' ' + noun_phrase[0] + ' ' 
            num = num + 2
            continue
        elif words_at_a_time == 3:
            if format_selection == 0:
                line = line + noun_phrase[0] + ' ' + verb_phrase[0] + ' ' + adjective[0] + ' '
            elif format_selection == 1:
                line = line + verb_phrase[0] + ' ' + adverb[0] + ' ' + transition[0] + ' '
            elif format_selection == 2:
                line = line + proper_noun[0] + ' ' + verb_phrase[0] + ' ' + conjuntion[0] + ' '
            elif format_selection == 3:
                line = line + adjective[0] + ' ' + noun_phrase[0] + ' ' + verb_phrase[0] + ' '
            elif format_selection == 4:
                line = line + adverb[0] + ' ' + adjective[0] + ' ' + noun_phrase[0] + ' '
            elif format_selection == 5:
                line = line + transition[0] + ' ' + noun_phrase[0] + ' ' + verb_phrase[0] + ' '
            elif format_selection == 6:
                line = line + conjuntion[0] + ' ' + adjective[0] + ' ' + noun_phrase[0] + ' '
            elif format_selection == 7:
                line = line + pronoun[0] + ' ' + noun_phrase[0] + ' ' + verb_phrase[0] + ' '
            elif format_selection == 8:
                line = line + number[0] + ' ' + noun_phrase[0] + ' ' + adjective[0] + ' '
            num = num + 3
            continue
        elif words_at_a_time == 4:
            if format_selection == 0:
                line = line + noun_phrase[0] + ' ' + verb_phrase[0] + ' ' + adjective[0] + ' ' + transition[0] + ' '
            elif format_selection == 1:
                line = line + verb_phrase[0] + ' ' + adverb[0] + ' ' + transition[0] + ' ' + noun_phrase[0] + ' '
            elif format_selection == 2:
                line = line + proper_noun[0] + ' ' + verb_phrase[0] + ' ' + conjuntion[0] + ' ' + adjective[0] + ' '
            elif format_selection == 3:
                line = line + adjective[0] + ' ' + noun_phrase[0] + ' ' + verb_phrase[0] + ' ' + conjuntion[0] + ' '
            elif format_selection == 4:
                line = line + adverb[0] + ' ' + adjective[0] + ' ' + noun_phrase[0] + ' ' + number[0] + ' '
            elif format_selection == 5:
                line = line + transition[0] + ' ' + noun_phrase[0] + ' ' + verb_phrase[0] + ' ' + adjective[0] + ' '
            elif format_selection == 6:
                line = line + conjuntion[0] + ' ' + adjective[0] + ' ' + noun_phrase[0] + ' ' + verb_phrase[0] + ' '
            elif format_selection == 7:
                line = line + pronoun[0] + ' ' + noun_phrase[0] + ' ' + verb_phrase[0] + ' ' + transition[0] + ' '
            elif format_selection == 8:
                line = line + number[0] + ' ' + noun_phrase[0] + ' ' + adjective[0] + ' ' + adverb[0] + ' '
            num = num + 4
            continue

    return line

#print(build_line(15))