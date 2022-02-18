#basket Ball Roster Program 
#Welcome the user to the program. 

print("\nWelcome to the Basket Ball Roster Program")

#initialise players to an empty list and accept inputs of players
players = []
players.append(input("\nWho is you point guard? ").title())
players.append(input("Who is your shooting guard? ").title())
players.append(input("Who is your small forward? ").title())
players.append(input("Who is your power forward? ").title())
players.append(input("Who takes the center? ").title())

#Display the inputs of the user.
print("\n\tYour starting 5 for the upcoming bastekball season")
print(f"\tPoint Guard: \t\t{players[0]}")
print(f"\tShooting Guard: \t{players[1]}")
print(f"\tsmall Forward: \t\t{players[2]}")
print(f"\tpower Forward: \t\t{players[3]}")
print(f"\tcenter: \t\t{players[4]}")

#remove the injured player
injured_player = players.pop(2)

#Display injured player,number left and 
print(f"\nOh no!, {injured_player} is injured")
print(f"Your roster have only {len(players)} players. ")
replaced_player = input(f"Who will take {injured_player}'s spot? ").title()

#insert new player 
players.insert(2,replaced_player)

#Display the new list of players.
print("\n\tYour CONFIRMED! starting 5 for the upcoming bastekball season")
print(f"\tPoint Guard: \t\t{players[0]}")
print(f"\tShooting Guard: \t{players[1]}")
print(f"\tsmall Forward: \t\t{players[2]}")
print(f"\tpower Forward: \t\t{players[3]}")
print(f"\tcenter: \t\t{players[4]}")

print(f"\nGood Luck this season, {players[2]} will do well!")
print(f"Your Roster have {len(players)} players now!")

