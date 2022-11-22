from cgi import print_arguments
from fileinput import filename
from string import punctuation
import random
from matplotlib.pyplot import text
import spacy
nlp = spacy.load("en_core_web_sm") #initalizes NLP


filename_list = ['climate_change.txt', 'fall_season.txt', 'native_american.txt', 'love_poems.txt']
selected_file = random.choices(filename_list, weights=[45, 15, 15, 25])
print('selected file')
print(selected_file)



#inspiring_text = open("Sample_Text.txt", "r")
inspiring_text = open("Inspiring_Sets/" + selected_file[0], "r")
it_as_string = inspiring_text.read() #inspiring text as a string

#processing the inspiring text
text = (it_as_string) 
doc = nlp(text) #initializing the natural language processor

noun_phrases = [token.lemma_ for token in doc if token.pos_ == "NOUN"] #Nouns present as a list
verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"] #verbs present as a list
proper_nouns = [token.lemma_ for token in doc if token.pos_ == "PROPN"] #proper nouns list
adjectives = [token.lemma_ for token in doc if token.pos_ == "ADJ"] #Adjectives list
adverbs = [token.lemma_ for token in doc if token.pos_ == "ADV"] #Adverbs list
transition = [token.lemma_ for token in doc if token.pos_ == "ADP"] #Transitions list
conjunctions = [token.lemma_ for token in doc if token.pos_ == "CCONJ"] #Conjunctions list
punctuation = [token.lemma_ for token in doc if token.pos_ == "PUNCT"] #Punctuation list
pronouns = [token.lemma_ for token in doc if token.pos_ == "PRON"] #Pronoun list
numbers = [token.lemma_ for token in doc if token.pos_ == "NUM"] #Numbers list











  