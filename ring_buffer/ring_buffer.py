from doubly_linked_list import DoublyLinkedList

# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current = None
#         self.storage = DoublyLinkedList()
#         self.data = []

#     def append(self, item):
#         # pass
#         # when capacity is full append last element
#         if self.data.length == self.capacity:
#             # print("item",item)
#             # self.storage.add_to_head(item)
#             self.current = 0
#             self.storage[self.current] = item
#             self.current = (self.current + 1) % self.capacity
#         else:
#             self.storage.add_to_head(item)


#     def get(self):
#         # Note:  This is the only [] allowed
#         list_buffer_contents = []

#         # if self.storage is not None:
#             # print(self.storage.head.value)
#         return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
