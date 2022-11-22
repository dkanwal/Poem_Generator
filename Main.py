'''
Written by Deven Kanwal, 11/21/22.
In this script: Main.py contains the main() method which drives Genpo Supreme 
utilizing its three helper scripts.
'''


import Build_Line
import Word_Classifier
import Evaluate
import numpy as np
import os 

def main():
    """Program driver. Prompts user for input and returns a saved output poem 
    with optimal fitness, and reads the poem aloud for the user."""
    num_words_per_line = input("How many words per line?\n")
    num_lines_per_stanza = input("How many lines per stanza?\n")
    num_stanzas = input("How many stanzas would you like the poem to have?\n")

    num_iterations = 4 #number of iterations to get the best fitness value

    '''Block of if statements makes an introduction to begin the poem'''
    poem_type = Word_Classifier.selected_file[0]
    if poem_type == 'climate_change.txt':
        introduction = 'A poem on climate change. '
    elif poem_type == 'fall_season.txt':
        introduction = 'A Fall poem. '
    elif poem_type == 'native_american.txt':
        introduction = 'A poem inspried by Native Americans. '
    elif poem_type == 'love_poems.txt':
        introduction = 'A love poem. '
    
    
    '''For loop iterates through the process of creating a poem, reserving
    the most fit version for output.'''
    lowest_fitness = 99999 #Fitness of output poem saved to this parameter
    output_poem = '' #Most fit poem saved here
    iteration_number = 0
    for num in range(0, num_iterations):
        poem = '' #Poem for current iteration
        for i in range(0, int(num_stanzas)):
            #Building a stanza from user specified number of lines
            for j in range(0, int(num_lines_per_stanza)): 
                line = Build_Line.build_line(int(num_words_per_line)) 
                poem = poem + line + '\n'
            poem = poem + '\n'    
        poem_fitness = Evaluate.syllable_fitness(poem=poem)
        if poem_fitness < lowest_fitness:
            lowest_fitness = poem_fitness
            output_poem = poem
            iteration_number = num
        else:
            continue
    
    '''Writing to the output file bringing together the introduction, poem, and 
    Genpo Supreme's signauture.'''
    
    with open("output/generated_poem", "w") as f:
        f.write("Poem Fitness: " + str(lowest_fitness) + '\n' + '\n')
        f.write(introduction + 'Selection number ' + str(iteration_number) + \
            ' out of ' + str(num_iterations) + '.' + '\n' + '\n')
        f.write(output_poem + '\n' + '\n')
        f.write("Written by Genpo Supreme")
        f.close()

    os.system("open output/test_output")

    '''For loop uses os's TTS to speak the poem and open it on local machine'''
    for line in output_poem.splitlines():
        if line != '':
            os.system("say " + line)
        else:
            continue
    
if __name__ == "__main__":
    main()