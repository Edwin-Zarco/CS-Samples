#User input to list
letters=input('Enter 7 puzzle letters: ')
letters=letters.upper()

#Generate puzzle
print('--------SPELLING BEE-------')
print('--------- / ¯¯¯ \ ---------')
print('---------    '+letters[2]+'    ---------')
print('----/ ¯¯¯ \ ___ / ¯¯¯ \----')
print('----   '+letters[3]+'           '+letters[1]+'   ----')
print('----\ ___ / ¯¯¯ \ ___ /----')
print('---------    '+letters[0]+'    ---------')
print('----/ ¯¯¯ \ ___ / ¯¯¯ \----')
print('----   '+letters[4]+'           '+letters[6]+'   ----')
print('----\ ___ / ¯¯¯ \ ___ /----')
print('---------    '+letters[5]+'    ---------')
print('--------- \ ___ / ---------')
