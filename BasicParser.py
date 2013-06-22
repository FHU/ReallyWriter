'''
Created on Jun 17, 2013

@author: andy.maach@students.fhu.edu
'''

import sys

VOWELS = "aeiouy"
LETTERS = "abcdefghijklmnopqrstuvwxyz"
SPACE = " "
SENTENCE = ".!?"

source = sys.argv[1]

if source == "fields":
    print "@ATTRIBUTE   letters_per_word        NUMERIC"
    print "@ATTRIBUTE   vowels_per_letter       NUMERIC"
    print "@ATTRIBUTE   words_per_sentence		NUMERIC"

#Open the input
f = open(source, 'r')

data = f.read().lower()

letters = 0.0
words = 0.0
vowels = 0.0
sentences = 0.0

had_word_since_space = False
had_sentence_since_period = False


for c in data:
    if c in LETTERS:
        letters += 1
        had_word_since_space = True
        had_sentence_since_period = True
        
    if c in VOWELS:
        vowels += 1

    if had_word_since_space and c in SPACE:
        words += 1
        had_word_since_space = False
        
    if had_sentence_since_period and c in SENTENCE:
        sentences += 1

sentences -= data.count(" mrs. ")
sentences -= data.count(" mr. ")
sentences -= data.count(" dr. ")
sentences -= data.count(" ms. ")

letters -= data.count(",") #lower() counts commas as letters..why idk.
        
if sentences == 0: sentences = 1

letters_per_word = letters  / words
vowels_per_letter = vowels / letters
words_per_sentence = words / sentences

sys.stdout.write(str(letters_per_word) + "," + str(vowels_per_letter) + "," + str(words_per_sentence))
        