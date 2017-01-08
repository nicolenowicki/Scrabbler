'''Nicole Nowicki: this program produces a list of scrabble words based on the letters inputed. Words can be organized by length or by tile score, there is a option to print the words which require just one more letter'''

from easygui import *
file = open(r"scrabble_words.txt")

#FUNCTIONS:
def score_tabulater(word, change):
    '''score_tabulater(string, string) --> integer 
    Returns the score calculated based on the argument's (word) content, also if blank spaced used the argument, change, represents the letter that is automaticaly scored zero'''
    
    #tile letters and correspoding scores (parallel lists)
    tile_letters = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    tile_scores = [0, 1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    score = 0
    
    for n in word:
        score += (tile_scores[tile_letters.index(n)])
        #bonus 50 points if word has 7 tiles or more
    if len(word) >= 7:
        score += 50 
    if change != "":
        score -= tile_scores[tile_letters.index(change)]        
    return score

word_list = []
extra_letter = []
extra_scores = []
tiles_1 = []
reg_scores = []

tiles = enterbox("Enter your tiles: ", "SCRABBLER")

while len(tiles) > 7:
    tiles = enterbox("Please enter 7 tiles or less: ", "SCRABBLER")
tiles = tiles.upper()

for n in tiles:
    tiles_1.append(n)
    
for line in file:
    line = line.strip("\n")
    #the variable extra is used to indicate if the word has used ONE extra letter
    #the words that use an extra will be appened to seperate lists and printed at the users request
    extra = 0
    letter_score = 0
    score_change = ""
    
    if len(line) <= (len(tiles)+1):
        word = ""
        tiles_2 = tiles_1[:]
        
        for n in line:
            if n in tiles_2:
                tiles_2.remove(n)
                word += n
            
            #cases where a blank tile is provided
            elif ' ' in tiles_2:
                score_change = n
                tiles_2.remove(' ')
                word += n
            
            #extra letter words    
            elif extra == 0:
                word += n
                extra = 1
        
        if word == line:
            if extra == 1:
                extra_letter.append(word)
                letter_score = score_tabulater(word, score_change)
                extra_scores.append(letter_score)
                
            else:
                word_list.append(word)
                letter_score = score_tabulater(word, score_change)
                reg_scores.append(letter_score)

user_1 = buttonbox("Provide possible words with: ", "SCRABBLER", ["Current Letters", "One More Letter"])
user_2 = buttonbox("Sort words by: ", "SCRABBLER", ["Length", "Tile Score"])

out = ""

if user_1 == 'Current Letters':
    if user_2 == 'Length':
        word_list_1 = word_list[:]
        word_list_1.sort(key = len)
        
        for n in word_list_1:
            out += "{}\n".format(n)
        textbox("Words From Short to Long Length:", "SCRABBLER", out)
            
    else:
        reg_scores_1 = reg_scores[:]
        reg_scores_1.sort()
        #using the index function and parallel lists, the sorted scores are found in the unsorted scores and matched with their corresponding words
        #when a score is matched with a word it is replaced in the list with '_'
        for n in reg_scores_1:
            index = reg_scores.index(n)
            reg_scores[index] = '_'
            out += "{}\n".format(word_list[index])
        textbox("Words From Least to Greatest Score:", "SCRABBLER", out)
    
elif user_1 == 'One More Letter':
    if user_2 == 'Length':
        extra_letter_1 = extra_letter[:]
        extra_letter_1.sort(key = len)
        
        for n in extra_letter_1:
            out += "{}\n".format(n)
        textbox("Words From Short to Long Length:", "SCRABBLER", out)
            
    else:
        extra_scores_1 = extra_scores[:]
        extra_scores_1.sort()
        
        for n in extra_scores_1:
            index = extra_scores.index(n)
            extra_scores[index] = '_'
            out += "{}\n".format(extra_letter[index])
        textbox("Words From Least to Greatest Score:", "SCABBLER", out)

#NOTES:        
#LIST WITH SCORES