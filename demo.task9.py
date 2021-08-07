def entity_details():
  """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """

  entity=input("Enter the name of an entity: ")
  numbers=[]
  option=input(("Enter 'x' to display or click 'a' to add:\n "))

  while option != 'x':
    numbers.append(int(input()))
    option=input("Enter 'a' or 'x'")
  return entity, numbers
a=entity_details()  
print(a)
