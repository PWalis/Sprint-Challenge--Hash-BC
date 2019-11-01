#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
import copy


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # Populate the hashtable
    index = 0
    for w in weights:
        hash_table_insert(ht, w, index)
        index += 1
    # Subtract the weight from the limit and check if the difference is a key in the HT
    for w in weights:
        dif = limit - w
        lookup = hash_table_retrieve(ht, dif)
        if dif == w:
            answer_0 = weights.index(w)
            answer_1 = lookup
            print(f'0{answer_0} 1{answer_1}')
            if answer_0 > answer_1:
                return (answer_0, answer_1)
            else:
                return (answer_1, answer_0)
        
        elif lookup:
            answer_0 = hash_table_retrieve(ht, w)
            answer_1 = lookup
            print(f'0{answer_0} 1{answer_1}')
            if answer_0 > answer_1:
                return (answer_0, answer_1)
            else:
                return (answer_1, answer_0)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# print(get_indices_of_item_weights([4,4], 2, 8))
ht = HashTable(16)
hash_table_insert(ht, 4, 0)
hash_table_insert(ht, 4, 1)
print(ht.storage[1].value)