"""
Write a function called safe_list which returns the last 
element of a list if an IndexError occurs. The function safe_list will take a list as the first argument and an index as the second argument.

To complete this problem, you should use a try, except block
to try to index into the list. 
If an IndexError occurs, you should return the last element of the list.
"""

def safe_list(a_list, index):
  # Your code here

  
    


if __name__ == "__main__":

  my_list = [1, 49, 9, 46, 4, 33, 9, "the last element"]

  # This should print 49
  print(safe_list(my_list, 1))

  # This should print "the last element"
  print(safe_list(my_list, 100))

