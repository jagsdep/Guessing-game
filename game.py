# raw_input(): the return type of raw_input() is always a string
# input(): the return type of input() need not to be string only it could be integer, depending on what python have judged it to be

print ("Howdy, what is your name?");
name = raw_input() #prompt the user to enter his name and store it to a variable named name.

print (name + ', I am thinking of a number between 1 and 100');
print('Try to guess my number')

number_of_tries=0;

import random #to generate a random number we need to first import 

n = random.randint(1, 99) #we will use the random module to generate a number between 1 to 100 and store it in a variable named n.

guess = int(input("Your Guess? "))
while n != "guess":
    number_of_tries+=1 #we are incrementing the value of number_of_tries variable by 1.
    
    if guess < n:
        print ("Your guess is too low");
        guess = int(input("Your Guess? "))
    if guess > n:
        print ("Your guess is too high");
        guess = int(input("Your Guess? "))
        
    if guess == n:
         print ('Well done, ' + name + ' you found my number in '+ str(number_of_tries) + ' tries');
         
         break


    
   
    