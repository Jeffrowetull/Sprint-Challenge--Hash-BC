#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Given a list of numbers, the length of that list, and a target.
    Find the indices of the two numbers in the list that sum up to the 
    target.
    Store the list in a hash table with the numbers as the keys and 
    the indices as the values
    """
    for i in range(0,length):
        hash_table_insert(ht,weights[i],i)
    
    for i in range(0,length):
        complement = hash_table_retrieve(ht, limit-weights[i])
        if complement:
            if complement > i:
                return [complement,i]
            else:
                return [i,complement]
    


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
