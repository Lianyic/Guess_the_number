print ('This is a guessthenumber game, you will have 3 chances')
print ('I am thinking of a numbers between 1 and 13')
import random
secretnumber=random.randint(1,13)
for guesstaken in range(1,4):
    print ('take a guess')
    guessnumber = int(input())

    if guessnumber>secretnumber:
        print ('your guess is too high')
    elif guessnumber<secretnumber:
        print('your guess is too low')

    if guessnumber==secretnumber:
        print('you are right! you passed the guess game in only '+str(guesstaken)+' guesses')
        break
else:
    print('uh oh, the number I am thinking of is '+str(secretnumber))



