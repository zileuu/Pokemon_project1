entity=[]
entity.append(input("Enter entity name: ")) 
option=input("Press 'a' to add more entity or enter 'x' to display:\n ")
while option != 'x':
  print("Starting process choose:\n")
  option=input(("Enter 'x' or 'a':\n "))
  if option != 'x':
   entity.append(input())