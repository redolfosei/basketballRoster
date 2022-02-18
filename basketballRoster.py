#basket Ball Roster Program 
#Welcome the user to the program. 

print("\nWelcome to the Basket Ball Roster Program")

#initialise players to an empty list and accept inputs of players
players = []
players.append(input("\nWho is you point guard? ").title())
players.append(input("\nWho is your shooting guard? ").title())
players.append(input("\nWho is your small forward? ").title())
players.append(input("\nWho is your power forward? ").title())
players.append(input("\nWho takes the center? ").title())

#Display the inputs of the user.
print("\n\tYour starting 5 for the upcoming bastekball season")
print(f"\t\tPoint Guard: \t{players[0]}")
print(f"\t\tShooting Guard: \t{players[1]}")
print(f"\t\tsmall Forward: \t{players[2]}")
print(f"\t\power Forward: \t{players[3]}")
print(f"\t\tcenter: \t{players[4]}")

#remove the injured player
injured_player = players.pop(2)

#Display injured player,number left and 
print(f"Oh no!, {injured_player} is injured")
print(f"Your roster have only {len(players)} players. ")
replaced_player = input(f"Who will take {injured_player}'s spot? ")

#insert new player 
players.insert(2,replaced_player)

#Display the new list of players.
print("\n\tYour CONFIRMED! starting 5 for the upcoming bastekball season")
print(f"\t\tPoint Guard: \t{players[0]}")
print(f"\t\tShooting Guard: \t{players[1]}")
print(f"\t\tsmall Forward: \t{players[2]}")
print(f"\t\power Forward: \t{players[3]}")
print(f"\t\tcenter: \t{players[4]}")

print(f"Good Luck this season, {players[2]} will do well!")
print(f"Your Roster have {len(players)} players now!")

