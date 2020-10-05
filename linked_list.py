#Create a python menu driven program for:
#Create a link list of 5 nodes, take data from user.
#Insert an element in front, last and middle of the list.
#Delete a node from front, last and middle.
#Sort the list in ascending and descending order.
#Search a node from a sorted and unsorted list.
#Print the list.
#Count the number of nodes in the list.
def Main_menu():
    print ("This is a python menu driven program for the following options:")
    print ("\n1.Create a linked list of 5 nodes and take data from the user.")
    print ("2.Insert an element in front, last and middle of the list.")
    print ("3.Delete a node from front, last and middle.")
    print ("4.Sort the list in ascending and descending order.")
    print ("5.Search a node from a sorted and unsorted list.")
    print ("6.Print the list.")
    print ("7.Count the number of nodes in the list.")

#variable to store menu input
main_menu_input = 0

#Calling the main menu
Main_menu()

#Enter main menu input
print ("\n Please enter your input:")
main_menu_input = input()

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
  
    def __repr__(self):
      self.head = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
      node = self.head
      nodes = []
      while node is not None:
        nodes.append(node.data)
        node = node.next
      nodes.append("None")
      return "->".join(nodes)



