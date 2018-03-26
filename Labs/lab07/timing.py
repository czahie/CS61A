from lab07 import Link
from time import time
from random import randint
import argparse

def indexing_test(repetitions, size):
    """Index into both lists (of size SIZE) REPETITIONS times
    """
    pyList, linkedList = setup_lists(size)

    print("Randomly indexing into Python list {} times".format(repetitions), end=": ")
    start = time()
    for _ in range(repetitions):
        pyList[randint(0, size - 1)]
    pyTime = time() - start
    print("took " +  format(pyTime, '.6f')  + 's')

    print("Randomly indexing into linked list {} times".format(repetitions), end=": ")
    start = time()
    for _ in range(repetitions):
        get_item(linkedList, randint(0, size - 1))
    linkTime = time() - start
    print("took " + format(linkTime, '.6f') + 's')
    print("Ratio of Python List to Linked List: " + format(pyTime / linkTime, '.6f'))

def insert_test(repetitions):
    """Insert REPETITIONS elements into the 0 index of both lists.
    """
    pyList, linkedList = [], Link.empty

    print("Inserting {} items into the start of a Python list".format(repetitions), end=": ")
    start = time()
    for _ in range(repetitions):
        pyList.insert(0, 0)
    end = time()
    pyTime = end - start
    print("took " +  format(pyTime, '.6f')  + 's')

    print("Inserting {} items into the head of a linked list".format(repetitions), end=": ")
    start = time()
    for _ in range(repetitions):
        linkedList = Link(0, linkedList)
    end = time()
    linkTime = end - start
    print("took " + format(linkTime, '.6f') + 's')
    print("Ratio of Python List to Linked List: " + format(pyTime / linkTime, '.6f'))

#########
#UTILITY#
#########
def range_link(start, end):
    """Returns a Link that contains the values from START upto END.
    """
    linked = Link.empty
    current = end
    while current >= start:
        linked = Link(current, linked)
        current = current - 1
    return linked

def get_item(lst, i):
    """Iteratively traverse a linkedlist to access the item at index i
    """
    assert(i >= 0 and int(i) == i)
    while i > 0:
        lst = lst.rest
        i -= 1
    return lst.first

def setup_lists(length):
    pylist = list(range(length))
    linkedlist = range_link(0, length)
    return pylist, linkedlist


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Time operations on linked list & lists.')
    parser.add_argument('operation', choices=['insert', 'index'],
                       help='The operation to perform on the lists')
    parser.add_argument('repetitions', type=int, default=10000,
                       help='Number of time to repeat ')
    parser.add_argument('--size', type=int, default=10000,
                       help='Size of list for indexing ')
    args = parser.parse_args()

    if args.operation == 'insert':
        insert_test(args.repetitions)
    elif args.operation == 'index':
        indexing_test(args.repetitions, args.size)