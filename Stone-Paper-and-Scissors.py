import random
'''
1 for the Rock
2 for the Paper 
3 for the Scissor
'''
computer = random.choice([1,2,3])
your_choice=input("Enter your choice:")
youDict = {"R":1,"P":2,"S":3}
reverseDict = {1 : "Rock", 2 : "Paper" , 3 : "Scissor"}

you = youDict[your_choice]


print (f"You choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if (computer == you):
    print ("Its a draw")

else:
    if(computer ==1 and you ==2):
       print ("You Win!")
    elif(computer ==2 and you ==3):
       print ("You Win!")
    elif(computer ==3 and you ==1):
       print ("You win !")
    if(computer ==2 and you ==1):
       print ("Computer Win!")
    elif(computer ==3 and you ==2):
       print ("Computer Win!")
    elif(computer ==1 and you ==3):
       print ("Computer win !")

