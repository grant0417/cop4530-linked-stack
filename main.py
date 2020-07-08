# A linked stack data structure for COP 4530 by Team Nevada
# Thomas Hall (Requirements)
# Grant Gurvis (Developer)
# Austin Hadsock (Tester)
# Brian Guenzatti (Tester)

# Imports python standard libraries
import ast
import os
import pprint
import sys
from typing import Optional, Any


class LinkedList:
    next: Optional['LinkedList']
    item: Any

    # A very basic linked list that holds an item
    def __init__(self, item: Any):
        self.item = item
        self.next = None

    def __repr__(self):
        return pprint.pformat(vars(self))

    def copy(self) -> 'LinkedList':
        self_copy = LinkedList(self.item)
        if self.next is not None:
            self_copy.next = self.next.copy()
        return self_copy


class LinkedStack:
    linked_list: Optional['LinkedList']
    stack_size: int
    itop: int

    # A stack implemented using linked lists
    def __init__(self):
        # The current index in the head array that is the top
        self.itop = 0
        # Number of items currently in the stack
        self.stack_size = 0
        # Head of the LinkedList
        self.linked_list = None

    def __repr__(self):
        return pprint.pformat(vars(self))

    # Makes a deep copy of the LinkedStack
    def copy(self) -> 'LinkedStack':
        self_copy = LinkedStack()
        self_copy.itop = self.itop
        self_copy.stack_size = self.stack_size
        if self.linked_list is not None:
            self_copy.linked_list = self.linked_list.copy()
        return self_copy

    # Returns true if the stack is empty
    def empty(self) -> bool:
        return self.stack_size == 0

    # Returns the number of items on the stack
    def size(self) -> int:
        return self.stack_size

    # Returns the number of nodes in the linked list
    def list_size(self) -> int:
        return (self.stack_size + 7) // 8

    # Returns the top item on the stack without popping it off
    def top(self):
        # Returns an exception if the stack is empty
        if self.stack_size == 0:
            raise Exception("Underflow")
        else:
            return self.linked_list.item[self.itop]

    # Swaps the contents of two LinkedStacks
    def swap(self, other_stack: 'LinkedStack') -> None:
        tmp_itop = other_stack.itop
        tmp_stack_size = other_stack.stack_size
        tmp_linked_list_head = other_stack.linked_list

        other_stack.itop = self.itop
        other_stack.stack_size = self.stack_size
        other_stack.linked_list = self.linked_list

        self.itop = tmp_itop
        self.stack_size = tmp_stack_size
        self.linked_list = tmp_linked_list_head

    # Pushes an item onto the stack
    def push(self, item: Any) -> None:
        # Stack is empty
        if self.linked_list is None:
            self.linked_list = LinkedList([None] * 8)
            self.linked_list.item[0] = item
            self.itop = 0
            self.stack_size = 1
        # Array is full, new node needed
        elif self.itop == 7:
            self.itop = 0
            self.stack_size += 1
            next_head = LinkedList([None] * 8)
            next_head.item[0] = item
            next_head.next = self.linked_list
            self.linked_list = next_head
        # Places item
        else:
            self.itop += 1
            self.stack_size += 1
            self.linked_list.item[self.itop] = item

    # Pops item off the top of the stack
    def pop(self) -> Any:
        # Returns exception if the stack is empty
        if self.stack_size == 0 or self.linked_list is None:
            raise Exception("Underflow")
        else:
            item = self.linked_list.item[self.itop]
            self.linked_list.item[self.itop] = None
            self.stack_size -= 1
            # If array is empty, set new head
            if self.itop == 0:
                self.itop = 7
                self.linked_list = self.linked_list.next
            else:
                self.itop -= 1
            return item


if __name__ == "__main__":

    # Makes sure there is an input file and gets its path
    if len(sys.argv) != 2:
        raise ValueError('Please provide one file name of test file in the same directory.')
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/' + sys.argv[1]

    # Sets up stack
    stack = LinkedStack()

    # Reads from input file and prints results
    for command in open(dir_path, 'r').readlines():
        if command.startswith('Push'):
            item_string = command.lstrip('Push').strip()
            try:
                # Some ast magic to evaluate the literal to the correct type
                stack.push(ast.literal_eval(item_string))
            except ValueError:
                # ast can error if it can not evaluate the type
                print("Could not push:", item_string)
        if command.startswith('Pop'):
            print(stack.pop())
        if command.startswith('Empty'):
            print(stack.empty())
        if command.startswith('ListSize'):
            print(stack.list_size())
        if command.startswith('Top'):
            print(stack.top())
        if command.startswith('Inspect'):
            print(stack)
        if command.startswith('Clear'):
            stack = LinkedStack()
