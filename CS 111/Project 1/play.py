#Playing the game with words and scores
word=input('Word: ')
word=word.lower()                 
score=dictionary[word]
print('Score for '+word+':', score)
#Build lists
words_list.append(word)
scores_list.append(score)
