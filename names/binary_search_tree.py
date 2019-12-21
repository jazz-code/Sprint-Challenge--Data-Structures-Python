# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.storage = Stack()
        self.visited = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left is not None else False
        else:
            return self.right.contains(target) if self.right is not None else False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)
    # DAY 2 Project -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

# Make a queue
# Put root in the queue
# While queue is not empty
#     pop out front of queue
# 	DO THE THING!
#     if left:
#        add left to bck of queue
#     if right:
# 	   add right to back of queue
    def in_order_print(self, node):
            pass
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
            pass
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
             # Make a queue
            queue = Queue()
            #initialize root node
            root_node = self
             # Put root in the queue
            queue.enqueue(root_node)
            # While queue is not empty
            while queue.size > 0:
                 # pop out front of queue
                current_root = queue.dequeue()
                 # 	DO THE THING!
                print(current_root.value)
                 #     if left:
                if current_root.left is not None:
                    #        add left to bck of queue
                    queue.enqueue(current_root.left)
                    #     if right:
                if current_root.right is not None:
                    # 	   add right to back of queue
                    queue.enqueue(current_root.right)





    def dft_print(self, node):
        # pass
        # self.stack = Stack()
        # self.stack.push(node)
        # while self.stack is None:
        #     self.stack.pop()
        #     print(node)
        #     if self.left is None:
        #         self.stack.push(node)
        #     if self.right is None:
        #         self.stack.push(node)

        #     Make a stack
        stack = Stack()
        # put root in stack
        root_node = self
        stack.push(root_node)
        # while stack not empty
        while stack.size > 0:
            #     pop root out of stack
            current_root = stack.pop()
            # DO THE THING!
            print(current_root.value)
            #     if left
            if current_root.left is not None:
            #    add left to stack
                stack.push(current_root.left)
            #    if right
            if current_root.right is not None:
            #     add right to stack
                stack.push(current_root.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required
    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

""" *** Queue *** """
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev



class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()
        # self.value = []
        self.head = None
        self.last = None

    def enqueue(self, value):
        # if self.last is None:
        #     self.head = DoublyLinkedList()
        #     self.last = self.head
        # else:
        #     self.last.next = DoublyLinkedList()
        #     self.last = self.last.next
        self.storage.add_to_tail(value)
        self.size +=1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1

            return self.storage.remove_from_head()

    def len(self):
       return self.size

""" ***Stack*** """

# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     """Wrap the given value in a ListNode and insert it
#     after this node. Note that this node could already
#     have a next node it is point to."""

#     def insert_after(self, value):
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     """Wrap the given value in a ListNode and insert it
#     before this node. Note that this node could already
#     have a previous node it is point to."""

#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     """Rearranges this ListNode's previous and next pointers
#     accordingly, effectively deleting this ListNode."""

#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # make a new node
        new_node = ListNode(value, None, None)
        # grow the length of the linked list
        self.length += 1

        # if this is not head or tail (singular node)
        if not self.head and not self.tail:
            # set the head and tail to this new node
            self.head = new_node
            self.tail = new_node
        # otherwise
        else:
            # set the new nodes Next to the current head
            new_node.next = self.head
            # set the heads prev to the new node
            self.head.prev = new_node
            # set the head ref to the new node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # set the return value to the value of the head
        value = self.head.value
        # delete head
        self.delete(self.head)
        # return the value
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # make a new node
        new_node = ListNode(value, None, None)
        # grow the length of the linked list
        self.length += 1

        # if this is not head or tail (singular node)
        if not self.head and not self.tail:
            # set the head and tail to this new node
            self.head = new_node
            self.tail = new_node
        # otherwise
        else:
            # set the new nodes Prev to the current tail
            new_node.prev = self.tail
            # set the tails next to the new node
            self.tail.next = new_node
            # set the tail ref to the new node
            self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # set the return value to the tail value
        value = self.tail.value
        # delete the tail
        self.delete(self.tail)
        # return the value
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # if node is head then return
        if node is self.head:
            return
        # set value to nodes value
        value = node.value
        # if the node is the tail
        if node is self.tail:
            # remove node from tail
            self.remove_from_tail()
        # otherwise
        else:
            # delete the node
            node.delete()
            # decrement the length
            self.length -= 1

        # add the value to the head
        self.add_to_head(value)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # if node is tail then return
        if node is self.tail:
            return
        # set value to nodes value
        value = node.value
        # if the node is the head
        if node is self.head:
            # remove node from head
            self.remove_from_head()
        # otherwise
        else:
            # delete the node
            node.delete()
            # decrement the length
            self.length -= 1

        # add the value to the tail
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # decrement the length
        self.length -= 1
        # if not head or tail return
        if not self.head and not self.tail:
            return
        # if the head is the tail
        if self.head == self.tail:
            # set the head and tail to none
            self.head = None
            self.tail = None
        # otherwise if head is the node
        elif self.head == node:
            # set the head to the nodes next
            self.head = node.next
            # delete node
            node.delete()
        # otherwise if tail is the node
        elif self.tail == node:
            # set the tail to the nodes prev
            self.tail = node.prev
            # delete node
            node.delete()
        # otherwise
        else:
            # delete node
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # if no head the return None
        if not self.head:
            return None
        # set the initial max value to the heads value
        max_value = self.head.value
        # set current node to head
        current_node = self.head
        # loop over nodes while current exists
        while current_node:
            # if current value is greater than the max value
            if current_node.value > max_value:
                # set the max value to the current value
                max_value = current_node.value
            # move to the next node
            current_node = current_node.next
        # return max value
        return max_value

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        if self.storage.head is None:
            self.storage.add_to_head(value)
            self.size += 1
        else:
            self.storage.add_to_head(value)
            self.size += 1

    def pop(self):
        if self.storage.head is None:
            return None
        else:
            if self.size > 0:
                self.size -= 1

        return self.storage.remove_from_tail()

    def len(self):
        return self.size
