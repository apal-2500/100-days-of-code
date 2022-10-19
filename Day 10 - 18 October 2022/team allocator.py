import random

players = ["Martin", "Craig", "Sue",
	   "Claire", "Dave", "Alice",
	   "Sonakshi", "Harry", "Jack",
	   "Ross", "Lexi", "Maria",
	   "Thomas", "James", "William",
	   "Ada", "Grace", "Jean",
	   "Marissa", "Alan"]

print("Welcome to Team Allocator!")

while True:
    random.shuffle(players)

#select the first team
    team1 = players[:len(players)//2]

    print("Team 1 captain: " + random.choice(team1))

    print("Team 1: ")
    for player in team1:
        print(player)

#select the second team
    team2 = players[len(players)//2:]

    print("\nTeam 2 Captain: " + random.choice(team2))
    print("Team 2: ")
    for player in team2:
        print(player)

#break loop
    response = input("Pick teams again? Type y or n: ")
    if response == "n":
        break

#team or tornament
#print("Welcome to Team/Player Allocator!")
#while True:
#    random.shuffle(players)
#    response = input("Is it a team or individual sport? \
#			\nType team or individual: ")
#    if response == "team":
#       team1 = players[:len(players)//2]

#    for player in team2:
#        print(player)
#    else:
#        for i in range(0, 20, 2):
#            print(players[i] + " vs " + players[i+1])

#   print(players[i] + " vs " + players[i+1])
#   start = random.randrange(i, i+2)
#   print(players[start] + " starts")
