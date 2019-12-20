from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # current = self.current
        storage = self.storage
        # when capacity is full append last element
        if storage.length is None:
            # print("item",item)
            storage.add_to_head(item)
            self.current = storage.head
        elif storage.length < self.capacity:
            # print("item add",item)
            storage.add_to_tail(item)
            self.current = storage.tail
        elif self.current is storage.tail:
            storage.remove_from_head()
            # print("item",item)
            storage.add_to_head(item)
            self.current = storage.head
        else:
            self.current.insert_after(item)
            storage.length += 1
            self.current = self.current.next
            storage.delete(self.current.next)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
